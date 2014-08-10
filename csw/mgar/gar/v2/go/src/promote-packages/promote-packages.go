// Command promote-packages analyzes the state of the catalogs, and promotes
// packages from one catalog release (unstable) to another one (testing, but
// needs to be called by name, e.g. bratislava), based on a set of rules.
//
// Packages are put in groups. Groups are defined as:
// - we start with a single package
// - we add the following related packages:
//   - all packages from the same bundle
//   - all reverse dependencies that aren't present in the target catalog
//   - all reverse dependencies (maybe not necessary)
//
// Groups of packages to be promoted are built for each pair of catalogs.
//
// We want to keep catalogs in sync. Groups from each catalog pair are matched.
// When the same group is identified across all catalog pairs, the group is
// scheduled to be promoted in all catalogs.
//
// Known issues:
// - There can be a dependency cycle between package groups. In such cases
//   integration will not work, unless the two groups are merged into one.
//   There is no code to merge groups yet.
// - This program has to be compiled with gcc-4.8.x, because gcc-4.9.{0,1}
//   produce a binary which segfaults (or the go runtime segfauls, hard to
//   tell). The bug is filed in the gcc bugzilla:
//   https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61303

package main

import (
  "bufio"
  "encoding/json"
  "flag"
  "fmt"
  "html/template"
  "io"
  "log"
  "net/http"
  "os"
  "os/exec"
  "path"
  "sort"
  "strings"
  "sync"
  "time"

  "opencsw/diskformat"
  "opencsw/mantis"
)

// Command line flags
var from_catrel_flag string
var to_catrel_flag string
var htmlReportDir string
var packageTimesFilename string
var htmlReportTemplate string
var daysOldRequired int64
var logFile string

const (
  htmlReportFile = "promote-packages.html"
)

func init() {
  flag.StringVar(&from_catrel_flag, "from-catrel", "unstable",
                 "Actually, only unstable makes sense here.")
  flag.StringVar(&to_catrel_flag, "to-catrel", "bratislava",
                 "The testing release.")
  flag.StringVar(&htmlReportDir, "html-report-path",
                 "/home/maciej/public_html",
                 "Full path to the file where the HTML report will be " +
                 "written. If the file already exists, it will be " +
                 "overwritten. ")
  flag.StringVar(&htmlReportTemplate, "html-report-template",
                 "src/promote-packages/report-template.html",
                 "HTML template used to generate the report.")
  flag.StringVar(&packageTimesFilename, "package-times-json-file",
                 "/home/maciej/.checkpkg/package-times.json",
                 "JSON file with package times state. This file is used " +
                 "for persistence: it remembers when each of the packages " +
                 "was last modified in the unstable catalog.")
  flag.Int64Var(&daysOldRequired, "required-age-in-days", 14,
                "Packages must be this number of days old before they can " +
                "be integrated.")
  flag.StringVar(&logFile, "log-file",
                 "-",
                 "The log file contains rollback information.")
}

type CatalogSpecTransition struct {
  fromCatspec diskformat.CatalogSpec
  toCatspec diskformat.CatalogSpec
}

type CatalogWithSpecTransition struct {
  fromCat diskformat.CatalogExtra
  toCat diskformat.CatalogExtra
}

// An operation that can be made on a catalog. It is a logical operation. If
// only "removed" is present it means we're removing a package. An upgrade is
// represented as a removal and an addition.
type catalogOperation struct {
  Spec diskformat.CatalogSpec
  Removed *diskformat.PackageExtra
  Added *diskformat.PackageExtra
  SourceChanged time.Time
}

// Type used to store information about the last time package was seen.
type PackageTimeInfo struct {
  Spec diskformat.CatalogSpec `json:"spec"`
  Pkg diskformat.PackageExtra `json:"pkg"`
  Present bool                `json:"present"`
  ChangedAt time.Time         `json:"changed_at"`
}

// Represents information about when certain package's state last changed. For
// example, when a package appeared in a catalog, and/or when did it disappear.
// Appearances could be tracked directly in the database, but disappearances
// couldn't. This is why we're tracking them on the client side.
type CatalogReleaseTimeInfo struct {
  Pkgs []PackageTimeInfo `json:"pkgs"`

  // For faster operations. Indexed by MD5 sums. Not serialized directly.
  catalogs map[diskformat.CatalogSpec]map[diskformat.Md5Sum]PackageTimeInfo
}

func (t *CatalogReleaseTimeInfo) Time(sourceSpec diskformat.CatalogSpec, md5Sum diskformat.Md5Sum) (time.Time, error) {
  sourceSpec.Catrel = from_catrel_flag

  if catTime, ok := t.catalogs[sourceSpec]; ok {
    if pti, ok := catTime[md5Sum]; ok {
      return pti.ChangedAt, nil
    }
    return time.Time{}, fmt.Errorf("Could not find timing for %v in %v", md5Sum, sourceSpec)
  }
  return time.Time{}, fmt.Errorf("Could not find timing information for catalog %v", sourceSpec)
}

// This means "we notice that this package is missing from the source catalog
// now." It's used when there's a package missing from the source / unstable
// catalog, and present in the testing catalog. We want to know the approximated
// deletion time. If we don't have any information, we call this function and
// this starts the timer for deletion.
func (t *CatalogReleaseTimeInfo) AddMissing(spec diskformat.CatalogSpec, p diskformat.PackageExtra) {
  spec.Catrel = from_catrel_flag
  if _, ok := t.catalogs[spec]; !ok {
    t.catalogs[spec] = make(map[diskformat.Md5Sum]PackageTimeInfo)
  }
  t.catalogs[spec][p.Md5_sum] = PackageTimeInfo{
    spec,
    p,
    false,
    time.Now(),
  }
}

func (t *CatalogReleaseTimeInfo) Load() error {
  log.Println("Loading", packageTimesFilename)
  fh, err := os.Open(packageTimesFilename)
  if err != nil {
    return t.Save()
  }
  defer fh.Close()
  r := bufio.NewReader(fh)
  dec := json.NewDecoder(r)
  if err = dec.Decode(t); err != nil {
    log.Println("Error decoding:", err)
    return err
  }
  // Move data to the unexported member.
  t.catalogs = make(map[diskformat.CatalogSpec]map[diskformat.Md5Sum]PackageTimeInfo)
  for _, p := range t.Pkgs {
    if _, ok := t.catalogs[p.Spec]; !ok {
      t.catalogs[p.Spec] = make(map[diskformat.Md5Sum]PackageTimeInfo)
    }
    t.catalogs[p.Spec][p.Pkg.Md5_sum] = p
  }
  return nil
}

// Serialize the data structure to disk.
func (t *CatalogReleaseTimeInfo) Save() error {
  // We need to move all data from the private data structure to the exported
  // one.
  t.Pkgs = make([]PackageTimeInfo, 0)
  for _, tByMd5 := range t.catalogs {
    for _, p := range tByMd5 {
      t.Pkgs = append(t.Pkgs, p)
    }
  }

  fo, err := os.Create(packageTimesFilename)
  if err != nil {
    return err
  }
  defer fo.Close()
  w := bufio.NewWriter(fo)
  defer w.Flush()
  return json.NewEncoder(w).Encode(t)
}

// Updates the timing information based on a catalog.
// SVR4 files are identified by md5 sum. Possible states:
//
//   State in cache | State in catalog | Action
//   ---------------+------------------+--------
//   nil            | -                | -
//   nil            | present          | add to cache, update ts
//   pkg-present    | -                | mark as absent, update ts
//   pkg-present    | present          | -
//   pkg-absent     | -                | -
//   pkg-absent     | present          | add to cache, update ts
//
func (t *CatalogReleaseTimeInfo) Update(c diskformat.CatalogExtra) {
  if _, ok := t.catalogs[c.Spec]; !ok {
    t.catalogs[c.Spec] = make(map[diskformat.Md5Sum]PackageTimeInfo)
  }
  inCat := make(map[diskformat.Md5Sum]bool)
  for _, p := range c.PkgsExtra {
    if pti, ok := t.catalogs[c.Spec][p.Md5_sum]; !ok || !pti.Present {
      // Packages we haven't seen yet that are in the catalog.
      t.catalogs[c.Spec][p.Md5_sum] = PackageTimeInfo{
        c.Spec,
        p,
        true,
        time.Now(),
      }
    }
    inCat[p.Md5_sum] = true
  }
  // What about packages that were removed? They are in the timing data
  // structure, but not in the catalog.
  for _, pti := range t.catalogs[c.Spec] {
    md5 := pti.Pkg.Md5_sum
    if _, ok := inCat[md5]; !ok {
      // Packages that aren't in the catalog (any more).
      p := t.catalogs[c.Spec][md5]
      // Only update the last-seen time the first time the package goes from
      // present to absent. Otherwise the entry wouldn't age.
      if p.Present {
        p.Present = false
        p.ChangedAt = time.Now()
        t.catalogs[c.Spec][md5] = p
      }
    }
  }
}

func (c catalogOperation) String() string {
  var t string = " (last change time unknown)"
  if (!c.SourceChanged.IsZero()) {
    t = (" (" + c.SourceChanged.String() + ", that is " +
         (time.Now().Sub(c.SourceChanged)).String() + " ago)")
  }
  if c.Removed != nil && c.Added != nil {
    return fmt.Sprintf("Change: %v %v → %v in %v %v",
                       c.Removed.Catalogname, c.Removed.Version,
                       c.Added.Version, c.Spec, t)
  } else if c.Removed != nil && c.Added == nil {
    return fmt.Sprintf("Removal: %v %v in %v %v",
                       c.Removed.Catalogname, c.Removed.Version,
                       c.Spec, t)
  }
  if c.Removed == nil && c.Added != nil {
    return fmt.Sprintf("Addition: %v %v in %v %v",
                       c.Added.Catalogname, c.Added.Version,
                       c.Spec, t)
  }
  return fmt.Sprintf("This operation does not remove nor add anything.")
}

// Returns the identifier of the group to which this operation should belong.
// Ideally, it's the bundle name.
func (c catalogOperation) GroupKey() (string, error) {
  if c.Removed != nil && c.Added != nil {
    if c.Removed.Bundle == "" && c.Added.Bundle == "" {
      return "", fmt.Errorf("Either source or target package's bundle is " +
                            "empty, or both: %v -> %v.", c.Removed, c.Added)
    }
    if c.Removed.Bundle == "" {
      // The removed package doesn't have a bundle but the added package has.
      // Let's say that the bundle is defined here.
      return c.Added.Bundle, nil
    }
    // When both package define a bundle, they might not agree.
    if c.Removed.Bundle == c.Added.Bundle {
      return c.Removed.Bundle, nil
    }
    return "", fmt.Errorf("It's an upgrade, but bundles don't agree, %v vs %v in %v",
                          c.Removed.Bundle, c.Added.Bundle, c)
  } else if c.Removed != nil {
    // Package removal
    if c.Removed.Bundle == "" {
      return "", fmt.Errorf("Removal, but bundle undefined: %v", c.Removed)
    }
    return c.Removed.Bundle, nil
  } else if c.Added != nil {
    // Package addition
    if c.Added.Bundle == "" {
      return "", fmt.Errorf("Addition, but bundle undefined: %v", c.Removed)
    }
    return c.Added.Bundle, nil
  }
  return "", fmt.Errorf("This should never happen: %v", c)
}

func (c catalogOperation) Catalogname() string {
  if c.Removed != nil {
    return c.Removed.Catalogname
  }
  if c.Added != nil {
    return c.Added.Catalogname
  }
  return "catalogname unknown"
}

// Returns shell/curl commands to run to perform the action, and another set to
// roll the action back.
func (c catalogOperation) Commands() []string {
  ans := make([]string, 0)
  if c.Removed != nil {
    ans = append(ans, c.Removed.CurlInvocation(c.Spec, "DELETE"))
  }
  if c.Added != nil {
    ans = append(ans, c.Added.CurlInvocation(c.Spec, "PUT   "))
  }
  return ans
}

func (c catalogOperation) Rollback() []string {
  rollback := make([]string, 0)
  if c.Added != nil {
    rollback = append(rollback, c.Added.CurlInvocation(c.Spec, "DELETE"))
  }
  if c.Removed != nil {
    rollback = append(rollback, c.Removed.CurlInvocation(c.Spec, "PUT   "))
  }
  return rollback
}

type credentials struct {
  username, password string
}

// One of the messier parts. We're running on web, so we need to ssh back to
// the login host to get the password.
func GetCredentials() credentials {
  // os.user.Current() seems not to work.
  u := os.Getenv("LOGNAME")
  if diskformat.DryRun {
    log.Println("dry run: Not trying to get the password.")
    return credentials{u, "password not necessary"}
  }
  args := []string{"login", "cat"}
  args = append(args, fmt.Sprintf("/etc/opt/csw/releases/auth/%s", u))
  log.Println("Running ssh", args)
  passwdBytes, err := exec.Command("ssh", args...).Output()
  passwd := strings.TrimSpace(string(passwdBytes))
  if err != nil {
    log.Fatalln(err);
  }
  return credentials{
    u,
    passwd,
  }
}

func RestRequest(client *http.Client, cr credentials, verb, url string) error {
  req, err := http.NewRequest(verb, url, nil)
  if err != nil {
    return err
  }
  req.SetBasicAuth(cr.username, cr.password)
  resp, err := client.Do(req)
  if err != nil {
    return err
  }
  defer resp.Body.Close()
  if resp.StatusCode >= 200 && resp.StatusCode < 300 {
    log.Println(verb, "to", url, "successful:", resp.StatusCode)
  } else {
    return fmt.Errorf("Response to %s is not a success: %+v", req, resp)
  }
  return nil
}

func (c catalogOperation) Perform(client *http.Client, cr credentials, w *os.File) error {
  if c.Removed != nil {
    url := c.Removed.UrlInCat(c.Spec)
    if !diskformat.DryRun {
      w.WriteString(fmt.Sprintf("# DELETE %s\n", url))
      if err := RestRequest(client, cr, "DELETE", url); err != nil {
        return err
      }
    } else {
      w.WriteString(fmt.Sprintf("# (dry run) DELETE %s\n", url))
      log.Println("Dry run: DELETE", url)
    }
  }
  if c.Added != nil {
    url := c.Added.UrlInCat(c.Spec)
    if !diskformat.DryRun {
      w.WriteString(fmt.Sprintf("# PUT %s\n", url))
      if err := RestRequest(client, cr, "PUT", url); err != nil {
        return err
      }
    } else {
      w.WriteString(fmt.Sprintf("# (dry run) PUT %s\n", url))
      log.Println("Dry run: PUT", url)
    }
  }
  return nil
}

// Group of packages to be moved, specific to one catalog.
type integrationGroup struct {
  Key string
  Spec diskformat.CatalogSpec
  Ops []catalogOperation
  LatestMod time.Time
}

type catalogIntegration struct {
  Spec diskformat.CatalogSpec
  Groups map[string]*integrationGroup
  Badops []catalogOperation
}

// Cross-catalog integration group. Contains the group name, all the disk
// operations, and bugs associated with the involved packages. Maybe this isn't
// the best way to represent this.
type CrossCatIntGroup struct {
  Key string
  Ops map[diskformat.CatalogSpec][]catalogOperation
  Bugs []mantis.Bug
  LatestMod time.Time
  // Which other cross catalog groups this group depends on. Catalog operations
  // which belong to this group must not be applied before applying operations
  // from all the dependencies.
  Dependencies map[string]*CrossCatIntGroup

  Evaluated bool
  CanBeIntegratedNow bool
  NeedsAttention bool
  Messages []string
}

func NewCrossCatIntGroup(key string) (*CrossCatIntGroup) {
  g := new(CrossCatIntGroup)
  g.Key = key
  g.Ops = make(map[diskformat.CatalogSpec][]catalogOperation)
  g.Bugs = make([]mantis.Bug, 0)
  g.Dependencies = make(map[string]*CrossCatIntGroup)
  return g
}

func (g CrossCatIntGroup) HasOperations() bool {
  for _, ops := range g.Ops {
    if len(ops) > 0 {
      return true
    }
  }
  return false
}

type reportData struct {
  CatalogName string
  GeneratedOn time.Time
  Catalogs []catalogIntegration
  CrossCatGroups []*CrossCatIntGroup
  TimeInfo map[diskformat.CatalogSpec]map[diskformat.Md5Sum]PackageTimeInfo
}

func groupByOsrelAndArch(cs []diskformat.CatalogSpec) map[diskformat.CatalogSpec]diskformat.CatalogSpec {
  fromIndexed := make(map[diskformat.CatalogSpec]diskformat.CatalogSpec)
  for _, f := range cs {
    i := diskformat.CatalogSpec{"fake", f.Arch, f.Osrel}
    fromIndexed[i] = f
  }
  return fromIndexed
}

func matchCatspecs(fromCats, toCats []diskformat.CatalogSpec) ([]CatalogSpecTransition) {
  transitions := make([]CatalogSpecTransition, 0)
  // We need to match the catspecs according to osrel and arch.
  fromIndexed := groupByOsrelAndArch(fromCats)
  toIndexed := groupByOsrelAndArch(toCats)
  for k, f := range fromIndexed {
    if t, ok := toIndexed[k]; ok {
      transitions = append(transitions, CatalogSpecTransition{f, t})
    } else {
      log.Println("Did not find a match for", f, "something might be wrong",
                  "with the data / the database.")
    }
  }
  return transitions
}

func fetchTwo(transition CatalogSpecTransition) (f, t diskformat.CatalogExtra) {
  chf := make(chan diskformat.CatalogExtra)
  go func(ch chan diskformat.CatalogExtra) {
    fromCat, err := diskformat.FetchCatalogExtra(transition.fromCatspec)
    if err != nil {
      log.Fatalln("Could not fetch", fromCat, "error:", err)
    }
    ch <- fromCat
  }(chf)
  cht := make(chan diskformat.CatalogExtra)
  go func(ch chan diskformat.CatalogExtra) {
    toCat, err := diskformat.FetchCatalogExtra(transition.toCatspec)
    if err != nil {
      log.Fatalln("Could not fetch", toCat, "error:", err)
    }
    ch <- toCat
  }(cht)
  return <-chf, <-cht
}

func byPkgname(c diskformat.CatalogExtra) map[string]*diskformat.PackageExtra {
  m := make(map[string]*diskformat.PackageExtra)
  // It's the typical gotcha. When we do "for _, pkg := range c.PkgsExtra", we
  // must not take the address of pkg, because it's an address to a local
  // variable.
  for i, _ := range c.PkgsExtra {
    pkg := &c.PkgsExtra[i]
    if _, ok := m[pkg.Pkgname]; ok {
      log.Fatalln("Pkgnames must be unique in a catalog.",
                  pkg.Pkgname, "occurs more than once in", c.Spec)
    }
    m[pkg.Pkgname] = pkg
  }
  return m
}

func intGroupSane(c diskformat.CatalogExtra, i *integrationGroup) error {
  // We probably want to use the existing functionality.
  // Make a copy of the catalog, because we need to manipulate it.

  pkgnames := byPkgname(c)

  for _, op := range i.Ops {
    if op.Removed != nil {
      delete(pkgnames, op.Removed.Pkgname)
    }
    if op.Added != nil {
      pkgnames[op.Added.Pkgname] = op.Added
    }
  }

  // We have sanity checks for the other catalog format. Let's transform.
  pkgs := make([]diskformat.Package, 0)
  cws := diskformat.CatalogWithSpec{c.Spec, pkgs}
  if !cws.IsSane() {
    return fmt.Errorf("Integration group %v has problems.", i.Key)
  }
  return nil
}

func GroupsFromCatalogPair(t CatalogWithSpecTransition, timing *CatalogReleaseTimeInfo) (map[string]*integrationGroup, []catalogOperation) {
  log.Println("GroupsFromCatalogPair from", t.fromCat.Spec,
              "to", t.toCat.Spec)

  // First we need to match a set of operations to perform. Then we group these
  // operations.
  fromByPkgname := byPkgname(t.fromCat)
  toByPkgname := byPkgname(t.toCat)

  oplist := make([]catalogOperation, 0)

  // Packages that are missing or different in the target catalog.
  for pkgname, pkgSrcCat := range fromByPkgname {
    if pkgDestCat, ok := toByPkgname[pkgname]; ok {
      if pkgSrcCat.Version == pkgDestCat.Version {
        // Package versions are the same. Nothing to do here.
        continue
      }
      // There is a package with the same pkgname in the target catalog.
      if pkgTime, err := timing.Time(t.toCat.Spec, pkgSrcCat.Md5_sum); err == nil {
        op := catalogOperation{t.toCat.Spec, pkgDestCat, pkgSrcCat, pkgTime}
        oplist = append(oplist, op)
      } else {
        log.Fatalln(err)
      }
    } else {
      // There is no package with the same pkgname in the target catalog.
      if pkgTime, err := timing.Time(t.toCat.Spec, pkgSrcCat.Md5_sum); err == nil {
        op := catalogOperation{t.toCat.Spec, nil, pkgSrcCat, pkgTime}
        oplist = append(oplist, op)
      } else {
        log.Fatalln(err)
      }
    }
  }

  // Packages that are only in the target catalog.
  for pkgname, topkg := range toByPkgname {
    if _, ok := fromByPkgname[pkgname]; !ok {
      if pkgTime, err := timing.Time(t.toCat.Spec, topkg.Md5_sum); err == nil {
        // Deleted package information is still in the timing information.
        op := catalogOperation{t.toCat.Spec, topkg, nil, pkgTime}
        oplist = append(oplist, op)
      } else {
        log.Println("Package", topkg.Md5_sum, topkg.Basename,
                    "has been removed from unstable, and we have never seen " +
                    "the package in unstable, and so we have no idea when it " +
                    "was removed. We'll act as if the package was removed " +
                    "just now.")
        timing.AddMissing(t.toCat.Spec, *topkg)
        op := catalogOperation{t.toCat.Spec, topkg, nil, time.Now()}
        oplist = append(oplist, op)
      }
    }
  }
  log.Println("Found", len(oplist), "oplist")

  // We have the operations. Let's form groups.
  groups := make(map[string]*integrationGroup)
  badops := make([]catalogOperation, 0)
  for _, op := range oplist {
    key, err := op.GroupKey()
    if err != nil {
      log.Println("Couldn't get the group key:", op, err)
      badops = append(badops, op)
      continue
    }
    if intgroup, ok := groups[key]; !ok {
      oplist := make([]catalogOperation, 0)
      intgroup = &integrationGroup{key, op.Spec, oplist, time.Time{}}
      groups[key] = intgroup
    }
    groups[key].Ops = append(groups[key].Ops, op)
  }

  for key := range groups {
    // Set the group's latest change.
    var youngest time.Time
    for _, op := range groups[key].Ops {
      if youngest.IsZero() || op.SourceChanged.Before(youngest) {
        youngest = op.SourceChanged
      }
    }
    groups[key].LatestMod = youngest
  }

  // We need to make sure that all the dependencies are present in the target
  // catalog. We need to mock-apply the group change, and then verify that
  // there aren't any missing dependencies there.
  for key, group := range groups {
    if err := intGroupSane(t.toCat, group); err != nil {
      log.Println("Group", key, "it not sane:", err)
    }

  }
  return groups, badops
}

func transitions() []CatalogSpecTransition {
  all_catspecs, err := diskformat.GetCatalogSpecsFromDatabase()
  if err != nil {
    log.Fatalln("Could not get the catalog spec list")
  }
  log.Println("Catalogs:", from_catrel_flag, "→", to_catrel_flag)
  from_catspecs := diskformat.FilterCatspecs(all_catspecs, from_catrel_flag)
  to_catspecs := diskformat.FilterCatspecs(all_catspecs, to_catrel_flag)
  return matchCatspecs(from_catspecs, to_catspecs)
}

// The idea of creating a pipeline in this fashion is that a function call
// generates a channel and closes it after all data are written to it.
// The closure inside this function looks weird, but its scope is the same as
// the scope of the function, so it quickly becomes natural to read, and keeps
// related pieces of code together.

// Stage 1 has no input, and produces a series of catalog spec transitions.
func pipeStage1() <-chan CatalogSpecTransition {
  out := make(chan CatalogSpecTransition)
  go func() {
    for _, t := range transitions() {
      out <- t
    }
    close(out)
  }()
  return out
}

// Fetches data from the REST interface.
func pipeStage2(in <-chan CatalogSpecTransition) <-chan CatalogWithSpecTransition {
  out := make(chan CatalogWithSpecTransition)
  go func() {
    for t := range in {
      fromCat, toCat := fetchTwo(t)
      out <-CatalogWithSpecTransition{fromCat, toCat}
    }
    close(out)
  }()
  return out
}

func writeReport(rd reportData) {
  t := template.Must(template.ParseFiles(htmlReportTemplate))
  outFile := path.Join(htmlReportDir, htmlReportFile)
  fo, err := os.Create(outFile)
  if err != nil {
    log.Println("Could not open", outFile)
    panic(err)
  }
  defer fo.Close()
  if err := t.Execute(fo, rd); err != nil {
    log.Fatal("Could not write the report:", err)
  }
  log.Println("The report has been written to", outFile)
}

type ByKey []*CrossCatIntGroup

func (a ByKey) Len() int { return len(a) }
func (a ByKey) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a ByKey) Less(i, j int) bool { return a[i].Key < a[j].Key }

func addBlockingBugs(groups map[string]*CrossCatIntGroup, mantisBugs <-chan mantis.Bug) {
  // Severities from mantis that don't block package promotions.
  lowSeverities := [...]string{
    "Trivial",
    "Minor",
    "Feature",
  }

  // Add blocking Mantis Bugs.
  bugsByCatname := make(map[string][]mantis.Bug)
  for bug := range mantisBugs {
    // Bugs that aren't blockers.
    if bug.Status == "Closed" || bug.Status == "Resolved" {
      continue
    }
    shouldSkip := false
    for _, sev := range lowSeverities {
      if bug.Severity == sev {
        shouldSkip = true
        break
      }
    }
    if shouldSkip {
      continue
    }
    c := bug.Catalogname
    if _, ok := bugsByCatname[c]; !ok {
      bugsByCatname[c] = make([]mantis.Bug, 0)
    }
    bugsByCatname[c] = append(bugsByCatname[c], bug)
  }

  for _, g := range groups {
    catNames := make(map[string]bool)
    for _, ops := range g.Ops {
      for _, op := range ops {
        catNames[op.Catalogname()] = true
      }
    }
    for catName, _ := range catNames {
      g.Bugs = append(g.Bugs, bugsByCatname[catName]...)
    }
  }
}

// Find the last time.
func setLatestModifications(groups map[string]*CrossCatIntGroup) {
  // The latest operation in the group is the time of the whole group.
  for key := range groups {
    var t time.Time
    for _, opslice := range groups[key].Ops {
      for _, op := range opslice {
        if t.IsZero() || t.Before(op.SourceChanged) {
          t = op.SourceChanged
        }
      }
    }
    groups[key].LatestMod = t
  }
}

// Add dependencies. In every group:
// - For each catalog
//   - For each added package
//     - For each dependency of an added package
//       - If there is another group which changes/adds this package,
//         that group must be included in this group.
//       - If there isn't another group which adds the package, the package
//         must be already in the target catalog.
//
// Ingredients needed:
// - groups to modify
// - contents of the target catalog
func addDependencies(groups map[string]*CrossCatIntGroup, targetCatByPkgname map[diskformat.CatalogSpec]map[string]*diskformat.PackageExtra) {
  groupProvides := make(map[diskformat.CatalogSpec]map[string]*CrossCatIntGroup)
  for _, group := range groups {
    for spec, ops := range group.Ops {
      for _, op := range ops {
        if _, ok := groupProvides[spec]; !ok {
          groupProvides[spec] = make(map[string]*CrossCatIntGroup)
        }
        if op.Added != nil {
          groupProvides[spec][op.Added.Pkgname] = group
        }
      }
    }
  }

  for _, group := range groups {
    for spec, ops := range group.Ops {
      for _, op := range ops {
        if op.Added != nil {
          for _, dep := range op.Added.Deps {
            // A dependency of this group
            //
            // What if one group removes a package and another group depends on it?
            // This is only possible if the source catalog is broken.
            // Maybe we should still add some checks for it?

            if pkgByPkgname, ok := targetCatByPkgname[spec]; ok {
              if _, ok := pkgByPkgname[dep]; !ok {
                // No catalog provides this dependency. But there is stil hope!
                // Maybe one of the groups provides the package?
                if groupByPkgname, ok := groupProvides[spec]; ok {
                  if groupProviding, ok := groupByPkgname[dep]; ok {
                    if groupProviding.Key != group.Key {
                      group.Dependencies[groupProviding.Key] = groupProviding
                      // We could also add some information why this dependency is needed here.
                    }
                  } else {
                    log.Fatalln("The", groupProviding.Key, "group doesn't provide", dep)
                  }
                } else {
                  log.Fatalln("Catalog", spec, "does not provide package", dep,
                              "which is required by package",
                              op.Added.Basename, op.Added.Md5_sum)
                }
              }
            } else {
              log.Fatalln("targetCatByPkgname does not provide catalog", spec)
            }
          }
        }
      }
    }
  }
}

func canBeIntegrated(groups map[string]*CrossCatIntGroup) {
  requiredAge := time.Duration(time.Hour * (-24) * time.Duration(daysOldRequired))
  now := time.Now()
  for key := range groups {
    problems := make([]string, 0)
    // I can't make sense of the Before/After thing here.
    if now.Add(requiredAge).Before(groups[key].LatestMod) {
      age := now.Sub(groups[key].LatestMod)
      reqAge := (-1) * requiredAge
      timeLeft := reqAge - age
      msg := fmt.Sprintf("Not old enough: %v, but %v age is required (%v days), %v left.",
                         age, reqAge, daysOldRequired, timeLeft)
      problems = append(problems, msg)
    }
    if len(groups[key].Bugs) > 0 {
      msg := fmt.Sprintf("Critical bugs")
      problems = append(problems, msg)
      groups[key].NeedsAttention = true
    }
    if len(groups[key].Dependencies) > 0 {
      msg := ("This group depends on other groups. We cannot " +
          "evaluate all groups recursively because of a potential graph " +
          "cycle. " +
          "Dependencies will be integrated first, this " +
          "group will be processed in the next iteration.")
      problems = append(problems, msg)
    }
    groups[key].CanBeIntegratedNow = len(problems) == 0
    groups[key].Evaluated = true
    groups[key].Messages = append(groups[key].Messages, problems...)
  }
}

// Analyzes the data.
func pipeStage3(in <-chan CatalogWithSpecTransition, mantisBugs <-chan mantis.Bug) <-chan reportData {
  out := make(chan reportData)
  go func() {
    // Catalog timing information
    timing := new(CatalogReleaseTimeInfo)
    if err := timing.Load(); err != nil {
      log.Fatalln("Could not read the timing information:", err,
                  "-- If this is the first run, please create an empty file with",
                  "the '{}' contents, location:", packageTimesFilename)
    }
    rd := reportData{
      to_catrel_flag,
      time.Now(),
      make([]catalogIntegration, 0),
      make([]*CrossCatIntGroup, 0),
      timing.catalogs,
    }

    // To discover dependencies later.
    // We need to go from package name to md5 sum
    // Then from package name to another integration group
    //
    // Pointer business again, to save memory. It will probably not work as expected.
    targetCatByPkgname := make(map[diskformat.CatalogSpec]map[string]*diskformat.PackageExtra)

    for t := range in {
      timing.Update(t.fromCat)
      groups, badops := GroupsFromCatalogPair(t, timing)
      rd.Catalogs = append(
          rd.Catalogs,
          catalogIntegration{t.fromCat.Spec, groups, badops})
      if _, ok := targetCatByPkgname[t.toCat.Spec]; !ok {
        targetCatByPkgname[t.toCat.Spec] = make(map[string]*diskformat.PackageExtra)
      }
      for i := range t.toCat.PkgsExtra {
        targetCatByPkgname[t.toCat.Spec][t.toCat.PkgsExtra[i].Pkgname] = &t.toCat.PkgsExtra[i]
      }
    }

    // We're walking the reportData structure and populating the
    // CrossCatIntGroup structures. This is about combining updates across all
    // catalogs into one group that will be examined as a whole.
    groups := make(map[string]*CrossCatIntGroup)
    for _, r := range rd.Catalogs {
      for key, srcIntGroup := range r.Groups {
        var group *CrossCatIntGroup
        group, ok := groups[key]
        if !ok {
          group = NewCrossCatIntGroup(key)
          groups[key] = group
        }
        // We have our CrossCatIntGroup now.
        if _, ok := group.Ops[srcIntGroup.Spec]; !ok {
          group.Ops[srcIntGroup.Spec] = make([]catalogOperation, 0)
        }
        group.Ops[srcIntGroup.Spec] = append(group.Ops[srcIntGroup.Spec],
                                             srcIntGroup.Ops...)
      }
    }

    setLatestModifications(groups)
    addBlockingBugs(groups, mantisBugs)
    addDependencies(groups, targetCatByPkgname)
    canBeIntegrated(groups)

    // Sort by group / bundle name
    for _, g := range groups {
      rd.CrossCatGroups = append(rd.CrossCatGroups, g)
    }
    sort.Sort(ByKey(rd.CrossCatGroups))

    out <- rd

    if err := timing.Save(); err != nil {
      log.Fatalln("Could not save the timing information:", err)
    }

    // We close the channel as the last thing, because we need to make sure
    // that the main goroutine doesn't exit before we finish writing the report.
    close(out)
  }()
  return out
}

func mantisChan() <-chan mantis.Bug {
  mch := make(chan mantis.Bug)
  go func(ch chan mantis.Bug) {
    log.Println("Fetching bugs from mantis")
    bugs, err := mantis.FetchBugs()
    if err != nil {
      log.Fatalln("Fetching bugs failed.")
    }
    log.Println("Fetched", len(bugs), "bugs from Mantis")
    for _, bug := range bugs {
      ch <-bug
    }
    close(ch)
  }(mch)
  return mch
}

// From http://blog.golang.org/pipelines
func merge(cs ...<-chan CatalogWithSpecTransition) <-chan CatalogWithSpecTransition {
    var wg sync.WaitGroup
    out := make(chan CatalogWithSpecTransition)

    // Start an output goroutine for each input channel in cs.  output
    // copies values from c to out until c is closed, then calls wg.Done.
    output := func(c <-chan CatalogWithSpecTransition) {
        for n := range c {
            out <- n
        }
        wg.Done()
    }
    wg.Add(len(cs))
    for _, c := range cs {
        go output(c)
    }

    // Start a goroutine to close out once all the output goroutines are
    // done.  This must start after the wg.Add call.
    go func() {
        wg.Wait()
        close(out)
    }()
    return out
}

func maybeApplyChanges(rd reportData, cr credentials) {
  // Depends on dry_run.
  logBasename := fmt.Sprintf(time.Now().Format("catalog-integrations-2006-01.log"))
  runLog := path.Join(htmlReportDir, logBasename)
  fo, err := os.OpenFile(runLog, os.O_RDWR | os.O_CREATE | os.O_APPEND, 0644)
  if err != nil {
    log.Fatalln("Could not write to", runLog)
  }
  defer fo.Close()

  timestampWritten := false
  client := new(http.Client)
  for _, group := range rd.CrossCatGroups {
    if !group.Evaluated {
      log.Println("Group", group.Key, "was not evaluated, changes will not be applied.")
      continue
    }
    if !group.CanBeIntegratedNow {
      log.Println("Group", group.Key, "is not marked for integration now.")
      continue
    }
    if !group.HasOperations() {
      log.Println("Group", group.Key, "has no operations to perform.")
      continue
    }
    if !timestampWritten {
      fo.WriteString(fmt.Sprintf("# STARTED %s\n", rd.GeneratedOn))
      timestampWritten = true
    }
    log.Println("Continuing to process changes for", group.Key)
    fo.WriteString(fmt.Sprintf("# PERFORMING %s\n", group.Key))
    for _, ops := range group.Ops {
      for _, op := range ops {
        if err := op.Perform(client, cr, fo); err != nil {
          // This error contains auth info.
          // fo.WriteString(fmt.Sprintf("# ERROR: %s\n", err))
          log.Fatalf("Performing '%s' has failed: %s", op, err)
        }
      }
    }
    fo.WriteString(fmt.Sprintf("# ROLLBACK FOR %s\n", group.Key))
    for _, ops := range group.Ops {
      for _, op := range ops {
        for _, line := range op.Rollback() {
          fo.WriteString(fmt.Sprintf("%s\n", line))
        }
      }
    }
  }
  if timestampWritten {
    fo.WriteString(fmt.Sprintf("# FINISHED %s\n", rd.GeneratedOn))
  }
}

func main() {
  programStart := time.Now()
  flag.Parse()

  log.SetFlags(log.Llongfile | log.Ldate | log.Ltime)
  if logFile != "-" {
    fo, err := os.OpenFile(logFile, os.O_RDWR | os.O_CREATE | os.O_APPEND, 0644)
    if err != nil {
      log.Println("Could not create the log file:", err)
      return
    }
    defer fo.Close()
    log.Println("Writing an additional copy of the log to", logFile)
    log.SetOutput(io.MultiWriter(os.Stdout, fo))
  }

  log.Println("Program start")

  crch := make(chan credentials)
  go func(crch chan credentials) {
    crch <- GetCredentials()
  }(crch)

  mch := mantisChan()
  tch := pipeStage1()
  // Parallelization of the pipeline.
  cch1 := pipeStage2(tch)
  cch2 := pipeStage2(tch)
  cch3 := pipeStage2(tch)
  rch := pipeStage3(merge(cch1, cch2, cch3), mch)

  for rd := range rch {
    writeReport(rd)
    maybeApplyChanges(rd, <-crch)
  }
  log.Println("Finished, running time: ", time.Since(programStart))
}

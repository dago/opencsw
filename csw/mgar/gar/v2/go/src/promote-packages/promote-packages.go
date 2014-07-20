// Command promote-packages analyzes the state of the catalogs, and promotes
// packages from one catalog (unstable) to another one, based on a set of
// rules.
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
// Features missing:
// - adding dependencies to a group
// - tracking the times when a package appeared or disappeared in a catalog
//   (for time accounting)
// - making changes to the testing catalog
//
// This program has to be compiled with gcc-4.8.2, because gcc-4.9.0 produces
// a binary which segfaults (or the go runtime segfauls, hard to tell). 
// The bug is filed in the gcc bugzilla:
// https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61303

package main

import (
  "bufio"
  "encoding/json"
  "flag"
  "fmt"
  "html/template"
  "log"
  "os"
  "sort"
  "sync"
  "time"

  "opencsw/diskformat"
  "opencsw/mantis"
)

// Command line flags
var from_catrel_flag string
var to_catrel_flag string

const htmlReportPath = "/home/maciej/public_html/promote-packages.html"

func init() {
  flag.StringVar(&from_catrel_flag, "from-catrel", "unstable",
                 "Actually, only unstable makes sense here.")
  flag.StringVar(&to_catrel_flag, "to-catrel", "bratislava",
                 "The testing release.")
}

type CatalogSpecTransition struct {
  fromCatspec diskformat.CatalogSpec
  toCatspec diskformat.CatalogSpec
}

// CONTINUE FROM HERE: The challenge is to plug in the time information. We
// need to combine the data from REST with previously serialized data.
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
  // Maybe add timing information here?
  SourceChanged *time.Time
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

  // For faster operations. Indexed by MD5 sums. Not serialized.
  catalogs map[diskformat.CatalogSpec]map[diskformat.Md5Sum]PackageTimeInfo
}

func (t *CatalogReleaseTimeInfo) Get(spec diskformat.CatalogSpec, md5_sum string) PackageTimeInfo {
  return PackageTimeInfo{}
}

const packageTimesFilename = "/home/maciej/.checkpkg/package-times.json"

func (t *CatalogReleaseTimeInfo) Load() error {
  log.Println("Loading", packageTimesFilename)
  fh, err := os.Open(packageTimesFilename)
  if err != nil {
    // return err
    // Maybe just create an empty one?
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
// Packages are matched by md5 sum. Possible states:
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
    // Indexed by MD5 sum.
    t.catalogs[c.Spec] = make(map[diskformat.Md5Sum]PackageTimeInfo)
  }
  inCat := make(map[diskformat.Md5Sum]bool)
  for _, p := range c.PkgsExtra {
    if _, ok := t.catalogs[c.Spec][p.Md5_sum]; !ok {
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
      p.Present = false
      p.ChangedAt = time.Now()
      t.catalogs[c.Spec][md5] = p
    }
  }
}

func (c catalogOperation) String() string {
  if c.Removed != nil && c.Added != nil {
    return fmt.Sprintf("Change: %v %v → %v in %v",
                       c.Removed.Catalogname, c.Removed.Version,
                       c.Added.Version, c.Spec)
  } else if c.Removed != nil && c.Added == nil {
    return fmt.Sprintf("Removal: %v %v in %v",
                       c.Removed.Catalogname, c.Removed.Version,
                       c.Spec)
  }
  if c.Removed == nil && c.Added != nil {
    return fmt.Sprintf("Addition: %v %v in %v",
                       c.Added.Catalogname, c.Added.Version,
                       c.Spec)
  }
  return fmt.Sprintf("What?")
}

// Returns the identifier of the group to which this operation should belong.
// Ideally, it's the bundle name.
func (c catalogOperation) GroupKey() (string, error) {
  if c.Removed != nil && c.Added != nil {
    if c.Removed.Bundle == "" && c.Added.Bundle == "" {
      return "", fmt.Errorf("Either source or target package's bundle is empty, or both: %v -> %v.", c.Removed, c.Added)
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
    ans = append(ans,
                 fmt.Sprintf("curl --netrc -X DELETE %s/catalogs/%s/%s/%s/%s/",
                 diskformat.ReleasesUrl,
                 c.Spec.Catrel, c.Spec.Arch, c.Spec.Osrel,
                 c.Removed.Md5_sum))
  }
  if c.Added != nil {
    ans = append(ans,
                 fmt.Sprintf("curl --netrc -X PUT    %s/catalogs/%s/%s/%s/%s/",
                 diskformat.ReleasesUrl,
                 c.Spec.Catrel, c.Spec.Arch, c.Spec.Osrel,
                 c.Added.Md5_sum))
  }
  return ans
}

func (c catalogOperation) Rollback() []string {
  rollback := make([]string, 0)
  if c.Added != nil {
    rollback = append(rollback,
                      fmt.Sprintf("curl --netrc -X DELETE %s/catalogs/%s/%s/%s/%s/",
                      diskformat.ReleasesUrl,
                      c.Spec.Catrel, c.Spec.Arch, c.Spec.Osrel,
                      c.Added.Md5_sum))
  }
  if c.Removed != nil {
    rollback = append(rollback,
                      fmt.Sprintf("curl --netrc -X PUT    %s/catalogs/%s/%s/%s/%s/",
                      diskformat.ReleasesUrl,
                      c.Spec.Catrel, c.Spec.Arch, c.Spec.Osrel,
                      c.Removed.Md5_sum))
  }
  return rollback
}

type integrationGroup struct {
  Key string
  Spec diskformat.CatalogSpec
  Ops []catalogOperation
}

type IntegrationResult struct {
  noidea string
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
}

func NewCrossCatIntGroup(key string) (*CrossCatIntGroup) {
  g := new(CrossCatIntGroup)
  g.Key = key
  g.Ops = make(map[diskformat.CatalogSpec][]catalogOperation)
  g.Bugs = make([]mantis.Bug, 0)
  return g
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

func GroupsFromCatalogPair(t CatalogWithSpecTransition) (map[string]*integrationGroup, []catalogOperation) {
  // No Mantis integration yet.
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
      op := catalogOperation{t.toCat.Spec, pkgDestCat, pkgSrcCat, nil}
      oplist = append(oplist, op)
    } else {
      // There is no package with the same pkgname in the target catalog.
      op := catalogOperation{t.toCat.Spec, nil, pkgSrcCat, nil}
      oplist = append(oplist, op)
    }
  }

  // Packages that are only in the target catalog.
  for pkgname, topkg := range toByPkgname {
    if _, ok := fromByPkgname[pkgname]; !ok {
      op := catalogOperation{t.toCat.Spec, topkg, nil, nil}
      oplist = append(oplist, op)
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
      intgroup = &integrationGroup{key, op.Spec, oplist}
      groups[key] = intgroup
    }
    groups[key].Ops = append(groups[key].Ops, op)
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
  t := template.Must(template.ParseFiles(
      "src/promote-packages/report-template.html"))
  fo, err := os.Create(htmlReportPath)
  if err != nil {
    log.Println("Could not open", htmlReportPath)
    panic(err)
  }
  defer fo.Close()
  log.Println("Writing HTML")
  if err := t.Execute(fo, rd); err != nil {
    log.Fatal("Could not write the report:", err)
  }
  log.Println("The report has been written.")
}

type ByKey []*CrossCatIntGroup

func (a ByKey) Len() int { return len(a) }
func (a ByKey) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a ByKey) Less(i, j int) bool { return a[i].Key < a[j].Key }

// Analyzes the data.
func pipeStage3(in <-chan CatalogWithSpecTransition, mantisBugs <-chan mantis.Bug) <-chan IntegrationResult {
  out := make(chan IntegrationResult)
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
    for t := range in {
      timing.Update(t.fromCat)
      groups, badops := GroupsFromCatalogPair(t)
      rd.Catalogs = append(
          rd.Catalogs,
          catalogIntegration{t.fromCat.Spec, groups, badops})
      msg := fmt.Sprintf("Processed data for: %+v → %+v",
                         t.fromCat.Spec, t.toCat.Spec)
      out <-IntegrationResult{msg}
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
        // We have our CrossCatIntGroup here
        if _, ok := group.Ops[srcIntGroup.Spec]; !ok {
          group.Ops[srcIntGroup.Spec] = make([]catalogOperation, 0)
        }
        group.Ops[srcIntGroup.Spec] = append(group.Ops[srcIntGroup.Spec],
                                             srcIntGroup.Ops...)
      }
    }

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

    for _, g := range groups {
      rd.CrossCatGroups = append(rd.CrossCatGroups, g)
    }
    sort.Sort(ByKey(rd.CrossCatGroups))

    // Let's write the HTML report.
    var wg sync.WaitGroup
    wg.Add(1)
    go func(rd reportData) {
      log.Println("Starting a goroutine to write the report.")
      defer wg.Done()
      writeReport(rd)
    }(rd)
    wg.Wait()

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

func main() {
  flag.Parse()
  log.Println("Program start")

  mch := mantisChan()
  tch := pipeStage1()
  cch1 := pipeStage2(tch)
  cch2 := pipeStage2(tch)
  rch := pipeStage3(merge(cch1, cch2), mch)
  for r := range rch {
    log.Println("Result:", r)
  }
}

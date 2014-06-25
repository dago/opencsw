// Package diskformat works with OpenCSW catalogs in the disk format, as they
// are provided on the master mirror at http://mirror.opencsw.org/

package diskformat

import (
  "bufio"
  "encoding/json"
  "flag"
  "fmt"
  "log"
  "net/http"
  "os"
  "path"
  "path/filepath"
  "sort"
  "strconv"
  "strings"
  "sync"
  "syscall"
  "time"
)

// When Dry Run is set, do not perform any operations on disk. Read data and
// process them, but do not write anything. Variable meant to be controlled by
// a command line flag.
var DryRun bool
// Keeping PkgdbUrl as a package global variable is probably not the best idea,
// but let's not refactor without a good plan.
var PkgdbWebUrl string
var PkgdbUrl string
var ReleasesUrl string

func init() {
  flag.StringVar(&PkgdbUrl, "pkgdb-url",
                 "http://buildfarm.opencsw.org/pkgdb/rest",
                 "Web address of the pkgdb app.")
  flag.BoolVar(&DryRun, "dry-run", false,
               "Dry run mode, no changes on disk are made")
  flag.StringVar(&PkgdbWebUrl, "pkgdb-web-url",
                 "http://buildfarm.opencsw.org/pkgdb",
                 "Web address of the pkgdb app.")
  flag.StringVar(&ReleasesUrl, "releases-url",
                 "http://buildfarm.opencsw.org/releases",
                 "Web address of the releases app.")
}

// 3 strings that define a specific catalog, e.g. "unstable sparc 5.10"
// This turns out to be one of the most fundamental data structures in this code.
type CatalogSpec struct {
  Catrel string `json:"catrel"`
  Arch string   `json:"arch"`
  Osrel string  `json:"osrel"`
}

func (cs CatalogSpec) Url() string {
  return fmt.Sprintf("%s/catalogs/%s-%s-%s/",
                     PkgdbWebUrl, cs.Catrel, cs.Arch, cs.Osrel)
}

func longOsrelAsInt(long_osrel string) int64 {
  short_osrel := shortenOsrel(long_osrel)
  fields := strings.Split(short_osrel, ".")
  if len(fields) < 2 {
    log.Fatalf("Error: %v does not conform to SunOS5.X\n", long_osrel)
  }
  sunos_version, err := strconv.ParseInt(fields[1], 10, 32)
  if err != nil {
    log.Fatalf("Could not parse %v as int\n", fields[1])
  }
  return sunos_version
}
// We want to order catalog specs by OS release, so we can go from the oldest
// Solaris releases to the newest. This specialized array implements the sorting
// order we need.
type byOsRelease []CatalogSpec
func (cs byOsRelease) Len() int { return len(cs) }
func (cs byOsRelease) Swap(i, j int) { cs[i], cs[j] = cs[j], cs[i] }
func (cs byOsRelease) Less(i, j int) bool {
  // Ordering by: 1. catrel, 2. arch, 3. osrel
  if cs[i].Catrel != cs[j].Catrel {
    return cs[i].Catrel < cs[j].Catrel
  }
  if cs[i].Arch != cs[j].Arch {
    return cs[i].Arch < cs[j].Arch
  }
  i_as_n := longOsrelAsInt(cs[i].Osrel)
  j_as_n := longOsrelAsInt(cs[j].Osrel)
  return i_as_n < j_as_n
}

// Specialized array of strings to allow automatic unmarshalling from JSON.
type PkginstSlice []string

// Format the list of pkgnames as requred by the package catalog:
// CSWfoo|CSWbar|CSWbaz; or "none" if empty.
func (p *PkginstSlice) FormatForIndexFile() string {
  if len(*p) <= 0 {
    return "none"
  }
  return strings.Join(*p, "|")
}

// Deserialize from the format output by the RESTful interface.
func (s *PkginstSlice) UnmarshalJSON(data []byte) error {
  var st string
  err := json.Unmarshal(data, &st)
  if err != nil {
    return err
  }
  *s = parseCatalogFormatPkginstList(st)
  return nil
}

// A line in the catalog file; plus the extra description field.
// As described in the manual:
// http://www.opencsw.org/manual/for-maintainers/catalog-format.html
type Package struct {
  Catalogname string     `json:"catalogname"`
  Version string         `json:"version"`
  Pkginst string         `json:"pkgname"`
  Filename string        `json:"basename"`
  Md5_sum string         `json:"md5_sum"`
  Size uint64            `json:"size"`
  Depends PkginstSlice   `json:"deps"`
  Category string        `json:"category"`
  I_depends PkginstSlice `json:"i_deps"`
  Description string     `json:"desc"`
}

// Format line as required by the catalog format.
func (p *Package) AsCatalogEntry() string {
  lst := []string{
    p.Catalogname,
    p.Version,
    p.Pkginst,
    p.Filename,
    p.Md5_sum,
    fmt.Sprintf("%v", p.Size),
    p.Depends.FormatForIndexFile(),
    p.Category,
    p.I_depends.FormatForIndexFile(),
  }
  return strings.Join(lst, " ")
}

// Format a line as required by the "descriptions" file.
func (p *Package) AsDescription() string {
  lst := []string{ p.Catalogname, "-", p.Description, }
  return strings.Join(lst, " ")
}

func (p Package) Url() string {
  return fmt.Sprintf("%s/srv4/%s/", PkgdbWebUrl, p.Md5_sum)
}

func (p Package) String() string {
  return fmt.Sprintf("%s", p.Filename)
}

type CatalogWithSpec struct {
  Spec CatalogSpec
  Pkgs []Package
}

// To avoid confusion between various things represented as strings.
type Md5Sum string

// Extra information about a package
type PackageExtra struct {
  Basename string    `json:"basename"`
  Bundle string      `json:"bundle"`
  Catalogname string `json:"catalogname"`
  Category string    `json:"category"`
  Deps []string      `json:"deps"`
  I_deps []string    `json:"i_deps"`
  Inserted_by string `json:"inserted_by"` // decode?
  Inserted_on string `json:"inserted_on"` // decode?
  Maintainer string  `json:"maintainer"`
  Md5_sum Md5Sum     `json:"md5_sum"`
  Mtime string       `json:"mtime"`  // decode?
  Pkgname string     `json:"pkgname"`
  Size int           `json:"size"`
  Version string     `json:"version"`
}

func (p PackageExtra) Url() string {
  return fmt.Sprintf("%s/srv4/%s/", PkgdbWebUrl, p.Md5_sum)
}

func (p PackageExtra) String() string {
  return fmt.Sprintf("%s", p.Basename)
}

// I'm not sure if this is a good idea.
type CatalogExtra struct {
  Spec CatalogSpec
  PkgsExtra []PackageExtra
}

const (
  symlink = iota
  hardlink
)

type linkOnDisk struct {
  file_name string
  link_type int
  target *string
}

func parseCatalogFormatPkginstList(s string) []string {
  if s == "none" {
    slice := make(PkginstSlice, 0)
    return slice
  }
  return strings.Split(s, "|")
}

// Run sanity checks and return the result. Currently only checks if there are
// any dependencies on packages absent from the catalog.
func (cws *CatalogWithSpec) IsSane() bool {
  catalog_ok := true
  deps_by_pkginst := make(map[string]PkginstSlice)
  for _, pkg := range cws.Pkgs {
    deps_by_pkginst[pkg.Pkginst] = pkg.Depends
  }
  for _, pkg := range cws.Pkgs {
    for _, dep := range pkg.Depends {
      if _, ok := deps_by_pkginst[dep]; !ok {
        log.Printf(
          "Problem in the catalog: Package %s declares dependency on %s " +
          "but %s is missing from the %s catalog.", pkg.Pkginst, dep, dep,
          cws.Spec)
        catalog_ok = false
      }
    }
  }
  return catalog_ok;
}

func (self *CatalogSpec) UnmarshalJSON(data []byte) error {
  var slice []string
  err := json.Unmarshal(data, &slice)
  if err != nil {
    return err
  }
  if len(slice) != 3 {
    return fmt.Errorf("%v is wrong length, should be 3", slice)
  }
  self.Catrel = slice[2]
  self.Arch = slice[1]
  self.Osrel = slice[0]
  return nil
}

func (s *CatalogSpec) MarshalJSON() ([]byte, error) {
  slice := []string{s.Osrel, s.Arch, s.Catrel}
  return json.Marshal(slice)
}

// Returns True when the two catalog specs match in arch and osrel.
func (s CatalogSpec) Matches(o CatalogSpec) bool {
  if s.Arch == o.Arch && s.Osrel == o.Osrel {
    if s.Catrel == o.Catrel {
      log.Println("We're matching the same catspec against itself: ", s)
    }
    return true
  }
  return false
}

func GetCatalogSpecsFromDatabase() ([]CatalogSpec, error) {
  url := fmt.Sprintf("%s/catalogs/", PkgdbUrl)
  resp, err := http.Get(url)
  if err != nil {
    return nil, err
  }
  defer resp.Body.Close()

  catspecs := make([]CatalogSpec, 0)
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&catspecs); err != nil {
    log.Println("Failed to decode JSON from", url, ":", err)
    return nil, err
  }

  if len(catspecs) <= 0 {
    return nil, fmt.Errorf("Retrieved 0 catalogs")
  }

  log.Println("GetCatalogSpecsFromDatabase returns", len(catspecs),
              "catalogs from", url)
  return catspecs, nil
}

func GetCatalogWithSpec(catspec CatalogSpec) (CatalogWithSpec, error) {
  url := fmt.Sprintf("%s/catalogs/%s/%s/%s/for-generation/as-dicts/",
                     PkgdbUrl, catspec.Catrel, catspec.Arch, catspec.Osrel)
  log.Println("Making a request to", url)
  resp, err := http.Get(url)
  if err != nil {
    log.Panicln("Could not retrieve the catalog list.", err)
    return CatalogWithSpec{}, err
  }
  defer resp.Body.Close()

  var pkgs []Package
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&pkgs); err != nil {
    log.Println("Failed to decode JSON output from", url, ":", err)
    return CatalogWithSpec{}, err
  }

  log.Println("Retrieved", catspec, "with", len(pkgs), "packages")

  cws := CatalogWithSpec{catspec, pkgs}
  if !cws.IsSane() {
    return cws, fmt.Errorf("There are sanity issues with the %s catalog. " +
                           "Please check the log for more information.",
                           cws.Spec)
  }
  return cws, nil
}

func FetchCatalogExtra(cs CatalogSpec) (CatalogExtra, error) {
  url := fmt.Sprintf("%s/catalogs/%s/%s/%s/timing/",
                     PkgdbUrl, cs.Catrel, cs.Arch, cs.Osrel)
  log.Println("Making a request to", url)
  resp, err := http.Get(url)
  if err != nil {
    log.Fatalln("Could not retrieve", url, ":", err)
    return CatalogExtra{}, err
  }
  defer resp.Body.Close()

  var pkgs []PackageExtra
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&pkgs); err != nil {
    log.Println("Failed to decode JSON output from", url, ":", err)
    return CatalogExtra{}, err
  }

  log.Println("Retrieved timing/extra info for", cs, "with", len(pkgs), "packages")

  cws := CatalogExtra{cs, pkgs}
  return cws, nil
}

// Allows to isolate specs for a given catalog release, e.g. unstable.
func FilterCatspecs(all_catspecs []CatalogSpec, catrel string) []CatalogSpec {
  catspecs := make([]CatalogSpec, 0)
  for _, catspec := range all_catspecs {
    if catspec.Catrel == catrel {
      catspecs = append(catspecs, catspec)
    }
  }
  return catspecs
}

func shortenOsrel(longosrel string) string {
  return strings.Replace(longosrel, "SunOS", "", -1)
}

func longOsrel(shortosrel string) string {
  if strings.HasPrefix(shortosrel, "SunOS") {
    return shortosrel
  } else {
    return fmt.Sprintf("SunOS%s", shortosrel)
  }
}

// Defines layout of files on disk. Can be built from the database or from
// disk.
type filesOfCatalog map[CatalogSpec]map[string]linkOnDisk

func getCatalogsFromREST(catalogs_ch chan []CatalogWithSpec, catspecs []CatalogSpec) {
  catalogs := make([]CatalogWithSpec, 0)
  var wg sync.WaitGroup
  type fetchResult struct {cws CatalogWithSpec; err error }
  ch := make(chan fetchResult)
  for _, catspec := range catspecs {
    wg.Add(1)
    go func(catspec CatalogSpec) {
      defer wg.Done()
      catalog_with_spec, err := GetCatalogWithSpec(catspec)
      if err != nil {
        log.Println("Error while retrieving the", catspec, "catalog:", err)
        ch <- fetchResult{CatalogWithSpec{}, err}
      }
      ch <- fetchResult{catalog_with_spec, nil}
    }(catspec)
  }
  // The channel will be closed when all fetches are done. We can process
  // available results in the meantime.
  go func() { wg.Wait(); close(ch) }()

  for {
    if result, ok := <-ch; !ok {
      // Channel has been closed; no more results to process.
      break
    } else if result.err != nil {
      log.Fatalln("Catalog fetch failed:", result.err,
                  "We don't want to continue, because this could result in " +
                  "wiping an existing catalog from disk because of an " +
                  "intermittent network issue.")
    } else {
      catalogs = append(catalogs, result.cws)
    }
  }
  // We have 2 places that read this data.
  catalogs_ch <- catalogs
  catalogs_ch <- catalogs
}

func getFilesOfCatalogFromDatabase(files_from_db_chan chan filesOfCatalog,
                                   catrel string, catalog_ch chan []CatalogWithSpec) {
  catalogs := <-catalog_ch
  catalogs_by_spec := make(map[CatalogSpec]CatalogWithSpec)
  catspecs := make([]CatalogSpec, 0)
  for _, cws := range catalogs {
    catalogs_by_spec[cws.Spec] = cws
    catspecs = append(catspecs, cws.Spec)
  }
  files_by_catspec := make(filesOfCatalog)
  // We must traverse catalogs in sorted order, e.g. Solaris 9 before Solaris 10.
  sort.Sort(byOsRelease(catspecs))
  visited_catalogs := make(map[CatalogSpec][]CatalogSpec)
  for _, catspec := range catspecs {
    // Used to group catalogs we can symlink from
    compatible_catspec := CatalogSpec{catspec.Catrel, catspec.Arch, "none"}
    pkgs := catalogs_by_spec[catspec].Pkgs
    for _, pkg := range pkgs {
      if _, ok := files_by_catspec[catspec]; !ok {
        files_by_catspec[catspec] = make(map[string]linkOnDisk)
      }
      var target string
      var exists_already bool
      // var exists_in_cat CatalogSpec
      // Does this path already exist? If so, we'll add a symlink.
      // Looking back at previous osrels
      if visited_compatible, ok := visited_catalogs[compatible_catspec]; ok {
        // We need to iterate in reverse order, from the newest to the oldest
        // Solaris versions.
        for i := len(visited_compatible) - 1; i >= 0; i-- {
          cand_catspec := visited_compatible[i]
          if _, ok := files_by_catspec[cand_catspec]; ok {
            if _, ok := files_by_catspec[cand_catspec][pkg.Filename]; ok {
              exists_already = true
              target = fmt.Sprintf("../%s/%s",
                                   shortenOsrel(cand_catspec.Osrel),
                                   pkg.Filename)
              break
            }
          }
        }
      }
      var link linkOnDisk
      if exists_already {
        link = linkOnDisk{pkg.Filename, symlink, &target}
      } else {
        link = linkOnDisk{pkg.Filename, hardlink, nil}
      }
      files_by_catspec[catspec][pkg.Filename] = link
    }
    if _, ok := visited_catalogs[compatible_catspec]; !ok {
      visited_catalogs[compatible_catspec] = make([]CatalogSpec, 0)
    }
    visited_catalogs[compatible_catspec] = append(visited_catalogs[compatible_catspec], catspec)
  }
  files_from_db_chan <- files_by_catspec
}

func getFilesOfCatalogFromDisk(files_from_disk_chan chan filesOfCatalog, root_path string,
                               catrel string) {
  files_by_catspec := make(filesOfCatalog)
  path_to_scan := path.Join(root_path, catrel)
  err := filepath.Walk(path_to_scan,
                       func(path string, f os.FileInfo, err error) error {
    if err != nil {
      return err
    }
    if f.Mode() & os.ModeDir > 0 {
      // We're ignoring directories.
      return nil
    }
    rel_path := strings.TrimPrefix(path, path_to_scan + "/")
    fields := strings.Split(rel_path, "/")
    if len(fields) != 3 {
      log.Println("Wrong path found:", fields)
    }
    arch := fields[0]
    osrel := longOsrel(fields[1])
    basename := fields[2]
    catspec := CatalogSpec{catrel, arch, osrel}
    // Figuring out the file type: hardlink/symlink
    var link linkOnDisk
    if !(strings.HasSuffix(basename, ".pkg.gz") ||
         strings.HasSuffix(basename, ".pkg")) {
      // Not a package, won't be processed. This means the file won't be
      // removed if not in the database.
      return nil
    }
    if f.Mode().IsRegular() {
      link = linkOnDisk{basename, hardlink, nil}
    } else if f.Mode() & os.ModeSymlink > 0 {
      target, err := os.Readlink(path)
      if err != nil {
        log.Printf("Reading link of %v failed: %v\n", path, err)
      } else {
        link = linkOnDisk{basename, symlink, &target}
      }
    } else {
      log.Println(path, "Is not a hardlink or a symlink. What is it then? Ignoring.")
    }
    if _, ok := files_by_catspec[catspec]; !ok {
      files_by_catspec[catspec] = make(map[string]linkOnDisk)
    }
    files_by_catspec[catspec][basename] = link
    return nil
  })
  if err != nil {
    log.Fatalf("filepath.Walk() failed with: %v\n", err)
  }
  files_from_disk_chan <- files_by_catspec
}

func filesOfCatalogDiff(base_files filesOfCatalog,
                        to_substract filesOfCatalog) filesOfCatalog {
  left_in_base := make(filesOfCatalog)
  for catspec, filemap := range base_files {
    for path, link := range filemap {
      // Is it in the database?
      in_db := false
      if files_db, ok := to_substract[catspec]; ok {
        if _, ok := files_db[path]; ok {
          in_db = true
        }
      }
      if !in_db {
        if _, ok := left_in_base[catspec]; !ok {
          left_in_base[catspec] = make(map[string]linkOnDisk)
        }
        left_in_base[catspec][path] = link
      }
    }
  }
  return left_in_base
}

// Returns true if there were any operations performed
func updateDisk(files_to_add filesOfCatalog,
                files_to_remove filesOfCatalog,
                catalog_root string) bool {
  changes_made := false

  for catspec, files_by_path := range files_to_add {
    for path, link := range files_by_path {
      tgt_path := filepath.Join(catalog_root, catspec.Catrel, catspec.Arch,
                                shortenOsrel(catspec.Osrel), path)
      if link.link_type == hardlink {
        src_path := filepath.Join(catalog_root, "allpkgs", path)
        if !DryRun {
          if err := syscall.Link(src_path, tgt_path); err != nil {
            log.Fatalf("Could not create hardlink from %v to %v: %v",
                       src_path, tgt_path, err)
          }
        }
        log.Printf("ln \"%s\"\n   \"%s\"\n", src_path, tgt_path)
        changes_made = true
      } else if link.link_type == symlink {
        // The source path is relative to the target, because it's a symlink
        src_path := *(link.target)
        if !DryRun {
          if err := syscall.Symlink(src_path, tgt_path); err != nil {
            log.Fatalf("Could not symlink %v to %v: %v", src_path, tgt_path, err)
          }
        }
        log.Printf("ln -s \"%s\"\n  \"%s\"\n", src_path, tgt_path)
        changes_made = true
      } else {
        log.Fatalln("Zonk! Wrong link type in %+v", link)
      }
    }
  }

  for catspec, files_by_path := range files_to_remove {
    for path, _ := range files_by_path {
      pkg_path := filepath.Join(catalog_root, catspec.Catrel, catspec.Arch,
                                shortenOsrel(catspec.Osrel), path)
      if !DryRun {
        if err:= syscall.Unlink(pkg_path); err != nil {
          log.Fatalf("Could not unlink %v: %v", pkg_path, err)
        }
      }
      log.Printf("rm \"%s\"\n", pkg_path)
      changes_made = true
    }
  }
  return changes_made
}

func formatCatalogFilePath(root_path string, catspec CatalogSpec,
                           filename string) string {
  return filepath.Join(root_path, catspec.Catrel,
                       catspec.Arch, shortenOsrel(catspec.Osrel),
                       filename)
}

func getCatalogFromIndexFile(catalog_root string,
                             catspec CatalogSpec) (*CatalogWithSpec, error) {
  pkgs := make([]Package, 0)
  // Read the descriptions first, and build a map so that descriptions can be
  // easily accessed when parsing the catalog file.
  desc_file_path := formatCatalogFilePath(catalog_root, catspec, "descriptions")
  catalog_file_path := formatCatalogFilePath(catalog_root, catspec, "catalog")
  desc_by_catalogname := make(map[string]string)
  desc_file, err := os.Open(desc_file_path)
  if err != nil {
    // Missing file is equivalent to an empty catalog.
    return &CatalogWithSpec{catspec, pkgs}, nil
  }
  defer desc_file.Close()
  desc_scanner := bufio.NewScanner(desc_file)
  for desc_scanner.Scan() {
    fields := strings.SplitN(desc_scanner.Text(), " ", 3)
    if len(fields) < 3 {
      log.Println("Could not parse description line:", fields)
      continue
    }
    catalogname := fields[0]
    description := fields[2]
    desc_by_catalogname[catalogname] = description
  }

  cat_file, err := os.Open(catalog_file_path)
  if err != nil {
    // Missing catalog file is equivalent to an empty file
    return &CatalogWithSpec{catspec, pkgs}, nil
  }
  defer cat_file.Close()

  scanner := bufio.NewScanner(cat_file)
  for scanner.Scan() {
    fields := strings.Fields(scanner.Text())
    if len(fields) != 9 {
      // Line does not conform, ignoring. It's a GPG signature line, or an
      // empty line, or something else.
      continue
    }
    catalogname := fields[0]
    desc, ok := desc_by_catalogname[catalogname]
    if !ok {
      log.Fatalln("Did not find description for", catalogname)
    }
    size, err := strconv.ParseUint(fields[5], 10, 32)
    if err != nil {
      log.Fatalln("Could not parse size")
    }
    if size <= 0 {
      log.Fatalln("Package size must be > 0:", fields[5])
    }
    deps := parseCatalogFormatPkginstList(fields[6])
    i_deps := parseCatalogFormatPkginstList(fields[8])
    pkg := Package{
      catalogname,
      fields[1],
      fields[2],
      fields[3],
      fields[4],
      size,
      deps,
      fields[7],
      i_deps,
      desc,
    }
    pkgs = append(pkgs, pkg)
  }
  if err := scanner.Err(); err != nil {
    log.Fatalf("Error reading %v: %v", catalog_file_path, err)
  }
  log.Println("Catalog index found:", catspec, "and", len(pkgs), "pkgs")
  cws := CatalogWithSpec{catspec, pkgs}
  return &cws, nil
}

func getCatalogIndexes(catspecs []CatalogSpec,
                       root_dir string) []CatalogWithSpec {
  // Read all catalog files and parse them.
  catalogs := make([]CatalogWithSpec, 0)
  for _, catspec := range catspecs {
    catalog, err := getCatalogFromIndexFile(root_dir, catspec)
    if err != nil {
      log.Fatalln("Could not get the index file of", catspec, "in",
                  root_dir, "error:", err)
    }
    catalogs = append(catalogs, *catalog)
  }
  return catalogs
}

// Struct to hold information about catalog comparisons
type catalogPair struct {
  c1 CatalogWithSpec
  c2 CatalogWithSpec
}

func groupCatalogsBySpec(c1, c2 []CatalogWithSpec) (map[CatalogSpec]catalogPair) {
  pairs_by_spec := make(map[CatalogSpec]catalogPair)
  for _, cws := range c1 {
    pairs_by_spec[cws.Spec] = catalogPair{cws, CatalogWithSpec{}}
  }
  for _, cws := range c2 {
    if pair, ok := pairs_by_spec[cws.Spec]; ok {
      pair.c2 = cws
      pairs_by_spec[cws.Spec] = pair
    } else {
      log.Println("Did not find", cws.Spec, "in c2")
    }
  }
  return pairs_by_spec
}

func massCompareCatalogs(c1, c2 []CatalogWithSpec) (map[CatalogSpec]bool) {
  diff_detected := make(map[CatalogSpec]bool)

  pairs_by_spec := groupCatalogsBySpec(c1, c2)

  // The catalog disk/db pairs are ready to be compared.
  for spec, pair := range pairs_by_spec {
    diff_detected[spec] = false
    // DeepEqual could do it, but it is too crude; doesn't provide details
    // This code can probably be simplified.
    catalognames := make(map[string]bool)
    c1_by_catn := make(map[string]Package)
    c2_by_catn := make(map[string]Package)
    if len(pair.c1.Pkgs) != len(pair.c2.Pkgs) {
      log.Printf("%v: %v vs %v are different length\n",
                 spec, len(pair.c1.Pkgs), len(pair.c2.Pkgs))
      diff_detected[spec] = true
      continue
    }
    for _, pkg := range pair.c1.Pkgs {
      catalognames[pkg.Catalogname] = true
      c1_by_catn[pkg.Catalogname] = pkg
    }
    for _, pkg := range pair.c2.Pkgs {
      catalognames[pkg.Catalogname] = true
      c2_by_catn[pkg.Catalogname] = pkg
    }
    for catalogname, _ := range catalognames {
      pkg_disk, ok := c1_by_catn[catalogname]
      if ok {
        pkg_db, ok := c2_by_catn[catalogname]
        if ok {
          // This comparison method is a bit silly. But we can't simply compare
          // the structs, because they contain slices, and slices are not
          // comparable.
          if pkg_db.AsCatalogEntry() != pkg_disk.AsCatalogEntry() {
            log.Printf("different in %v: %v %v vs %v, enough to trigger " +
                       "catalog index generation\n", spec, pkg_db.Filename,
                       pkg_db.Md5_sum, pkg_disk.Md5_sum)
            diff_detected[spec] = true
            break
          }
        } else {
          log.Printf("different in %v: %v not found in c2\n", spec, catalogname)
          diff_detected[spec] = true
          break
        }
      } else {
        log.Printf("different in %v: %v not found in c1\n", spec, catalogname)
        diff_detected[spec] = true
        break
      }
    }
  }

  return diff_detected
}

func generateCatalogIndexFile(catalog_root string,
                              cws CatalogWithSpec) {
  log.Printf("generateCatalogIndexFile(%v, %v)\n", catalog_root, cws.Spec)
  catalog_file_path := formatCatalogFilePath(catalog_root, cws.Spec, "catalog")
  desc_file_path := formatCatalogFilePath(catalog_root, cws.Spec, "descriptions")

  defer func() {
    // If there's a "catalog.gz" here, remove it. It will be recreated later by
    // the shell script which signs catalogs.
    gzip_catalog := catalog_file_path + ".gz";
    if DryRun {
      log.Println("Would have tried to remove", gzip_catalog)
      return
    }
    if err := os.Remove(gzip_catalog); err != nil {
      log.Println("Not removed", gzip_catalog, "error was", err)
    } else {
      log.Println(gzip_catalog, "was removed")
    }
  }()

  // If there are no files in the catalog, simply remove the catalog files.
  if len(cws.Pkgs) <= 0 {
    for _, filename := range []string{catalog_file_path, desc_file_path} {
      if DryRun {
        log.Println("Would have tried to remove", filename, "because the",
                    cws.Spec, "catalog is empty")
        continue
      }
      if err := os.Remove(filename); err != nil {
        // If the files are missing, that's okay
        if err != syscall.ENOENT {
          log.Println("Could not remove", filename, "error:", err)
        }
      } else {
        log.Println("Removed", filename, "because the", cws.Spec,
                    "catalog is empty")
      }
    }
    return
  }

  var catbuf *bufio.Writer
  var descbuf *bufio.Writer

  if !DryRun {
    catalog_fd, err := os.Create(catalog_file_path)
    if err != nil {
      log.Fatalln("Could not open", catalog_file_path, "for writing:", err)
    }
    defer catalog_fd.Close()

    catbuf = bufio.NewWriter(catalog_fd)
    defer catbuf.Flush()

    desc_fd, err := os.Create(desc_file_path)
    if err != nil {
      log.Fatalln("Could not open", desc_file_path, "for writing:", err)
    }
    defer desc_fd.Close()

    descbuf = bufio.NewWriter(desc_fd)
    defer descbuf.Flush()
  } else {
    log.Println("Dry run: printing catalog to stdout")
    catbuf = bufio.NewWriter(os.Stdout)
    defer catbuf.Flush()
    descbuf = bufio.NewWriter(os.Stdout)
    defer descbuf.Flush()
  }

  if err := WriteCatalogIndex(catbuf, cws); err != nil {
    log.Println("Failed while writing to", catalog_file_path,
                ":", err)
  }

  for _, pkg := range cws.Pkgs {
    descbuf.WriteString(pkg.AsDescription())
    descbuf.WriteString("\n")
  }
}

// Write the catalog file to given Writer. File format as defined by
// http://www.opencsw.org/manual/for-maintainers/catalog-format.html
func WriteCatalogIndex(w *bufio.Writer, cws CatalogWithSpec) error {
  ts_line := fmt.Sprintf("# CREATIONDATE %s\n", time.Now().Format(time.RFC3339))
  w.WriteString(ts_line)

  for _, pkg := range cws.Pkgs{
    _, err := w.WriteString(pkg.AsCatalogEntry())
    if err != nil { return err }
    _, err = w.WriteString("\n")
    if err != nil { return err }
  }
  return nil
}

// The main function of this package.
func GenerateCatalogRelease(catrel string, catalog_root string) {
  log.Println("catrel:", catrel)
  log.Println("catalog_root:", catalog_root)

  all_catspecs, err := GetCatalogSpecsFromDatabase()
  if err != nil {
    log.Fatalln("Could not get the catalog spec list:", err)
  }
  // Because of memory constraints, we're only processing 1 catalog in one run
  catspecs := FilterCatspecs(all_catspecs, catrel)

  // The plan:
  // 1. build a data structure representing all the hardlinks and symlinks
  //    based on the catalogs

  catalog_ch := make(chan []CatalogWithSpec)
  go getCatalogsFromREST(catalog_ch, catspecs)
  files_from_db_chan := make(chan filesOfCatalog)
  go getFilesOfCatalogFromDatabase(files_from_db_chan, catrel, catalog_ch)

  // 2. build a data structure based on the contents of the disk
  //    it should be done in parallel
  files_from_disk_chan := make(chan filesOfCatalog)
  go getFilesOfCatalogFromDisk(files_from_disk_chan, catalog_root, catrel)

  // 3. Retrieve results
  files_by_catspec_disk := <-files_from_disk_chan
  files_by_catspec_db := <-files_from_db_chan

  // 4. compare, generate a list of operations to perform

  log.Println("Calculating the difference")
  files_to_add := filesOfCatalogDiff(files_by_catspec_db,
                                     files_by_catspec_disk)
  files_to_remove := filesOfCatalogDiff(files_by_catspec_disk,
                                        files_by_catspec_db)

  // 5. perform these operations
  //    ...or save a disk file with instructions.
  if DryRun {
    log.Println("Dry run, only logging operations that would have been made.")
  } else {
    log.Println("Applying link/unlink operations to disk")
  }
  changes_made := updateDisk(files_to_add, files_to_remove, catalog_root)
  if !changes_made {
    if DryRun {
      log.Println("It was a dry run, but there would not have been any " +
                  "link/unlink operations performed anyway")
    } else {
      log.Println("There were no link/unlink operations to perform")
    }
  }

  // 6. Generate the catalog index files
  //    Are the current files up to date? Just that we modified linked/unlinked
  //    files on disk doesn't mean the catalog file needs to be updated.

  // Getting the content of catalog index files
  catalogs_idx_on_disk := getCatalogIndexes(catspecs, catalog_root)
  catalogs_in_db := <-catalog_ch

  diff_flag_by_spec := massCompareCatalogs(catalogs_in_db, catalogs_idx_on_disk)

  var wg sync.WaitGroup
  for _, cws := range catalogs_in_db {
    diff_present, ok := diff_flag_by_spec[cws.Spec]
    if !ok { continue }
    if diff_present {
      wg.Add(1)
      go func(catalog_root string, cws CatalogWithSpec) {
        defer wg.Done()
        generateCatalogIndexFile(catalog_root, cws)
      }(catalog_root, cws)
    } else {
      log.Println("Not regenerating", cws.Spec,
                  "because catalog contents on disk and in the database " +
                  "is the same.")
    }
  }
  wg.Wait()

  // This utility needs to be run for each catalog release, but different
  // catalog releases can be done concurrently.

  // This utility could be rewritten to regenerate all the catalogs in a single
  // run at the cost of using more RAM.
}

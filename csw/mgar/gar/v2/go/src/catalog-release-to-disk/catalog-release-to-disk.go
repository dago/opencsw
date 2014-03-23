// Generate OpenCSW catalog - symlinks and hardlinks on disk
//
// Obtains catalog contents via a REST interface, analyzes the disk state, and
// only performs the necessary operations.
//
// Building this program: See README in the go/ directory
//
// As of 2014-03-16, this program is not packaged, but instead simply compiled
// and put in place.

package main

import (
  "bufio"
  "encoding/json"
  "errors"
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

// 3 strings that define a specific catalog
type CatalogSpec struct {
  catrel string
  arch string
  osrel string
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
// Solaris releases to the newest.
type CatalogSpecs []CatalogSpec
func (cs CatalogSpecs) Len() int { return len(cs) }
func (cs CatalogSpecs) Swap(i, j int) { cs[i], cs[j] = cs[j], cs[i] }
func (cs CatalogSpecs) Less(i, j int) bool {
  // Ordering by: 1. catrel, 2. arch, 3. osrel
  if cs[i].catrel != cs[j].catrel {
    return cs[i].catrel < cs[j].catrel
  }
  if cs[i].arch != cs[j].arch {
    return cs[i].arch < cs[j].arch
  }
  i_as_n := longOsrelAsInt(cs[i].osrel)
  j_as_n := longOsrelAsInt(cs[j].osrel)
  return i_as_n < j_as_n
}

type PkginstSlice []string

func (p *PkginstSlice) FormatForIndexFile() string {
  if len(*p) <= 0 {
    return "none"
  }
  return strings.Join(*p, "|")
}

// A line in the catalog file; plus the extra description field
type PkgInCatalog struct {
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

func (p *PkgInCatalog) FormatCatalogIndexLine() string {
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

func (p *PkgInCatalog) FormatDescriptionLine() string {
  lst := []string{ p.Catalogname, "-", p.Description, }
  return strings.Join(lst, " ")
}

type Catalog []PkgInCatalog

type CatalogWithSpec struct {
  spec CatalogSpec
  pkgs Catalog
}

const (
  Symlink = iota
  Hardlink
)

type LinkOnDisk struct {
  file_name string
  link_type int
  target *string
}

func ParseCatalogFormatPkginstList(s string) []string {
  if s == "none" {
    slice := make(PkginstSlice, 0)
    return slice
  }
  return strings.Split(s, "|")
}

func (self *PkginstSlice) UnmarshalJSON(data []byte) error {
  var foo string
  err := json.Unmarshal(data, &foo)
  if err != nil {
    return err
  }
  *self = ParseCatalogFormatPkginstList(foo)
  return nil
}

// Our REST interface returns catspecs as lists, so let's have a common
// function to construct catspec structs from lists.
func MakeCatalogSpec(lst []string) (CatalogSpec, error) {
  var catspec CatalogSpec
  if len(lst) != 3 {
    return catspec, errors.New("Array of length 3 is needed.")
  }
  // We already have this in the unmarshal bit.
  catspec.catrel = lst[2]
  catspec.arch = lst[1]
  catspec.osrel = lst[0]
  return catspec, nil
}

func MakeCatalogWithSpec(catspec CatalogSpec, pkgs Catalog) CatalogWithSpec {
  var cws CatalogWithSpec
  cws.spec = catspec
  cws.pkgs = pkgs
  return cws
}

func NewPkgInCatalog(lst []string) (*PkgInCatalog, error) {
  size, err := strconv.ParseUint(lst[5], 10, 64)
  if err != nil {
    return nil, err
  }
  if size <= 0 {
    return nil, fmt.Errorf(
      "Package size must be greater than 0: %v in %v", lst[5],  lst)
  }

  depends := make([]string, 0)
  if lst[6] != "none" {
    depends = strings.Split(lst[6], "|")
  }

  i_depends := make([]string, 0)
  if lst[8] != "none" {
    i_depends = strings.Split(lst[8], "|")
  }

  var pkg PkgInCatalog
  pkg.Catalogname = lst[0]
  pkg.Version = lst[1]
  pkg.Pkginst = lst[2]
  pkg.Filename = lst[3]
  pkg.Md5_sum = lst[4]
  pkg.Size = size
  pkg.Depends = depends
  pkg.Category = lst[7]
  pkg.I_depends = i_depends
  pkg.Description = lst[9]
  return &pkg, nil
}

func (self *CatalogSpec) UnmarshalJSON(data []byte) error {
  var slice []string
  err := json.Unmarshal(data, &slice)
  if err != nil {
    return err
  }
  if len(slice) != 3 {
    return fmt.Errorf("%+v is wrong length, should be 3", slice)
  }
  self.catrel = slice[2]
  self.arch = slice[1]
  self.osrel = slice[0]
  return nil
}

func GetCatalogSpecs() (CatalogSpecs, error) {
  url := fmt.Sprintf("%s/catalogs/", pkgdb_url)
  resp, err := http.Get(url)
  if err != nil {
    return nil, err
  }
  defer resp.Body.Close()

  catspecs := make(CatalogSpecs, 0)
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&catspecs); err != nil {
    log.Println("Failed to decode JSON from", url)
    return nil, err
  }

  if len(catspecs) <= 0 {
    return nil, fmt.Errorf("Retrieved 0 catalogs")
  }

  log.Println("GetCatalogSpecs returns", len(catspecs), "catalogs from", url)
  return catspecs, nil
}

func GetCatalogWithSpec(catspec CatalogSpec) (CatalogWithSpec, error) {
  url := fmt.Sprintf("%s/catalogs/%s/%s/%s/for-generation/as-dicts/",
                     pkgdb_url, catspec.catrel, catspec.arch, catspec.osrel)
  log.Println("Making a request to", url)
  resp, err := http.Get(url)
  if err != nil {
    log.Panicln("Could not retrieve the catalog list.", err)
    return CatalogWithSpec{}, err
  }
  defer resp.Body.Close()

  var pkgs Catalog
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&pkgs); err != nil {
    log.Println("Failed to decode JSON output from", url, ":", err)
    return CatalogWithSpec{}, err
  }

  log.Println("Retrieved", catspec, "with", len(pkgs), "packages")

  cws := MakeCatalogWithSpec(catspec, pkgs)
  return cws, nil
}

func filterCatspecs(all_catspecs CatalogSpecs, catrel string) CatalogSpecs {
  catspecs := make(CatalogSpecs, 0)
  for _, catspec := range all_catspecs {
    if catspec.catrel == catrel {
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
type FilesOfCatalog map[CatalogSpec]map[string]LinkOnDisk

func GetCatalogsFromREST(catalogs_ch chan []CatalogWithSpec, catspecs CatalogSpecs) {
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
        log.Println(err)
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

func GetFilesOfCatalogFromDatabase(files_from_db_chan chan *FilesOfCatalog,
                                   catrel string, catalog_ch chan []CatalogWithSpec) {
  catalogs := <-catalog_ch
  catalogs_by_spec := make(map[CatalogSpec]CatalogWithSpec)
  catspecs := make(CatalogSpecs, 0)
  for _, cws := range catalogs {
    catalogs_by_spec[cws.spec] = cws
    catspecs = append(catspecs, cws.spec)
  }
  files_by_catspec := make(FilesOfCatalog)
  // We must traverse catalogs in sorted order, e.g. Solaris 9 before Solaris 10.
  sort.Sort(catspecs)
  visited_catalogs := make(map[CatalogSpec]CatalogSpecs)
  for _, catspec := range catspecs {
    // Used to group catalogs we can symlink from
    compatible_catspec := CatalogSpec{catspec.catrel, catspec.arch, "none"}
    pkgs := catalogs_by_spec[catspec].pkgs
    for _, pkg := range pkgs {
      if _, ok := files_by_catspec[catspec]; !ok {
        files_by_catspec[catspec] = make(map[string]LinkOnDisk)
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
                                   shortenOsrel(cand_catspec.osrel),
                                   pkg.Filename)
              break
            }
          }
        }
      }
      var link LinkOnDisk
      if exists_already {
        link = LinkOnDisk{pkg.Filename, Symlink, &target}
      } else {
        link = LinkOnDisk{pkg.Filename, Hardlink, nil}
      }
      files_by_catspec[catspec][pkg.Filename] = link
    }
    if _, ok := visited_catalogs[compatible_catspec]; !ok {
      visited_catalogs[compatible_catspec] = make(CatalogSpecs, 0)
    }
    visited_catalogs[compatible_catspec] = append(visited_catalogs[compatible_catspec], catspec)
  }
  files_from_db_chan <- &files_by_catspec
}

func GetFilesOfCatalogFromDisk(files_from_disk_chan chan *FilesOfCatalog, root_path string,
                               catrel string) {
  files_by_catspec := make(FilesOfCatalog)
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
    var link LinkOnDisk
    if !(strings.HasSuffix(basename, ".pkg.gz") ||
         strings.HasSuffix(basename, ".pkg")) {
      // Not a package, won't be processed. This means the file won't be
      // removed if not in the database.
      return nil
    }
    if f.Mode().IsRegular() {
      link = LinkOnDisk{basename, Hardlink, nil}
    } else if f.Mode() & os.ModeSymlink > 0 {
      target, err := os.Readlink(path)
      if err != nil {
        log.Printf("Reading link of %v failed: %v\n", path, err)
      } else {
        link = LinkOnDisk{basename, Symlink, &target}
      }
    } else {
      log.Println(path, "Is not a hardlink or a symlink. What is it then? Ignoring.")
    }
    if _, ok := files_by_catspec[catspec]; !ok {
      files_by_catspec[catspec] = make(map[string]LinkOnDisk)
    }
    files_by_catspec[catspec][basename] = link
    return nil
  })
  if err != nil {
    log.Fatalf("filepath.Walk() failed with: %v\n", err)
  }
  files_from_disk_chan <- &files_by_catspec
}

func FilesOfCatalogDiff(base_files *FilesOfCatalog,
                        to_substract *FilesOfCatalog) *FilesOfCatalog {
  left_in_base := make(FilesOfCatalog)
  for catspec, filemap := range *base_files {
    for path, link := range filemap {
      // Is it in the database?
      in_db := false
      if files_db, ok := (*to_substract)[catspec]; ok {
        if _, ok := files_db[path]; ok {
          in_db = true
        }
      }
      if !in_db {
        if _, ok := left_in_base[catspec]; !ok {
          left_in_base[catspec] = make(map[string]LinkOnDisk)
        }
        left_in_base[catspec][path] = link
      }
    }
  }
  return &left_in_base
}

// Returns true if there were any operations performed
func UpdateDisk(files_to_add *FilesOfCatalog,
                files_to_remove *FilesOfCatalog,
                catalog_root string) bool {
  changes_made := false

  for catspec, files_by_path := range *files_to_add {
    for path, link := range files_by_path {
      tgt_path := filepath.Join(catalog_root, catspec.catrel, catspec.arch,
                                shortenOsrel(catspec.osrel), path)
      if link.link_type == Hardlink {
        src_path := filepath.Join(catalog_root, "allpkgs", path)
        if !dry_run {
          if err := syscall.Link(src_path, tgt_path); err != nil {
            log.Fatalf("Could not create hardlink from %v to %v: %v",
                       src_path, tgt_path, err)
          }
        }
        log.Printf("ln \"%s\"\n   \"%s\"\n", src_path, tgt_path)
        changes_made = true
      } else if link.link_type == Symlink {
        // The source path is relative to the target, because it's a symlink
        src_path := *(link.target)
        if !dry_run {
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

  for catspec, files_by_path := range *files_to_remove {
    for path, _ := range files_by_path {
      pkg_path := filepath.Join(catalog_root, catspec.catrel, catspec.arch,
                                shortenOsrel(catspec.osrel), path)
      if !dry_run {
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

func FormatCatalogFilePath(root_path string, catspec CatalogSpec,
                           filename string) string {
  return filepath.Join(root_path, catspec.catrel,
                       catspec.arch, shortenOsrel(catspec.osrel),
                       filename)
}

func GetCatalogFromIndexFile(catalog_root string,
                             catspec CatalogSpec) (*CatalogWithSpec, error) {
  pkgs := make(Catalog, 0)
  // Read the descriptions first, and build a map so that descriptions can be
  // easily accessed when parsing the catalog file.
  desc_file_path := FormatCatalogFilePath(catalog_root, catspec, "descriptions")
  catalog_file_path := FormatCatalogFilePath(catalog_root, catspec, "catalog")
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
    deps := ParseCatalogFormatPkginstList(fields[6])
    i_deps := ParseCatalogFormatPkginstList(fields[8])
    pkg := PkgInCatalog{
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
  cws := MakeCatalogWithSpec(catspec, pkgs)
  return &cws, nil
}

func GetCatalogIndexes(catspecs CatalogSpecs,
                       root_dir string) []CatalogWithSpec {
  // Read all catalog files and parse them.
  catalogs := make([]CatalogWithSpec, 0)
  for _, catspec := range catspecs {
    catalog, err := GetCatalogFromIndexFile(root_dir, catspec)
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

func GroupCatalogsBySpec(c1, c2 []CatalogWithSpec) (*map[CatalogSpec]catalogPair) {
  pairs_by_spec := make(map[CatalogSpec]catalogPair)
  for _, cws := range c1 {
    pairs_by_spec[cws.spec] = catalogPair{cws, CatalogWithSpec{}}
  }
  for _, cws := range c2 {
    if pair, ok := pairs_by_spec[cws.spec]; ok {
      pair.c2 = cws
      pairs_by_spec[cws.spec] = pair
    } else {
      log.Println("Did not find", cws.spec, "in c2")
    }
  }
  return &pairs_by_spec
}

func MassCompareCatalogs(c1, c2 []CatalogWithSpec) (*map[CatalogSpec]bool) {
  diff_detected := make(map[CatalogSpec]bool)

  pairs_by_spec := GroupCatalogsBySpec(c1, c2)

  // The catalog disk/db pairs are ready to be compared.
  for spec, pair := range *pairs_by_spec {
    diff_detected[spec] = false
    // DeepEqual could do it, but it is too crude; doesn't provide details
    // This code can probably be simplified.
    catalognames := make(map[string]bool)
    c1_by_catn := make(map[string]PkgInCatalog)
    c2_by_catn := make(map[string]PkgInCatalog)
    if len(pair.c1.pkgs) != len(pair.c2.pkgs) {
      log.Printf("%v: %v vs %v are different length\n",
                 spec, len(pair.c1.pkgs), len(pair.c2.pkgs))
      diff_detected[spec] = true
      continue
    }
    for _, pkg := range pair.c1.pkgs {
      catalognames[pkg.Catalogname] = true
      c1_by_catn[pkg.Catalogname] = pkg
    }
    for _, pkg := range pair.c2.pkgs {
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
          if pkg_db.FormatCatalogIndexLine() != pkg_disk.FormatCatalogIndexLine() {
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

  return &diff_detected
}

func GenerateCatalogIndexFile(catalog_root string,
                              cws CatalogWithSpec) {
  log.Printf("GenerateCatalogIndexFile(%v, %v)\n", catalog_root, cws.spec)
  catalog_file_path := FormatCatalogFilePath(catalog_root, cws.spec, "catalog")
  desc_file_path := FormatCatalogFilePath(catalog_root, cws.spec, "descriptions")

  defer func() {
    // If there's a "catalog.gz" here, remove it. It will be recreated later by
    // the shell script which signs catalogs.
    gzip_catalog := catalog_file_path + ".gz";
    if err := os.Remove(gzip_catalog); err != nil {
      log.Println("Not removed", gzip_catalog, "error was", err)
    } else {
      log.Println(gzip_catalog, "was removed")
    }
  }()

  // If there are no files in the catalog, simply remove the catalog files.
  if len(cws.pkgs) <= 0 {
    for _, filename := range []string{catalog_file_path, desc_file_path} {
      // If the files are missing, that's okay
      if err := os.Remove(filename); err != nil {
        if err != syscall.ENOENT {
          log.Println("Could not remove", filename, "error:", err)
        }
      } else {
        log.Println("Removed", filename, "because the", cws.spec,
                    "catalog is empty")
      }
    }
    return
  }

  var catbuf *bufio.Writer
  var descbuf *bufio.Writer

  if !dry_run {
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

  // http://www.opencsw.org/manual/for-maintainers/catalog-format.html
  ts_line := fmt.Sprintf("# CREATIONDATE %s\n", time.Now().Format(time.RFC3339))
  catbuf.WriteString(ts_line)

  for _, pkg := range cws.pkgs {
    catbuf.WriteString(pkg.FormatCatalogIndexLine())
    catbuf.WriteString("\n")
    descbuf.WriteString(pkg.FormatDescriptionLine())
    descbuf.WriteString("\n")
  }
}

func GenerateCatalogRelease(catrel string, catalog_root string) {
  log.Println("catrel:", catrel)
  log.Println("catalog_root:", catalog_root)

  all_catspecs, err := GetCatalogSpecs()
  if err != nil {
    log.Panicln("Could not get the catalog spec list")
  }
  // Because of memory constraints, we're only processing 1 catalog in one run
  catspecs := filterCatspecs(all_catspecs, catrel_flag)

  // The plan:
  // 1. build a data structure representing all the hardlinks and symlinks
  //    based on the catalogs

  catalog_ch := make(chan []CatalogWithSpec)
  go GetCatalogsFromREST(catalog_ch, catspecs)
  files_from_db_chan := make(chan *FilesOfCatalog)
  go GetFilesOfCatalogFromDatabase(files_from_db_chan, catrel, catalog_ch)

  // 2. build a data structure based on the contents of the disk
  //    it should be done in parallel
  files_from_disk_chan := make(chan *FilesOfCatalog)
  go GetFilesOfCatalogFromDisk(files_from_disk_chan, catalog_root, catrel)

  // 3. Retrieve results
  files_by_catspec_disk := <-files_from_disk_chan
  files_by_catspec_db := <-files_from_db_chan

  // 4. compare, generate a list of operations to perform

  log.Println("Calculating the difference")
  files_to_add := FilesOfCatalogDiff(files_by_catspec_db,
                                     files_by_catspec_disk)
  files_to_remove := FilesOfCatalogDiff(files_by_catspec_disk,
                                        files_by_catspec_db)

  // 5. perform these operations
  //    ...or save a disk file with instructions.
  if dry_run {
    log.Println("Dry run, only logging operations that would have been made.")
  } else {
    log.Println("Applying link/unlink operations to disk")
  }
  changes_made := UpdateDisk(files_to_add, files_to_remove, catalog_root)
  if !changes_made {
    if dry_run {
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
  catalogs_idx_on_disk := GetCatalogIndexes(catspecs, catalog_root)
  catalogs_in_db := <-catalog_ch

  diff_flag_by_spec := MassCompareCatalogs(catalogs_in_db, catalogs_idx_on_disk)
  log.Println(*diff_flag_by_spec)

  var wg sync.WaitGroup
  for _, cws := range catalogs_in_db {
    diff_present, ok := (*diff_flag_by_spec)[cws.spec]
    if !ok { continue }
    if diff_present {
      wg.Add(1)
      go func(catalog_root string, cws CatalogWithSpec) {
        defer wg.Done()
        GenerateCatalogIndexFile(catalog_root, cws)
      }(catalog_root, cws)
    } else {
      log.Println("Not regenerating", cws.spec,
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

// Command line flags
var catrel_flag string
var catalog_root_flag string
var pkgdb_url string
var dry_run bool
func init() {
  flag.StringVar(&catrel_flag, "catalog-release", "unstable",
                 "e.g. unstable, bratislava, kiel, dublin")
  flag.StringVar(&catalog_root_flag, "catalog-root",
                 "/export/mirror/opencsw",
                 "Directory where all the catalogs live, and allpkgs is")
  flag.StringVar(&pkgdb_url, "pkgdb-url",
                 "http://buildfarm.opencsw.org/pkgdb/rest",
                 "Web address of the pkgdb app.")
  flag.BoolVar(&dry_run, "dry-run", false,
               "Dry run mode, no changes on disk are made")
}

func main() {
  flag.Parse()
  GenerateCatalogRelease(catrel_flag, catalog_root_flag)

  // Let's generate the catalog index too. And the description file. We've
  // already got all the necessary data. We also know whether we actually need
  // to generate a new catalog: when there were any operations to be made on
  // disk.
}

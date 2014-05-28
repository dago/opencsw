// Command promote-packages analyzes the state of the catalogs, and promotes
// packages from one catalog (unstable) to another one, based on a set of
// rules.

package main

import (
  // "bufio"
  "flag"
  "log"
  // "os"
  "opencsw/diskformat"
)

// Command line flags
var from_catrel_flag string
var to_catrel_flag string

func init() {
  flag.StringVar(&from_catrel_flag, "from-catrel", "unstable",
                 "Actually, only unstable makes sense here.")
  flag.StringVar(&to_catrel_flag, "to-catrel", "bratislava",
                 "The testing release.")
  flag.BoolVar(&diskformat.DryRun, "dry-run", true,
                 "Don't make any changes.")
  flag.StringVar(&diskformat.PkgdbUrl, "pkgdb-url",
                 "http://buildfarm.opencsw.org/pkgdb/rest",
                 "Web address of the pkgdb app.")
  flag.StringVar(&diskformat.ReleasesUrl, "releases-url",
                 "http://buildfarm.opencsw.org/releases",
                 "Web address of the releases app.")
}

type CatalogSpecTransition struct {
  fromCatspec diskformat.CatalogSpec
  toCatspec diskformat.CatalogSpec
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

func fetchTwo(transition CatalogSpecTransition) (f, t diskformat.CatalogWithSpec) {
  chf := make(chan diskformat.CatalogWithSpec)
  go func(ch chan diskformat.CatalogWithSpec) {
    fromCat, err := diskformat.GetCatalogWithSpec(transition.fromCatspec)
    if err != nil {
      log.Fatalln("Could not fetch", fromCat, "error:", err)
    }
    ch <- fromCat
  }(chf)
  cht := make(chan diskformat.CatalogWithSpec)
  go func(ch chan diskformat.CatalogWithSpec) {
    toCat, err := diskformat.GetCatalogWithSpec(transition.toCatspec)
    if err != nil {
      log.Fatalln("Could not fetch", toCat, "error:", err)
    }
    ch <- toCat
  }(cht)
  return <-chf, <-cht
}

func Integrate(transition CatalogSpecTransition) {
  // We have the catalogs, now we need to generate commands to integrate the
  // catalogs. One of the questions is how do we map replacements from one
  // catalog into the other; and how do we group these catalogs.
  fromCat, toCat := fetchTwo(transition)
  log.Println("Integration from", fromCat.Spec, "to", toCat.Spec)
  // Integrations are done by bundle; a group of packages. (or maybe not?)
  // Considering deletions as well as additions of packages.
  // Package addition and removal times are not taken from the catalog, but
  // from the times when we saw packages appear and/or disappear.
  // How to test these rules? What should be the output of this function?
}

func main() {
  flag.Parse()
  log.Println("Program start")

  all_catspecs, err := diskformat.GetCatalogSpecsFromDatabase()
  if err != nil {
    log.Fatalln("Could not get the catalog spec list")
  }
  from_catspecs := diskformat.FilterCatspecs(all_catspecs, from_catrel_flag)
  to_catspecs := diskformat.FilterCatspecs(all_catspecs, to_catrel_flag)
  transitions := matchCatspecs(from_catspecs, to_catspecs)
  for _, transition := range transitions {
    Integrate(transition)
  }
}

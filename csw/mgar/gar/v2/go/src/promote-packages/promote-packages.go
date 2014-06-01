// Command promote-packages analyzes the state of the catalogs, and promotes
// packages from one catalog (unstable) to another one, based on a set of
// rules.

package main

import (
  // "bufio"
  "fmt"
  "flag"
  "log"
  // "os"
  "opencsw/diskformat"
  "opencsw/mantis"
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

type CatalogWithSpecTransition struct {
  fromCat diskformat.CatalogExtra
  toCat diskformat.CatalogExtra
}

type IntegrationResult struct {
  noidea string
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
  log.Println("Example package:", fromCat.PkgsExtra[0])
  log.Println("Example package:", toCat.PkgsExtra[0])

  // Mantis:
  // http://www.opencsw.org/buglist/json
}


func transitions() []CatalogSpecTransition {
  all_catspecs, err := diskformat.GetCatalogSpecsFromDatabase()
  if err != nil {
    log.Fatalln("Could not get the catalog spec list")
  }
  from_catspecs := diskformat.FilterCatspecs(all_catspecs, from_catrel_flag)
  to_catspecs := diskformat.FilterCatspecs(all_catspecs, to_catrel_flag)
  return matchCatspecs(from_catspecs, to_catspecs)
}

// The idea of creating a pipeline in this fashion is that a function call
// generates a channel and closes it after all data are written to it.
// The closure inside this function looks weird, but its scope is the same as
// the scope of the function, so it quickly becomes natural to read, and keeps
// related pieces of code together.

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

// Continue from here: write the 3rd stage which just prints the results.
func pipeStage3(in <-chan CatalogWithSpecTransition) <-chan IntegrationResult {
  out := make(chan IntegrationResult)
  go func() {
    for t := range in {
      msg := fmt.Sprintf("Processing our fetched data: %+v -> %+v",
                         t.fromCat.Spec, t.toCat.Spec)
      out <-IntegrationResult{msg}
    }
    close(out)
  }()
  return out
}

func mantisChan() <-chan []mantis.Bug {
  mch := make(chan []mantis.Bug)
  go func(ch chan []mantis.Bug) {
    log.Println("Fetching bugs from mantis")
    bugs, err := mantis.FetchBugs()
    if err != nil {
      log.Fatalln("Fetching bugs failed.")
    }
    log.Println("Fetched", len(bugs), "bugs from Mantis")
    ch <-bugs
    close(ch)
  }(mch)
  return mch
}

func main() {
  flag.Parse()
  log.Println("Program start")

  mch := mantisChan()
  tch := pipeStage1()
  cch := pipeStage2(tch)
  rch := pipeStage3(cch)

  for r := range rch {
    log.Println("Result:", r)
  }
  <-mch
}

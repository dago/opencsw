// Command gen-catalog-index genereates a catalog index file as described on
// http://www.opencsw.org/manual/for-maintainers/catalog-format.html -- the
// same code is used in the larger catalog generation program. This standalone
// utility is used to generate on-disk catalogs for other purposes like
// catalog checking.
package main

import (
  "bufio"
  "flag"
  "log"
  "os"
  "opencsw/diskformat"
)

// Command line flags
var catrel_flag string
var arch_flag string
var osrel_flag string
var out_file string

func init() {
  flag.StringVar(&out_file, "output", "catalog",
                 "The name of the file to generate.")
  flag.StringVar(&catrel_flag, "catalog-release", "unstable",
                 "e.g. unstable, bratislava, kiel, dublin")
  flag.StringVar(&osrel_flag, "os-release", "SunOS5.10",
                 "e.g. SunOS5.10")
  flag.StringVar(&arch_flag, "arch", "sparc",
                 "{ sparc | i386 }")
  flag.StringVar(&diskformat.PkgdbUrl, "pkgdb-url",
                 "http://buildfarm.opencsw.org/pkgdb/rest",
                 "Web address of the pkgdb app.")
}

func main() {
  flag.Parse()
  spec := diskformat.CatalogSpec{catrel_flag, arch_flag, osrel_flag}
  cws, err := diskformat.GetCatalogWithSpec(spec)
  if err != nil {
    log.Fatalln("Could not fetch", spec, ":", err)
  }

  catalog_fd, err := os.Create(out_file)
  if err != nil {
    log.Fatalln("Could not open the output file for writing:", err)
  }
  defer catalog_fd.Close()
  catbuf := bufio.NewWriter(catalog_fd)
  defer catbuf.Flush()

  log.Println("Writing", spec, "to", out_file)
  if err = diskformat.WriteCatalogIndex(catbuf, cws); err != nil {
    log.Fatalln("Error while writing:", err)
  } else {
    log.Println("Catalog index written successfully")
  }
}

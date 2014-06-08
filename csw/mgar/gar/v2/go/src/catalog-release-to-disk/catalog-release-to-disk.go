// Command catalog-release to disk obtains catalog contents via the OpenCSW
// REST interface on the buildfarm, analyzes the state state of the
// filesystem, and performs the necessary operations to bring the catalog on
// disk to the state defined in the database.
//
// Building this program: See README in the go/ directory.
//
// As of 2014-03-16, this program is not packaged, but instead simply compiled
// and put in place.
package main

import (
  "flag"
  "opencsw/diskformat"
)

// Command line flags
var catrel_flag string
var catalog_root_flag string
func init() {
  flag.StringVar(&catrel_flag, "catalog-release", "unstable",
                 "e.g. unstable, bratislava, kiel, dublin")
  flag.StringVar(&catalog_root_flag, "catalog-root",
                 "/export/mirror/opencsw",
                 "Directory where all the catalogs live, and allpkgs is")
}

func main() {
  flag.Parse()
  diskformat.GenerateCatalogRelease(catrel_flag, catalog_root_flag)
}

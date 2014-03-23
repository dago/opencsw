package diskformat

import (
  "testing"
  "encoding/json"
)

const small_cat = `
[
    {
        "basename": "common-1.5,REV=2010.12.11-SunOS5.8-sparc-CSW.pkg",
        "catalogname": "common",
        "category": "none",
        "deps": "none",
        "desc": "common - common files and dirs for CSW packages",
        "i_deps": "none",
        "md5_sum": "f83ab71194e67e04d1eee5d8db094011",
        "pkgname": "CSWcommon",
        "size": 23040,
        "version": "1.5,REV=2010.12.11"
    },
    {
        "basename": "dash-0.5.7,REV=2012.04.17-SunOS5.9-sparc-CSW.pkg.gz",
        "catalogname": "dash",
        "category": "none",
        "deps": "CSWcommon",
        "desc": "dash - POSIX-compliant implementation of /bin/sh that aims to be as small as possible",
        "i_deps": "none",
        "md5_sum": "d1efb8957f35591ba3cf49fba2f41d21",
        "pkgname": "CSWdash",
        "size": 75821,
        "version": "0.5.7,REV=2012.04.17"
    }
]`

func TestVanilla(t *testing.T) {
  c := Catalog{}
  err := json.Unmarshal([]byte(small_cat), &c)
  if err != nil { t.Error(err); t.FailNow() }
  spec := CatalogSpec{"fake", "sparc", "5.10"}
  cws := CatalogWithSpec{spec, c}
  if !cws.IsSane() { t.Error("This catalog should be OK") }
}

func TestMissing(t *testing.T) {
  c := Catalog{}
  err := json.Unmarshal([]byte(small_cat), &c)
  c = c[1:]
  spec := CatalogSpec{"fake", "sparc", "5.10"}
  cws := CatalogWithSpec{spec, c}
  // t.Log("c:", c)
  if err != nil { t.Error(err); t.FailNow() }
  if cws.IsSane() { t.Error("This catalog is missing a dependency") }
}

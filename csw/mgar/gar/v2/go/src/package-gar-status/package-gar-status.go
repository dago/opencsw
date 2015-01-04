// We're only including fields that are relevant now. Fields that are present in
// JSON data but are not in structs, are ignored by the unmarshaller.

package main

import (
  "fmt"
  "flag"
  "net/http"
  "encoding/json"
  "log"
  "opencsw/diskformat"
  "time"
  "text/template"
  "os"
)

var outputFile string

const tmpl = `GAR package status report
Generated on {{ .Date }}

{{ range .Pkgs }}
{{ .Pkg.Catalogname }} is {{ if .InGar }} in GAR {{ else }} NOT in GAR {{ end }}{{ end }}
`

func init() {
  flag.StringVar(&outputFile, "output-file", "gar-package-status.txt",
                 "Where to write output.")
}

type BasicStatsType struct {
  Catalogname string        `json:"catalogname"`
  Md5_sum diskformat.Md5Sum `json:"md5_sum"`
}

type PackageStats struct {
  BadPaths map[string][]string `json:"bad_paths"`
  BasicStats BasicStatsType    `json:"basic_stats"`
  Mtime string                 `json:"mtime"` // decode as time.Time?
  Binaries []string            `json:"binaries"`
  Pkginfo map[string]string    `json:"pkginfo"`
}

func FindOutIfPackageIsInGar(md5 diskformat.Md5Sum) (bool, error) {
  url := fmt.Sprintf("%s/srv4/%s/pkg-stats/", diskformat.PkgdbUrl, md5)
  log.Println("Fetching", url)
  resp, err := http.Get(url)
  if err != nil {
    return false, err
  }
  defer resp.Body.Close()

  var stats PackageStats
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&stats); err != nil {
    log.Println("Failed to decode JSON from", url, ":", err)
    return false, err
  }
  _, inGar := stats.Pkginfo["OPENCSW_REPOSITORY"]
  return inGar, nil
}

type PackageWithExtraData struct {
  Pkg diskformat.Package
  InGar bool
}

type TemplateData struct {
  Pkgs []PackageWithExtraData
  Date time.Time
}

func main() {
  log.Println("Program start")
  spec := diskformat.CatalogSpec {
    "unstable",
    "i386",
    "SunOS5.10",
  }
  log.Println("spec:", spec)

  inGarByPkgname := make(map[string]PackageWithExtraData)
  if cws, err := diskformat.GetCatalogWithSpec(spec); err != nil {
    log.Fatalln("Error unmarshalling JSON data:", err)
  } else {
    for _, pkg := range cws.Pkgs {
      log.Println("Processing", fmt.Sprintf("%+v", pkg))
      if inGar, err := FindOutIfPackageIsInGar(pkg.Md5_sum); err != nil {
        log.Fatalln(pkg.Md5_sum, "boo", err)
      } else {
        log.Println("Result: ", pkg.Md5_sum, "is", inGar)
        var pwed PackageWithExtraData
        pwed.Pkg = pkg
        pwed.InGar = inGar
        inGarByPkgname[pkg.Catalogname] = pwed
      }
    }
  }
  f, err := os.Create(outputFile)
  if err != nil {
    panic(err)
  }
  defer f.Close()
  var td TemplateData
  td.Pkgs = make([]PackageWithExtraData, 0)
  for _, pkg := range inGarByPkgname {
    td.Pkgs = append(td.Pkgs, pkg)
  }
  td.Date = time.Now()
  t := template.Must(template.New("tmpl").Parse(tmpl))
  if err := t.Execute(f, td); err != nil {
    log.Fatal(err)
  }
}

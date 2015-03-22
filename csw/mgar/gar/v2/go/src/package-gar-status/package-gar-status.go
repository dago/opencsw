// We're only including fields that are relevant now. Fields that are present in
// JSON data but are not in structs, are ignored by the unmarshaller.
//
// The script fetches every package every time. It could store a local cache
// to speed up execution.

package main

import (
  "encoding/json"
  "flag"
  "fmt"
  "log"
  "net/http"
  "opencsw/diskformat"
  "os"
  "sort"
  "text/template"
  "time"
)

var outputFile string
var testingRun bool

const markdownTmpl = `# GAR package status report

Generated on {{ .Date }} by v2/go/src/package-gar-status/package-gar-status.go

## Packages not in GAR
{{ range .Pkgs }}{{ if .InGar }}{{ else }}
* [{{ .Pkg.Catalogname }}](http://www.opencsw.org/packages/{{ .Pkg.Catalogname }})
  --
  [{{ .Pkg.Md5_sum }}](http://buildfarm.opencsw.org/pkgdb/srv4/{{ .Pkg.Md5_sum }}/){{ end }}{{ end }}
`

func init() {
  flag.StringVar(&outputFile, "output-file", "gar-package-status.md",
                 "Where to write output.")
  flag.BoolVar(&testingRun, "testing", false,
               "Run for testing, only a few packages")
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

func GetPkgstats(md5 diskformat.Md5Sum) (PackageStats, error) {
  url := fmt.Sprintf("%s/srv4/%s/pkg-stats/", diskformat.PkgdbUrl, md5)
  log.Println("Fetching", url)
  var resp *http.Response
  resp, err := http.Get(url)
  if err != nil {
    log.Println("HTTP GET failed: ", err, " but we'll try again.")
    resp, err = http.Get(url)
    if err != nil {
      return PackageStats{}, err
    }
  }
  defer resp.Body.Close()

  var stats PackageStats
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&stats); err != nil {
    log.Println("Failed to decode JSON from", url, ":", err)
    return PackageStats{}, err
  }
  return stats, nil
}

type PackageWithExtraData struct {
  Pkg diskformat.Package
  InGar bool
}

type ByCatalogname []PackageWithExtraData

type TemplateData struct {
  Pkgs ByCatalogname
  Date time.Time
}

func (a ByCatalogname) Len() int { return len(a) }
func (a ByCatalogname) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a ByCatalogname) Less(i, j int) bool {
  return a[i].Pkg.Catalogname < a[j].Pkg.Catalogname
}

func main() {
  log.Println("Program start")
  // Without flag.Parse(), -h doesn't work.
  flag.Parse()

  // Parse the template early.
  t := template.Must(template.New("tmpl").Parse(markdownTmpl))

  spec := diskformat.CatalogSpec {
    "unstable",
    "i386",
    "SunOS5.10",
  }
  log.Println("Looking at catalog ", spec, " only.")

  inGarByPkgname := make(map[string]PackageWithExtraData)
  if cws, err := diskformat.GetCatalogWithSpec(spec); err != nil {
    log.Fatalln("Error unmarshalling JSON data:", err)
  } else {
    var count = 0
    for _, pkg := range cws.Pkgs {
      log.Println("Processing", fmt.Sprintf("%+v", pkg))
      stats, err := GetPkgstats(pkg.Md5_sum)
      if err != nil {
        log.Fatalln("Failed to fetch: ", pkg.Md5_sum, " because ", err)
      }
      _, inGar := stats.Pkginfo["OPENCSW_REPOSITORY"]
      log.Println("Result: ", pkg.Md5_sum, "is", inGar)
      var pwed PackageWithExtraData
      pwed.Pkg = pkg
      pwed.InGar = inGar
      inGarByPkgname[pkg.Catalogname] = pwed

      count += 1
      if testingRun && count > 10 {
        break
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
  sort.Sort(ByCatalogname(td.Pkgs))
  td.Date = time.Now()
  if err := t.Execute(f, td); err != nil {
    log.Fatal(err)
  }
  log.Println("Finished, potentially successfully.")
}

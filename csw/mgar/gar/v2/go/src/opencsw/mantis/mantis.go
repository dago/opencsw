// Package mantis provides Mantis related code, allowing e.g. to look up
// package bugs.
package mantis

import (
  "encoding/json"
  "fmt"
  "log"
  "net/http"
)

// Matches the data structure in http://www.opencsw.org/buglist/json
// Maybe this should go into a separate package, like opencsw/mantis.
type Bug struct {
   AssignedTo string         `json:"bug_assigned_to"`
   AssignedToFullname string `json:"bug_assigned_to_fullname"`
   Id string                 `json:"bug_id"`
   LastUpdated string        `json:"bug_last_updated"`
   Catalogname string        `json:"bug_pkg_catalogname"`
   SeverityId string         `json:"bug_severity"`
   Severity string           `json:"bug_severity_name"`
   StatusId string           `json:"bug_status"`
   Status string             `json:"bug_status_name"`
   Summary string            `json:"bug_summary"`
   MaintainerFullname string `json:"maintainer_fullname"`
   Maintainer string         `json:"maintainer_name"`
   MaintainerStatus string   `json:"maintainer_status"`
}

func (b Bug) Url() string {
  return fmt.Sprintf("https://www.opencsw.org/mantis/view.php?id=%s", b.Id)
}

// Fetches all bugs from Mantis.
func FetchBugs() ([]Bug, error) {
  url := "http://www.opencsw.org/buglist/json"
  resp, err := http.Get(url)
  if err != nil {
    return nil, err
  }
  defer resp.Body.Close()

  bugs := make([]Bug, 0)
  dec := json.NewDecoder(resp.Body)
  if err := dec.Decode(&bugs); err != nil {
    return nil, err
  }
  log.Println("Fetched", len(bugs), "bugs from", url)
  return bugs, nil
}

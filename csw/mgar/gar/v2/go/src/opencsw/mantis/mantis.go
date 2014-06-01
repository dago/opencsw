// Package mantis provides Mantis related code, allowing e.g. to look up
// package bugs.
package mantis

import (
  "net/http"
  "encoding/json"
  "log"

)

// Matches the data structure in http://www.opencsw.org/buglist/json
// Maybe this should go into a separate package, like opencsw/mantis.
type Bug struct {
   bug_assigned_to string          `json:"bug_assigned_to"`
   bug_assigned_to_fullname string `json:"bug_assigned_to_fullname"`
   bug_id string                   `json:"bug_id"`
   bug_last_updated string         `json:"bug_last_updated"`
   bug_pkg_catalogname string      `json:"bug_pkg_catalogname"`
   bug_severity string             `json:"bug_severity"`
   bug_severity_name string        `json:"bug_severity_name"`
   bug_status string               `json:"bug_status"`
   bug_status_name string          `json:"bug_status_name"`
   bug_summary string              `json:"bug_summary"`
   maintainer_fullname string      `json:"maintainer_fullname"`
   maintainer_name string          `json:"maintainer_name"`
   maintainer_status string        `json:"maintainer_status"`
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

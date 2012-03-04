#!/usr/bin/env python2.6

"""Polls a designated catalog tree, and sends notifications about
package updates."""

import optparse
import catalog
import common_constants
from Cheetah import Template
import urllib2
import logging
import configuration
import pprint
import cPickle
import json
import os.path
import smtplib
from email.mime.text import MIMEText
import rest

REPORT_TMPL = u"""Catalog update report for $email
Catalog URL: $url
#import re
#def CatalogList($catalogs)
#set $by_catrel = {}
#set $unused = [by_catrel.setdefault(x[0], []).append(x[1:]) for x in $catalogs]
#for catrel in $by_catrel:
  - $catrel: #
#set $by_arch = {}
#set $unused = [by_arch.setdefault(x[0], []).append(x[1:]) for x in $by_catrel[$catrel]]
#set $first = True
#for arch in $by_arch:
#if not $first
, #
#else
#set $first = False
#end if
$arch (#
#echo ", ".join([re.sub(r'^.*OS', '', x[0]) for x in $by_arch[$arch]]) + ")"
#end for

#end for
#end def
#if "new_pkgs" in $pkg_data

New packages:
#for basename in $pkg_data["new_pkgs"]
* $basename
  In catalogs:
#set $catalogs = $sorted($pkg_data["new_pkgs"][basename]["catalogs"])
$CatalogList($catalogs)
#end for
#end if
#if "removed_pkgs" in $pkg_data

Removed packages:
#for basename in $pkg_data["removed_pkgs"]
* $basename
  From catalogs:
#set $catalogs = $sorted($pkg_data["removed_pkgs"][basename]["catalogs"])
$CatalogList($catalogs)
#end for
#end if
#if "upgraded_pkg" in $pkg_data

Version change (probably upgrade):
#for basename in $pkg_data["upgraded_pkg"]
#for from_basename in $pkg_data["upgraded_pkg"][basename]["from_pkg"]
- $pkg_data["upgraded_pkg"][basename]["from_pkg"][from_basename]["file_basename"]
#end for
+ $pkg_data["upgraded_pkg"][basename]["to_pkg"]["file_basename"]
  In catalogs:
#set $catalogs = $sorted($pkg_data["upgraded_pkg"][basename]["catalogs"])
$CatalogList($catalogs)
#end for
#end if
#if "lost_pkg" in $pkg_data

You no longer maintain packages:
#for basename in $pkg_data["lost_pkg"]
#for from_basename in $pkg_data["lost_pkg"][basename]["from_pkg"]
- $pkg_data["lost_pkg"][basename]["from_pkg"][from_basename]["file_basename"]
#end for
  In catalogs:
#set $catalogs = $sorted($pkg_data["lost_pkg"][basename]["catalogs"])
$CatalogList($catalogs)
#end for
#end if
#if "got_pkg" in $pkg_data

You took over packages:
#for basename in $pkg_data["got_pkg"]
* $basename
  In catalogs:
#set $catalogs = $sorted($pkg_data["got_pkg"][basename]["catalogs"])
$CatalogList($catalogs)
#end for
#end if
"""

class NotificationFormatter(object):

  def _GetPkgsByMaintainer(self, catalogs, rest_client):
    c = catalog.CatalogComparator()
    pkgs_by_maintainer = {}
    for catrel, arch, osrel, cat_a, cat_b in catalogs:
      catalog_key = (catrel, arch, osrel)
      new_pkgs, removed_pkgs, updated_pkgs = c.GetCatalogDiff(cat_a, cat_b)
      labels_and_lists = (
          ("new_pkgs", new_pkgs),
          ("removed_pkgs", removed_pkgs),
      )
      for label, pkg_list in labels_and_lists:
        for pkg in pkg_list:
          maintainer = rest_client.GetMaintainerByMd5(pkg["md5sum"])
          maintainer_email = maintainer["maintainer_email"]
          pkgs_by_maintainer.setdefault(maintainer_email, {})
          pkgs_by_maintainer[maintainer_email].setdefault(label, {})
          labeled = pkgs_by_maintainer[maintainer_email][label]
          basename = pkg["file_basename"]
          labeled.setdefault(basename, {
            "pkg": pkg,
            "catalogs": [],
          })
          labeled[basename]["catalogs"].append(catalog_key)
      for d in updated_pkgs:
        from_pkg = d["from"]
        to_pkg = d["to"]
        maintainer_from = rest_client.GetMaintainerByMd5(from_pkg["md5sum"])
        maintainer_to = rest_client.GetMaintainerByMd5(to_pkg["md5sum"])
        from_email = maintainer_from["maintainer_email"]
        to_email = maintainer_to["maintainer_email"]
        if from_email == to_email:
          # A normal upgrade, no takeover
          label = "upgraded_pkg"
          self._StorePkgUpdate(catalog_key,
              label, pkgs_by_maintainer, from_email, from_pkg, to_pkg)
        else:
          # Package takeover
          self._StorePkgUpdate(catalog_key,
              "lost_pkg", pkgs_by_maintainer, from_email, from_pkg, to_pkg)
          self._StorePkgUpdate(catalog_key,
              "got_pkg", pkgs_by_maintainer, to_email, from_pkg, to_pkg)
    return pkgs_by_maintainer

  def _StorePkgUpdate(self,
      catalog_key,
      label, pkgs_by_maintainer, email, from_pkg, to_pkg):
    pkgs_by_maintainer.setdefault(email, {})
    pkgs_by_maintainer[email].setdefault(label, {})
    labeled = pkgs_by_maintainer[email][label]
    basename = to_pkg["file_basename"]
    labeled.setdefault(basename, {
      "to_pkg": to_pkg,
      "from_pkg": {},
      "catalogs": [],
    })
    labeled[basename]["from_pkg"][from_pkg["file_basename"]] = from_pkg
    labeled[basename]["catalogs"].append(catalog_key)

  def _RenderForMaintainer(self, pkg_data, email, url):
    namespace = {
        "pkg_data": pkg_data,
        "email": email,
        "url": url}
    t = Template.Template(REPORT_TMPL, searchList=[namespace])
    return unicode(t)

  def FormatNotifications(self, url, catalogs, rest_client):
    """Formats a notification from a series of catalogs.

    Args:
      url: Base URL for catalogs
      catalogs: A list of triplets (catrel, arch, osrel, cat_a, cat_b)
      rest_client: An interface to the outside world
    """
    pkgs_by_maintainer = self._GetPkgsByMaintainer(catalogs, rest_client)
    rendered_notifications = {}
    for email in pkgs_by_maintainer:
      rendered_notifications[email] = self._RenderForMaintainer(
          pkgs_by_maintainer[email], email, url)
    return rendered_notifications


class CatalogIndexDownloader(object):

  def GetCatalogsByTriad(self, cat_tree_url):
    catalogs_by_triad = {}
    for catrel in common_constants.DEFAULT_CATALOG_RELEASES:
      for arch in common_constants.PHYSICAL_ARCHITECTURES:
        for osrel in common_constants.OS_RELS:
          short_osrel = osrel.replace("SunOS", "")
          catalog_file_url = (
              "%s%s/%s/%s/catalog"
              % (cat_tree_url, catrel, arch, short_osrel))
          logging.info("Opening %s", repr(catalog_file_url))
          try:
            f = urllib2.urlopen(catalog_file_url)
            key = (catrel, arch, osrel)
            catalog_instance = catalog.OpencswCatalog(f)
            catalogs_by_triad[key] = catalog_instance.GetDataByCatalogname()
          except urllib2.URLError, e:
            logging.warning(e)
    return catalogs_by_triad


def main():
  DEFAULT_URL = "http://mirror.opencsw.org/opencsw/"
  DEFAULT_URL = "http://ivy.home.blizinski.pl/~maciej/opencsw/"
  parser = optparse.OptionParser()
  parser.add_option("-u", "--url",
      dest="url", help="Base URL of OpenCSW catalog",
      default=DEFAULT_URL)
  parser.add_option("-d", "--debug",
      dest="debug", action="store_true",
      default=False)
  parser.add_option("-s", "--send-notifications",
      dest="send_notifications", action="store_true",
      default=False)
  parser.add_option("-p", "--pickle-file",
      dest="pickle_file", help="Pickle file",
      default="/tmp/opencsw-notifier-data/example.pickle")
  parser.add_option("-w", "--whitelist",
      dest="whitelist",
      help="E-mail address whitelist, comma separated",
      default=None)
  options, args = parser.parse_args()
  logging.basicConfig(level=logging.DEBUG)
  # Getting catalogs
  cat_tree_url = options.url
  downloader = CatalogIndexDownloader()
  catalogs_by_triad = downloader.GetCatalogsByTriad(cat_tree_url)
  pickle_path = options.pickle_file
  previous_catalogs_by_triad = None
  try:
    with open(pickle_path, "rb") as fd:
      previous_catalogs_by_triad = cPickle.load(fd)
  except (IOError, EOFError), e:
    logging.warning(e)
    previous_catalogs_by_triad = {}
  # Merge the two data structures here
  catalogs = []
  for key in catalogs_by_triad:
    if key in previous_catalogs_by_triad:
      catalogs.append(
        # ("fossil", "amd65", "SolarOS5.12", cat_a, cat_b),
        key + (previous_catalogs_by_triad[key], catalogs_by_triad[key])
      )
    else:
      logging.debug("%s not found in previous_catalogs_by_triad", key)
  formatter = NotificationFormatter()
  rest_client = rest.RestClient()
  notifications = formatter.FormatNotifications(
      cat_tree_url, catalogs, rest_client)
  whitelist = frozenset()
  if options.whitelist:
    whitelist = frozenset(options.whitelist.split(","))
    logging.debug("Email whitelist: %s", whitelist)
  for email in notifications:
    if options.send_notifications:
      logging.debug("email: %s", repr(email))
      if whitelist and email not in whitelist:
        continue
      logging.debug("Sending.")
      msg = MIMEText(notifications[email])
      msg["Subject"] = "OpenCSW catalog update report"
      from_address = "Catalog update notifier <noreply@opencsw.org>"
      msg['From'] = from_address
      msg['To'] = email
      s = smtplib.SMTP('mail.opencsw.org')
      try:
        s.sendmail(from_address, [email], msg.as_string())
      except smtplib.SMTPRecipientsRefused, e:
        logging.warning(
            "Sending email to %s failed, recipient refused.",
            repr(email))
      s.quit()
      logging.debug("E-mail sent.")
    else:
      print notifications[email]
      print "* * *"
  with open(pickle_path, "wb") as fd:
    cPickle.dump(catalogs_by_triad, fd)


if __name__ == '__main__':
  main()

#!/opt/csw/bin/python2.6
# coding=utf-8
#
# $Id$

import optparse
import models as m
import sqlobject
import cPickle
import logging
import code
import os
import os.path
import re
import socket
import sys
import package_checks
from Cheetah.Template import Template

USAGE = """usage: %prog show errors <md5sum> [ ... ]
       %prog show pkg <pkgname> [ ... ]
       %prog gen-html <md5sum> [ ... ]
       """
SHOW_PKG_TMPL = """catalogname:    $catalogname
pkgname:        $pkginst.pkgname
basename:       $basename
mtime:          $mtime
md5_sum:        $md5_sum
arch:           $arch.name
os_rel:         $os_rel.short_name
maintainer:     $maintainer.email
latest:         $latest
version_string: $version_string
rev:            $rev
stats_version:  $stats_version
"""

DEFAULT_TEMPLATE_FILENAME = "../lib/python/pkg-review-template.html"


class HtmlGenerator(object):

  def __init__(self, md5_sums, template=None):
    self.md5_sums = md5_sums
    self.template = template

  def GetErrorTagsResult(self, srv4):
    res = m.CheckpkgErrorTag.select(
        m.CheckpkgErrorTag.q.srv4_file==srv4)
    return res

  def GetOverrideResult(self, srv4):
    res = m.CheckpkgOverride.select(
        m.CheckpkgOverride.q.srv4_file==srv4)
    return res

  def GenerateHtml(self):
    pkgstats = []
    # Add error tags
    for md5_sum in self.md5_sums:
      srv4 = GetPkg(md5_sum)
      data = cPickle.loads(str(srv4.data))
      if "OPENCSW_REPOSITORY" in data["pkginfo"]:
        build_src = data["pkginfo"]["OPENCSW_REPOSITORY"]
        build_src_url_svn = re.sub(r'([^@]*).*', r'\1/Makefile', build_src)
        build_src_url_trac = re.sub(
            r'https://gar.svn.(sf|sourceforge).net/svnroot/gar/([^@]+)@(.*)',
            r'http://sourceforge.net/apps/trac/gar/browser/\2/Makefile?rev=\3',
            build_src)
      else:
        build_src = None
        build_src_url_svn = None
        build_src_url_trac = None
      data["build_src"] = build_src
      data["build_src_url_svn"] = build_src_url_svn
      data["build_src_url_trac"] = build_src_url_trac
      data["error_tags"] = list(self.GetErrorTagsResult(srv4))
      data["overrides"] = list(self.GetOverrideResult(srv4))
      pkgstats.append(data)
    # This assumes the program is run as "bin/pkgdb", and not "lib/python/pkgdb.py".
    if not self.template:
      tmpl_filename = os.path.join(os.path.split(__file__)[0],
                                   DEFAULT_TEMPLATE_FILENAME)
    else:
      tmpl_filename = self.template
    tmpl_str = open(tmpl_filename, "r").read()
    t = Template(tmpl_str, searchList=[{
      "pkgstats": pkgstats,
      "hachoir_machines": package_checks.HACHOIR_MACHINES,
      }])
    return unicode(t)


def GetPkg(some_id):
  logging.debug("Selecting from db: %s", repr(some_id))
  res = m.Srv4FileStats.select(
      sqlobject.OR(
        m.Srv4FileStats.q.md5_sum==some_id,
        m.Srv4FileStats.q.catalogname==some_id))
  try:
    srv4 = res.getOne()
  except sqlobject.main.SQLObjectIntegrityError, e:
    logging.warning(e)
    for row in res:
      print "- %s %s %s" % (row.md5_sum, row.version_string, row.mtime)
    raise
  logging.debug("Got: %s", srv4)
  return srv4

def main():
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-t", "--pkg-review-template", dest="pkg_review_template",
                    help="A Cheetah template used for package review reports.")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  command = args[0]
  args = args[1:]
  if command == 'show':
    subcommand = args[0]
    args = args[1:]
  else:
    subcommand = None

  db_path = os.path.join(
      os.environ["HOME"],
      ".checkpkg",
      "checkpkg-db-%s" % socket.getfqdn())
  sqo_conn = sqlobject.connectionForURI('sqlite:%s' % db_path)
  sqlobject.sqlhub.processConnection = sqo_conn

  md5_sums = args

  if (command, subcommand) == ('show', 'errors'):
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      res = m.CheckpkgErrorTag.select(m.CheckpkgErrorTag.q.srv4_file==srv4)
      for row in res:
        print row.pkgname, row.tag_name, row.tag_info
  if (command, subcommand) == ('show', 'overrides'):
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      res = m.CheckpkgOverride.select(m.CheckpkgOverride.q.srv4_file==srv4)
      for row in res:
        print row.pkgname, row.tag_name, row.tag_info
  if (command, subcommand) == ('show', 'pkg'):
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      t = Template(SHOW_PKG_TMPL, searchList=[srv4])
      sys.stdout.write(unicode(t))
  if command == 'gen-html':
    g = HtmlGenerator(md5_sums, options.pkg_review_template)
    sys.stdout.write(g.GenerateHtml())


if __name__ == '__main__':
  main()

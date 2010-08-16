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
import socket
import sys
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

REVIEW_REQ_TMPL = """<html>
#import pprint
<head>
<title>
#for pkg in $pkgstats
$pkg.pkginfo.PKG
#end for
</title>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<style type="text/css">
body { font-family: sans-serif; }
p, td, li { font-size: 11px; }
h1 { font-size: 16px; }
h2 { font-size: 15px; }
h3 { font-size: 14px; }
h4 { font-size: 13px; }
pre { background-color: #EEE; }
ul.code {
  list-style: none;
  padding: 0px;
  margin: 0px;
}
ul.code li {
  font-family: monospace;
  background-color: #EEE;
}
</style>
</head>
<body>
#for pkg in $pkgstats
  <h1>$pkg.basic_stats.pkg_basename</h1>
  <h2>Basic stats</h2>
  <table>
#for key in ('md5_sum', 'pkgname', 'stats_version', 'pkg_basename', 'catalogname')
  <tr>
  <td>
  $key
  </td>
  <td>
  <code>$pkg.basic_stats[$key]</code>
  </td>
  </tr>
#end for
  </table>
  <p>parsed basename</p>
  <pre>
$pprint.pformat($pkg.basic_stats.parsed_basename)
  </pre>
  <h2>pkginfo</h2>
  <table>
#for key, val in $pkg.pkginfo.iteritems
  <tr>
  <td
  style="border: 1px solid gray;"
  >$key</td>
  <td style="font-family: monospace; border: 1px solid gray;"
  >$val</td>
  </tr>
#end for
  </table>
#if $pkg.binaries_dump_info
  <h2>binaries_dump_info</h2>
  <ul>
#for bin in $pkg["binaries_dump_info"]
	<li>
	<strong>$bin.path</strong>
## ['base_name', 'RUNPATH RPATH the same', 'runpath', 'RPATH set', 'needed sonames', 'path', 'RUNPATH set']
	<ul>
  <li> runpath: <code>$bin.runpath</code> </li>
	<li> needed sonames: <code>$bin["needed sonames"]</code> </li>
  </ul>
	</li>
#end for
	</ul>
#end if
#if $pkg.depends
  <h2>depends</h2>
  <ul>
#for depend_pkg, depend_desc in $pkg.depends
  <li>
  $depend_desc
  </li>
#end for
  </ul>
#end if
#if $pkg.files_metadata
  <h2>files metadata</h2>
  <table>
#for md in $pkg.files_metadata
  <tr>
  <td> $md.path </td>
  <td> $md.mime_type </td>
  </tr>
#end for
  </table>
#end if
#if $pkg.isalist
  <h2>isalist</h2>
  <p>$pkg.isalist</p>
#end if
#if $pkg.mtime
  <h2>mtime</h2>
  <p>
  $pkg.mtime
  </p>
#end if
#if $pkg.overrides
  <h2>overrides</h2>
  <ul>
#for override in $pkg.overrides
	<li>
	$override.pkgname
	$override.tag_name
  $override.tag_info
	</li>
#end for
  </ul>
#end if
  <h2>pkgchk</h2>
  <p>stdout</p>
  <pre>
#for l in $pkg.pkgchk.stdout_lines
$l
#end for
  </pre>
  <p>stderr</p>
  <pre>
#for l in $pkg.pkgchk.stderr_lines
$l
#end for
  </pre>
  <h2>pkgmap</h2>
  <ul class="code">
#for entry in $pkg.pkgmap
	<li>
	$entry.line
	</li>
#end for
  </ul>
#end for
</body>
</html>
"""

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
    pkgstats = []
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      pkgstats.append(cPickle.loads(str(srv4.data)))
    t = Template(REVIEW_REQ_TMPL, searchList=[srv4, {"pkgstats": pkgstats}])
    sys.stdout.write(unicode(t))


if __name__ == '__main__':
  main()

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
p, td, th, li { font-size: 11px; }
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
ul.clean {
  list-style: none;
  padding: 0px;
  margin: 0px;
}
span.warning {
  background-color: #DDF;
}
table.framed td {
  border: 1px solid #DDD;
}
td.numeric {
  text-align: right;
}
table.gently-lined td {
  border-bottom: 1px solid #DDD;
  margin: 0px;
  padding: 2px;
}
table.gently-lined th {
  border-bottom: 2px solid black;
  margin: 0px;
  padding: 2px;
}
</style>
</head>
<body>
#for pkg in $pkgstats
  <h1>$pkg.basic_stats.pkg_basename</h1>
  <h2>Build source code</h2>
#if $pkg.build_src
  <p>
    <a href="$pkg.build_src">
      $pkg.build_src
    </a>
  </p>
#else
  <p>
    <span style="warning">
      Build source (OPENCSW_REPOSITORY) not specified in pkginfo.
    </span>
  </p>
#end if
	<p>
	  <a href="http://www.opencsw.org/packages/$pkg.basic_stats.pkgname/">
	    $pkg.basic_stats.pkgname</a>
	  on the website.
	</p>
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
  <h3>parsed basename</h3>
  <table class="framed">
  <!--

{'arch': 'i386',
 'catalogname': 'mysql51',
 'full_version_string': '5.1.49,REV=2010.08.12',
 'osrel': 'SunOS5.9',
 'revision_info': {'REV': '2010.08.12'},
 'vendortag': 'CSW',
 'version': '5.1.49',
 'version_info': {'major version': '5',
                  'minor version': '1',
                  'patchlevel': '49'}}

  mysql51-5.1.49,REV=2010.08.12-SunOS5.9-i386-CSW.pkg.gz
  -->
  <tr>
    <th>catalogname</th>
    <th>full_version_string</th>
    <th>(version)</th>
    <th>(version_info)</th>
    <th>(revision_info)</th>
    <th>osrel</th>
    <th>arch</th>
    <th>vendortag</th>
  </tr>
  <tr>
    <td>$pkg.basic_stats.parsed_basename.catalogname</td>
    <td>$pkg.basic_stats.parsed_basename.full_version_string</td>
    <td>$pkg.basic_stats.parsed_basename.version</td>
    <td>
      <ul class="clean">
#for key, val in $pkg.basic_stats.parsed_basename.version_info.iteritems
        <li>$key: $val</li>
#end for
      </ul>
    </td>
    <td>
      <ul class="clean">
#for key, val in $pkg.basic_stats.parsed_basename.revision_info.iteritems
        <li>$key: $val</li>
#end for
      </ul>
    </td>
    <td>$pkg.basic_stats.parsed_basename.osrel</td>
    <td>$pkg.basic_stats.parsed_basename.arch</td>
    <td>$pkg.basic_stats.parsed_basename.vendortag</td>
  </tr>
  </table>
  <h2>pkginfo</h2>
  <table class="gently-lined">
  <tr>
  <th>Key</th>
  <th>Value</th>
  </tr>
#for key, val in $pkg.pkginfo.iteritems
  <tr>
  <td
  >$key</td>
  <td
  ><code>$val</code></td>
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
  <li>
    base name: <code>$bin.base_name</code>
  </li>
  <li> runpath:
    <ul>
#for runpath_el in $bin.runpath
      <li>
        <code>
            $runpath_el
        </code>
      </li>
#end for
    </ul>
  <li> needed sonames:
    <ul>
#for soname in $bin["needed sonames"]
      <li>
        <code>
          <a href="http://www.opencsw.org/packagesContainingFile/?fileName=$soname&searchsubmit=1">
            $soname
          </a>
        </code>
      </li>
#end for
    </ul>
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
    <a href="http://www.opencsw.org/packages/$depend_pkg/">
      $depend_desc
    </a>
  </li>
#end for
  </ul>
#end if
#if $pkg.files_metadata
  <h2>files metadata</h2>
  <table class="gently-lined">
  <tr>
    <th>path</th>
    <th>mimetype</th>
    <th>machine name</th>
    <!--
    <th>endian</th>
    -->
  </tr>
#for md in $pkg.files_metadata
  <tr>
  <td> $md.path </td>
  <td> $md.mime_type </td>
  <td style="text-align: center;">
#if "machine_id" in $md
  $hachoir_machines[$md.machine_id].name
#else
  &nbsp;
#end if
  </td>
  <!--
  <td>
#if "endian" in $md
  $md.endian
#else
  &nbsp;
#end if
  </td>
  -->
  </tr>
#end for
  </table>
#end if
#if $pkg.isalist
  <h2>isalist</h2>
  <ul class="code">
#for isa in $pkg.isalist
	  <li>
	    $isa
	  </li>
#end for
  </ul>
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
    # Add error tags
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      data = cPickle.loads(str(srv4.data))
      if "OPENCSW_REPOSITORY" in data["pkginfo"]:
        build_src = data["pkginfo"]["OPENCSW_REPOSITORY"]
        build_src = re.sub(r"@(\d+)$", r"?rev=\1", build_src)
      else:
        build_src = None
      data["build_src"] = build_src
      pkgstats.append(data)
    t = Template(REVIEW_REQ_TMPL, searchList=[{
      "pkgstats": pkgstats,
      "hachoir_machines": package_checks.HACHOIR_MACHINES,
      }])
    sys.stdout.write(unicode(t))


if __name__ == '__main__':
  main()

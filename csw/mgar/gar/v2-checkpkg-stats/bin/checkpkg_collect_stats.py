#!/opt/csw/bin/python2.6
#
# $Id$
#
# Collects statistics about a package and saves to a directory, for later use
# by checkpkg modules.

import errno
import os
import os.path
import sys
import logging
import optparse
import yaml

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw


STATS_VERSION = 1L


class PackageStats(object):
  """Collects stats about a package and saves it.

  base-stats.yml
  binaries.yml
  """

  def __init__(self, srv4_pkg):
    self.srv4_pkg = srv4_pkg
    self.md5sum = None
    self.dir_format_pkg = None
    self.stats_path = None

  def GetMd5sum(self):
    if not self.md5sum:
    	self.md5sum = self.srv4_pkg.GetMd5sum()
    return self.md5sum

  def GetStatsPath(self, home=None):
    if not self.stats_path:
      if not home:
        home = os.environ["HOME"]
      md5sum = self.GetMd5sum()
      two_chars = md5sum[0:2]
      parts = [home, ".checkpkg", "stats", two_chars, md5sum]
      self.stats_path = os.path.join(*parts)
    return self.stats_path

  def StatsExist(self):
    """Checks if statistics of a package exist.

    Returns:
      bool
    """
    if not self.StatsDirExists():
    	return False
    # More checks can be added in the future.
    return True

  def StatsDirExists(self):
    return os.path.isdir(self.GetStatsPath())

  def GetDirFormatPkg(self):
    if not self.dir_format_pkg:
    	self.dir_format_pkg = self.srv4_pkg.GetDirFormatPkg()
    return self.dir_format_pkg

  def MakeStatsDir(self):
    """mkdir -p equivalent.

    http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
    """
    stats_path = self.GetStatsPath()
    try:
      os.makedirs(stats_path)
    except OSError, e:
      if e.errno == errno.EEXIST:
      	pass
      else:
      	raise

  def CollectStats(self):
    stats_path = self.GetStatsPath()
    self.MakeStatsDir()
    dir_pkg = self.GetDirFormatPkg()
    self.DumpObject(dir_pkg.GetParsedPkginfo(), "pkginfo")
    self.DumpObject(dir_pkg.GetPkgmap().entries, "pkgmap")
    self.DumpObject(dir_pkg.ListBinaries(), "binaries")
    self.DumpObject(dir_pkg.GetDependencies(), "depends")
    self.DumpObject(dir_pkg.GetAllFilenames(), "all_filenames")
    overrides = dir_pkg.GetOverrides()
    def OverrideToDict(override):
      d = {}
      d["pkgname"] = override.pkgname
      d["tag_name"] = override.tag_name
      d["tag_info"] = override.tag_info
      return d
    overrides_simple = [OverrideToDict(x) for x in overrides]
    self.DumpObject(overrides_simple, "overrides")
    basic_stats = {}
    basic_stats["stats_version"] = STATS_VERSION
    basic_stats["pkg_path"] = self.srv4_pkg.pkg_path
    basic_stats["pkg_basename"] = os.path.basename(self.srv4_pkg.pkg_path)
    basic_stats["parsed_basename"] = opencsw.ParsePackageFileName(basic_stats["pkg_basename"])
    basic_stats["pkgname"] = dir_pkg.pkgname
    basic_stats["catalogname"] = dir_pkg.GetCatalogname()
    self.DumpObject(basic_stats, "basic_stats")

  def DumpObject(self, obj, name):
    stats_path = self.GetStatsPath()
    out_file_name = os.path.join(self.GetStatsPath(), "%s.yml" % name)
    logging.debug("DumpObject(): writing %s", repr(out_file_name))
    f = open(out_file_name, "w")
    f.write(yaml.safe_dump(obj))
    f.close()


def main():
  debug = True
  logging.basicConfig(level=logging.DEBUG)
  parser = optparse.OptionParser()
  options, args = parser.parse_args()
  logging.basicConfig(level=logging.INFO)
  logging.info("Collecting statistics about given package files.")
  logging.debug("args: %s", args)
  packages = [opencsw.CswSrv4File(x, debug) for x in args]
  stats_list = [PackageStats(pkg) for pkg in packages]
  for pkg_stats in stats_list:
  	pkg_stats.CollectStats()

if __name__ == '__main__':
	main()

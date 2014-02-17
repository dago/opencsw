#!/opt/csw/bin/python2.6

import logging
import optparse
import pprint

from lib.python import checkpkg_lib
from lib.python import configuration
from lib.python import package_checks
from lib.python import rest

DEFAULT_INDENT = 4

class LoggingCheckInterface(object):

  def _PrettyPrint(self, obj):
    indent = DEFAULT_INDENT + 2
    return pprint.pformat(obj, indent=indent, width=120)

  def __init__(self, osrel, arch, catrel, catalog, examined_files_by_pkg):
    self._set_check_interface = checkpkg_lib.SetCheckInterface(osrel,
        arch, catrel, catalog, examined_files_by_pkg)

  def GetPathsAndPkgnamesByBasename(self, *args, **kwargs):
    ret = self._set_check_interface.GetPathsAndPkgnamesByBasename(*args,
        **kwargs)
    with open("mock-log.txt", "a") as fd:
      fd.write(' ' * DEFAULT_INDENT)
      fd.write("self.error_mgr_mock.GetPathsAndPkgnamesByBasename(%r).AndReturn(\n%s%s)\n"
               % (args[0], ' ' * (DEFAULT_INDENT + 2), self._PrettyPrint(ret)))
    return ret

  def GetPkgByPath(self, arg):
    ret = self._set_check_interface.GetPkgByPath(arg)
    with open("mock-log.txt", "a") as fd:
      fd.write(' ' * DEFAULT_INDENT)
      fd.write("self.error_mgr_mock.GetPkgByPath(%r).AndReturn(\n%s%s)\n"
               % (arg, ' ' * (DEFAULT_INDENT + 2), self._PrettyPrint(sorted(ret))))
    return ret

  def NeedFile(self, pkgname, full_path, reason):
    self._set_check_interface.NeedFile(pkgname, full_path, reason)
    with open("mock-log.txt", "a") as fd:
      fd.write(' ' * DEFAULT_INDENT)
      fd.write("self.error_mgr_mock.NeedFile(%r, %r, %r)\n"
               % (pkgname, full_path, reason))

  def ReportError(self, *args, **kwargs):
    self._set_check_interface.ReportError(*args, **kwargs)
    args_str = ""
    if args:
      args_str += ", ".join(repr(x) for x in args)
    if kwargs:
      if args:
        args_str += ", "
      args_str += ", ".join("%s=%r" % (x, kwargs[x]) for x in kwargs)
    with open("mock-log.txt", "a") as fd:
      fd.write(' ' * DEFAULT_INDENT)
      fd.write("self.error_mgr_mock.ReportError(%s)\n"
               % (args_str))


def main():
  parser = optparse.OptionParser()
  parser.add_option("--debug", dest="debug", default=False, action="store_true")
  parser.add_option("--catalog-release", dest="catrel",
                    default="unstable")
  parser.add_option("--arch", dest="arch", default="i386")
  parser.add_option("--os-release", dest="osrel", default="SunOS5.10")
  parser.add_option("--md5", dest="md5")
  parser.add_option("--check-name", dest="check_name")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  configuration.SetUpSqlobjectConnection()
  osrel = options.osrel
  catrel = options.catrel
  arch = options.arch
  md5 = options.md5
  config = configuration.GetConfig()
  rest_client = rest.RestClient(
      pkgdb_url=config.get('rest', 'pkgdb'),
      releases_url=config.get('rest', 'releases'))
  logging.info("Fetching %s", md5)
  pkgstats = rest_client.GetBlob('pkgstats', md5)
  catalog = checkpkg_lib.Catalog()
  check_function = getattr(package_checks, options.check_name)
  examined_files_by_pkg = {}
  check_interface = LoggingCheckInterface(osrel, arch, catrel, catalog, examined_files_by_pkg)
  messenger = checkpkg_lib.CheckpkgMessenger()
  pkgstats['elfdump_info'] = checkpkg_lib.LazyElfinfo(rest_client)
  check_function([pkgstats], check_interface, logger=logging, messenger=messenger)

if __name__ == '__main__':
  main()

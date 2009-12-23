# This is a checkpkg library, common for all checkpkg tests written in Python.

import optparse

class Error(Exception):
  pass

class ConfigurationError(Error):
  pass

def GetOptions():
  parser = optparse.OptionParser()
  parser.add_option("-e", dest="extractdir",
                    help="The directory into which the package has been extracted")
  parser.add_option("-p", dest="pkgname",
                    help="The pkgname, e.g. CSWfoo")
  (options, args) = parser.parse_args()
  if not options.extractdir:
    raise ConfigurationError("ERROR: -e option is missing.")
  if not options.pkgname:
    raise ConfigurationError("ERROR: -p option is missing.")
  return options, args

#!/usr/bin/env python2.6
# $Id$

import unittest
import sys
import os.path
import logging

# To add more test files, create <name>.py file and add a corresponding line
# here:
from lib.python.catalog_notifier_test      import *
from lib.python.catalog_test               import *
from lib.python.checkpkg_lib_test          import *
from lib.python.csw_upload_pkg_test        import *
from lib.python.database_test              import *
from lib.python.dependency_checks_test     import *
from lib.python.generate_catalog_file_test import *
from lib.python.integrate_catalogs_test    import *
from lib.python.ldd_emul_test              import *
from lib.python.models_test                import *
from lib.python.opencsw_test               import *
from lib.python.overrides_test             import *
from lib.python.package_checks_test        import *
from lib.python.package_stats_test         import *
from lib.python.pkgdb_test                 import *
from lib.python.pkgmap_test                import *
from lib.python.relational_util_test       import *
from lib.python.sharedlib_utils_test       import *
from lib.python.struct_util_test           import *
from lib.python.submit_to_newpkgs_test     import *
from lib.python.system_pkgmap_test         import *
from lib.python.tag_test                   import *
from lib.python.util_test                  import *

# These are very slow GAR tests, which I'm disabling for now.
# from lib.python.example_test            import *

if __name__ == '__main__':
  # Some tests output warnings, and we don't want them to be displayed
  # during unit test runs.
  logging.basicConfig(level=logging.ERROR)
  unittest.main()

# vim:set ts=2 sts=2 sw=2 expandtab:

#!/usr/bin/env python2.6
# $Id$

import unittest
import sys
import os.path
import logging
module_path = [os.path.dirname(__file__),
               "..", "lib", "python"]
sys.path.append(os.path.join(*module_path))

# To add more test files, create <name>.py file and add a corresponding line
# here:
from catalog_notifier_test   import *
from catalog_test            import *
from checkpkg_lib_test       import *
from checkpkg_test           import *
from csw_upload_pkg_test     import *
from dependency_checks_test  import *
from inspective_package_test import *
from ldd_emul_test           import *
from models_test             import *
from opencsw_test            import *
from package_checks_test     import *
from package_stats_test      import *
from package_test            import *
from pkgdb_test              import *
from pkgmap_test             import *
from sharedlib_utils_test    import *
from struct_util_test        import *
from submit_to_newpkgs_test  import *
from system_pkgmap_test      import *
from tag_test                import *

# These are very slow GAR tests, which I'm disabling for now.
# from example_test            import *
# from overrides_test          import *

if __name__ == '__main__':
  # Some tests output warnings, and we don't want them to be displayed
  # during unit test runs.
  logging.basicConfig(level=logging.ERROR)
  unittest.main()

# vim:set ts=2 sts=2 sw=2 expandtab:

# Add a dependency to CSWpython
_EXTRA_GAR_PKGS += $(PYTHON_PACKAGE)

# For the record, do not include the following line:
# _MERGE_EXCLUDE_CATEGORY += .*\.egg-info.*
#
# It breaks pysetuptools and trac.  Here's a relevant reading:
# http://fedoraproject.org/wiki/Packaging:Python#Packaging_eggs_and_setuptools_concerns

# No need to include unit tests in released packages.
_MERGE_EXCLUDE_CATEGORY += .*/$(NAME)/test
_MERGE_EXCLUDE_CATEGORY += .*/$(NAME)/test/.*

# Activate cswpycompile support to exclude .pyc and .pyo files from 
# the package and compile them on installation. File exclusion is 
# handled by gar.mk and cswclassutils integration by gar.pkg.mk
PYCOMPILE = 1

# Haven't seen a python module with a configure phase so far
CONFIGURE_SCRIPTS ?=

# gar.lib.mk contains implicit targets for setup.py
BUILD_SCRIPTS ?= $(WORKSRC)/setup.py
INSTALL_SCRIPTS ?= $(WORKSRC)/setup.py
INSTALL_ARGS ?= --root=$(DESTDIR) --prefix=$(prefix)
TEST_SCRIPTS ?= $(WORKSRC)/setup.py
TEST_TARGET ?= test
LICENSE ?= PKG-INFO
SPKG_SOURCEURL ?= http://pypi.python.org/pypi/$(NAME)
MASTER_SITES ?= $(PYPI_MIRROR)
PACKAGES ?= $(PYTHON_MODULE_PACKAGE_PREFIX)$(DASHED_NAME)

# for use in any references by specific recipes so it can be replaced easily
# across the tree.  this could later be parameterized for use by multiple
# versions of python too.
SITE_PACKAGES = $(PYTHON_SITE_PACKAGES)

include gar/gar.mk

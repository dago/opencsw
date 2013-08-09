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

# Do not make all Python modules depend on the interpreter. With the
# dual-version packages we would have to make all modules depend on both
# Python versions. It's better to not depend on any Python version.
# _EXTRA_GAR_PKGS += $(PYTHON_PACKAGE_2_6)
# _EXTRA_GAR_PKGS += $(PYTHON_PACKAGE_2_7)

# During the transition to Python 2.7, all modules are built for two Python
# versions: 2.6 and 2.7. This implies the dependency on both CSWpython and
# CSWpython27.
_CATEGORY_MODULATORS ?= PYTHON_VERSION
MODULATIONS_PYTHON_VERSION ?= 2_6 2_7
MERGE_SCRIPTS_isa-default-python_version-2_6 ?= copy-all
MERGE_SCRIPTS_isa-default-python_version-2_7 ?= copy-all
MERGE_SCRIPTS_isa-default-python_version-3_3 ?= copy-all

include gar/gar.mk

GARCOMPILER_PYTHON_2_6 = SOS12U3
GARCOMPILER_PYTHON_2_7 = GNU
GARCOMPILER = $(GARCOMPILER_PYTHON_$(PYTHON_VERSION))

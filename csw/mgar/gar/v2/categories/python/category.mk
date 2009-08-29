# Add a dependency to CSWpython
_EXTRA_GAR_PKGS += CSWpython

# Exclude egg-info files (only needed for easy_install)
_MERGE_EXCLUDE_CATEGORY += .*\.egg-info.*

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

include gar/gar.mk

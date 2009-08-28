# Add a dependency to CSWpython
_EXTRA_GAR_PKGS += CSWpython

# We just set PYCOMPILE, gar.mk then excludes the corresponding .py{c,o} 
# files. Only thing we explicitly exclude here are the egg-info files. 
# gar.pkg.mk handles the usual cswclassutils stuff. 

PYCOMPILE = /opt/csw/lib/python/site-packages/.*\.py
_MERGE_EXCLUDE_CATEGORY += .*\.egg-info.*

# Haven't seen a python module with a configure phase so far
CONFIGURE_SCRIPTS ?=

# gar.lib.mk contains implicit targets for setup.py
BUILD_SCRIPTS ?= $(WORKSRC)/setup.py
INSTALL_SCRIPTS ?= $(WORKSRC)/setup.py
INSTALL_ARGS ?= --root=$(DESTDIR) --prefix=$(prefix)
TEST_SCRIPTS ?= $(WORKSRC)/setup.py

include gar/gar.mk

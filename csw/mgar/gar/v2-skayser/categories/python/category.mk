# Add a dependency to CSWpython
_EXTRA_GAR_PKGS += CSWpython

# Put PYCOMPILE in here for now and let gar.pkg.mk handle the usual
# cswclassutils stuff.
PYCOMPILE = .*\.py

# Could we have "setup.py install" just _not_ compile .py{c,o} files
# in the first place?
_MERGE_EXCLUDE_CATEGORY = .*\.pyo .*\.pyc .*\.egg-info.*

# Haven't seen a python module with a configure phase so far
CONFIGURE_SCRIPTS ?=

# gar.lib.mk contains implicit targets for setup.py
BUILD_SCRIPTS ?= $(WORKSRC)/setup.py
INSTALL_SCRIPTS ?= $(WORKSRC)/setup.py
INSTALL_ARGS ?= --root=$(DESTDIR) --prefix=$(prefix)

include gar/gar.mk

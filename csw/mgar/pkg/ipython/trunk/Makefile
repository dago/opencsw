GARNAME    = ipython
GARVERSION = 0.10
CATEGORIES = lang

DESCRIPTION = Python toolkit for generation of output for the web
define BLURB
	Genshi is a Python library that provides an integrated set of 
	components for parsing, generating, and processing HTML, XML 
	or other textual content for output generation on the web
endef

MASTER_SITES = http://ipython.scipy.org/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

ARCHALL_CSWipython = 1
PACKAGES = CSWipython
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
# comment what this does or remove it
# PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

REQUIRED_PKGS_CSWipython = CSWpython-rt
CATALOGNAME_CSWipython = ipython
SPKG_DESC_CSWipython   = $(DESCRIPTION)

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS   = $(WORKSRC)/setup.py
TEST_SCRIPTS    = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)

include gar/category.mk


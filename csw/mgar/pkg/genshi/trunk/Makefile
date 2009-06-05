GARNAME    = Genshi
GARVERSION = 0.5.1
CATEGORIES = utils

DESCRIPTION = Python toolkit for generation of output for the web
define BLURB
	Genshi is a Python library that provides an integrated set of 
	components for parsing, generating, and processing HTML, XML 
	or other textual content for output generation on the web
endef

MASTER_SITES = http://ftp.edgewall.com/pub/genshi/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

ARCHALL_CSWgenshi = 1
PACKAGES = CSWgenshi
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

REQUIRED_PKGS_CSWgenshi = CSWpython-rt
CATALOGNAME_CSWgenshi = genshi
SPKG_DESC_CSWgenshi   = $(DESCRIPTION)

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS   = $(WORKSRC)/setup.py
TEST_SCRIPTS    = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)

include gar/category.mk


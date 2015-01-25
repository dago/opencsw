NAME = python-augeas
VERSION = 0.5.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Augeas Python Bindings
define BLURB
endef

MASTER_SITES = https://pypi.python.org/packages/source/p/python-augeas/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES += 0001-hardcode_libaugeas.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://augeas.net

PACKAGES = CSWpy-augeas
SPKG_DESC_CSWpy-augeas = Augeas Python Bindings
CATALOGNAME = py_augeas

OBSOLETED_BY_CSWpy-augeas = CSWpyaugeas


DEP_PKGS = CSWaugeas
#Lib needed:
CHECKPKG_OVERRIDES_CSWpy-augeas += surplus-dependency|CSWaugeas


CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 
#TEST_TARGET = check

ARCHALL = 1

include gar/category.mk

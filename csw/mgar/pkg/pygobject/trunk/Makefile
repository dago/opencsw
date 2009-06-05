GARNAME = pygobject
GARVERSION = 2.15.4
CATEGORIES = lang

DESCRIPTION = pygobject support for Python
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.15/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

STRIP_LIBTOOL = 1

PACKAGES = CSWpygobject
REQUIRED_PKGS_CSWpygobject  = CSWpython CSWggettextrt CSWglib2

CATALOGNAME_CSWpygobject = pygobject
SPKG_DESC_CSWpygobject = pygobject support for Python

## patch to change zero sized struct to zero-sized sub-object
PATCHFILES = pygobject.diff

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
#TEST_TARGET = check
TEST_SCRIPTS = 

include gar/category.mk


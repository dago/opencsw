GARNAME = pygobject
GARVERSION = 2.21.1
CATEGORIES = lang
RELVER = $(shell echo $(GARVERSION) | gsed -e 's/\.[0-9]\+$$//')

DESCRIPTION = Python bindings for the GObject library
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(GARNAME)/$(RELVER)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

STRIP_LIBTOOL = 1

PACKAGES = CSWpygobject
RUNTIME_DEP_PKGS_CSWpygobject  = CSWpython CSWggettextrt CSWglib2

CATALOGNAME_CSWpygobject = py_gobject
SPKG_DESC_CSWpygobject = $(DESCRIPTION)
PYCOMPILE = 1

PATCHFILES = 0001-forcing-lglib-2.0.patch

EXTRA_MERGE_EXCLUDE_FILES += .*\.egg-info.* .*\.pyo .*\.pyc

UFILES_REGEX = (\d+(?:\.\d+)*).tar.bz2
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_TARGET = check
TEST_SCRIPTS =

# This package predates the convention and renaming is problematic
CHECKPKG_OVERRIDES_CSWpygobject += pkgname-does-not-start-with-CSWpy-

include gar/category.mk

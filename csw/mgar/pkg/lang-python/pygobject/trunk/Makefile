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

PACKAGES = CSWpy-gobject-devel CSWpygobject CSWlibpyglib-2-0-python0 

CATALOGNAME_CSWpygobject = py_gobject
SPKG_DESC_CSWpygobject = $(DESCRIPTION)
CHECKPKG_OVERRIDES_CSWpygobject += pkgname-does-not-start-with-CSWpy-
RUNTIME_DEP_PKGS_CSWpygobject = CSWpython CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWpygobject += CSWlibpyglib-2-0-python0
PKGFILES_CSWpygobject = $(libdir)/python/site-packages/.*

SPKG_DESC_CSWlibpyglib-2-0-python0 = Runtime library for the Python GObject library
CATALOGNAME_CSWlibpyglib-2-0-python0 = libpyglib_2_0_python0
PKGFILES_CSWlibpyglib-2-0-python0 = $(libdir)/libpyglib-2.0-python.so.0.*
RUNTIME_DEP_PKGS_CSWlibpyglib-2-0-python0 = CSWggettextrt CSWglib2

SPKG_DESC_CSWpy-gobject-devel = Development files for the Python GObject library
CATALOGNAME_CSWpy-gobject-devel = py_gobject_devel
RUNTIME_DEP_PKGS_CSWpy-gobject-devel = CSWpython
ARCHALL_CSWpy-gobject-devel = 1

PYCOMPILE = 1

PATCHFILES = 0001-forcing-lglib-2.0.patch

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

UFILES_REGEX = (\d+(?:\.\d+)*).tar.bz2
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_TARGET = check
TEST_SCRIPTS =

# This package predates the convention and renaming is problematic
CHECKPKG_OVERRIDES_CSWpygobject += pkgname-does-not-start-with-CSWpy-

include gar/category.mk

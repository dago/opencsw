NAME = pygobject
VERSION = 2.21.1
CATEGORIES = lang
RELVER = $(shell echo $(VERSION) | gsed -e 's/\.[0-9]\+$$//')

DESCRIPTION = Python bindings for the GObject library
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(RELVER)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

STRIP_LIBTOOL = 1

PACKAGES = CSWpy-gobject-devel CSWpy-gobject CSWlibpyglib-2-0-py0 

CATALOGNAME_CSWpy-gobject = py_gobject
SPKG_DESC_CSWpy-gobject = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWpy-gobject = CSWpython CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibpyglib-2-0-py0
INCOMPATIBLE_PKGS_CSWpy-gobject = CSWpygobject
PKGFILES_CSWpy-gobject = $(libdir)/python/site-packages/.*

SPKG_DESC_CSWlibpyglib-2-0-py0 = Runtime library for the Python GObject library
CATALOGNAME_CSWlibpyglib-2-0-py0 = libpyglib_2_0_py0
PKGFILES_CSWlibpyglib-2-0-py0 = $(libdir)/libpyglib-2.0-python.so.0.*
RUNTIME_DEP_PKGS_CSWlibpyglib-2-0-py0 = CSWggettextrt CSWglib2

# soname results in a package name that is too long so it was shortened
CHECKPKG_OVERRIDES_CSWlibpyglib-2-0-py0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libpyglib-2.0-python.so.0.0.0|soname=libpyglib-2.0-python.so.0|pkgname=CSWlibpyglib-2-0-py0|expected=['CSWlibpyglib-2-0-python0',|'CSWlibpyglib-2-0-python-0']
SPKG_DESC_CSWpy-gobject-devel = Development files for the Python GObject library
CATALOGNAME_CSWpy-gobject-devel = py_gobject_devel
RUNTIME_DEP_PKGS_CSWpy-gobject-devel = CSWpython

PYCOMPILE = 1

PATCHFILES = 0001-forcing-lglib-2.0.patch

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk

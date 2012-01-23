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

PATCHFILES = 0001-forcing-lglib-2.0.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWpy-gobject
SPKG_DESC_CSWpy-gobject = $(DESCRIPTION)
PKGFILES_CSWpy-gobject = $(libdir)/python/site-packages/.*
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWpython
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWglib2
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibpyglib-2-0-py0
OBSOLETED_BY_CSWpy-gobject = CSWpygobject

PACKAGES += CSWlibpyglib-2-0-py0 
SPKG_DESC_CSWlibpyglib-2-0-py0 = Runtime library for the Python GObject library
PKGFILES_CSWlibpyglib-2-0-py0 = $(libdir)/libpyglib-2.0-python.so.0.*
RUNTIME_DEP_PKGS_CSWlibpyglib-2-0-py0 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibpyglib-2-0-py0 += CSWlibintl8
# soname results in a package name that is too long so it was shortened
CHECKPKG_OVERRIDES_CSWlibpyglib-2-0-py0 += shared-lib-pkgname-mismatch

PACKAGES += CSWpy-gobject-dev
SPKG_DESC_CSWpy-gobject-dev = Development files for the Python GObject library
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWlibpyglib-2-0-py0
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWpython

# These are just comments
CHECKPKG_OVERRIDES_CSWpy-gobject-dev += file-with-bad-content|/usr/local|root/opt/csw/share/pygobject/2.0/codegen/defsgen.py
CHECKPKG_OVERRIDES_CSWpy-gobject-dev += file-with-bad-content|/usr/local|root/opt/csw/share/pygobject/2.0/codegen/h2def.py

PYCOMPILE = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

include gar/category.mk

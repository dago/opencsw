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

PACKAGES += CSWlibpyglib2-0python0
CATALOGNAME_CSWlibpyglib2-0python0 = libpyglib2_0python0
PKGFILES_CSWlibpyglib2-0python0 += $(call baseisadirs,$(libdir),libpyglib-2\.0-python\.so\.0\.0\.0)
PKGFILES_CSWlibpyglib2-0python0 += $(call baseisadirs,$(libdir),libpyglib-2\.0-python\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpyglib2-0python0 += $(DESCRIPTION), libpyglib-2.0-python.so.0
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python0 += CSWlibglib2-0-0

PACKAGES += CSWpy-gobject-dev
OBSOLETED_BY_CSWpy-gobject-dev += CSWpygobject
SPKG_DESC_CSWpy-gobject-dev = Development files for the Python GObject library
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWlibpyglib2-0python0
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWpython

# These are just comments
CHECKPKG_OVERRIDES_CSWpy-gobject-dev += file-with-bad-content|/usr/local|root/opt/csw/share/pygobject/2.0/codegen/defsgen.py
CHECKPKG_OVERRIDES_CSWpy-gobject-dev += file-with-bad-content|/usr/local|root/opt/csw/share/pygobject/2.0/codegen/h2def.py

PACKAGES += CSWpy-gobject
OBSOLETED_BY_CSWpy-gobject += CSWpygobject
SPKG_DESC_CSWpy-gobject = $(DESCRIPTION)
PKGFILES_CSWpy-gobject = $(libdir)/python/site-packages/.*
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWpython
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibpyglib2-0python0

PYCOMPILE = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_TARGET = check
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

include gar/category.mk

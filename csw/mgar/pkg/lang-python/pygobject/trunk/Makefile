# $Id$

NAME = pygobject
VERSION = 2.90.4
CATEGORIES = lang
RELVER = $(shell echo $(VERSION) | gsed -e 's/\.[0-9]\+$$//')

DESCRIPTION = Python bindings for the GObject library
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(RELVER)/
DISTFILES  = $(NAME)-$(# PATCHFILES = 0001-forcing-lglib-2.0.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
BUILD_DEP_PKGS = CSWlibffi-dev

PACKAGES += CSWlibpyglib-gi2-0python0
PKGFILES_CSWlibpyglib-gi2-0python0 += $(call baseisadirs,$(libdir),libpyglib-gi-2\.0-python\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpyglib-gi2-0python0 += $(DESCRIPTION), libpyglib-gi-2.0-python.so.0
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWlibpyglib-gi2-0python0
RUNTIME_DEP_PKGS_CSWlibpyglib-gi2-0python0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibpyglib-gi_PKGS_CSWlibpyglib2-0python0 += CSWlibglib2-0-0

PACKAGES += CSWpy-gobject-dev
OBSOLETED_BY_CSWpy-gobject-dev += CSWpygobject
SPKG_DESC_CSWpy-gobject-dev = Development files for the Python GObject library
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWli-dev += CSWpython

# These are just comments
CHECKPKG_OVERRIDES_CSWpython-package-missing-py26-files
CHECKPKG_OVERRIDES_CSWpy-gobject-dev += python-package-missing-py-files0/codegen/h2def.py

PACKAGES += CSWpy-gobject
OBSOLETED_BY_CSWpy-gobject += CSWpygobject
SPKG_DESC_CSWpy-gobject = $(DESCRIPTION)
PKGFILES_CSWpy-gobject .*/site-packages/.*
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibffi5
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgirepository1-0-1
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibglibt += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpypyglib-gi2-0python0

PYCOMPILE = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
# GS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_TARGET = check
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

includ
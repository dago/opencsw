# $Id$

NAME = pygobject
VERSION = 2.28.6
CATEGORIES = lang
RELVER = $(shell echo $(VERSION) | gsed -e 'MAJOR = $(shell echo $(VERSION) | gsed -e 's/\(^[0-9]\+\)\..*/\1-e '# keep the 'configure; make; make install'-mantra'# CATEGORIES = python's/\.[0-9]\+$$//')

DESCRIPTION = Python bindings for the GObject library
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(RELVER)/
DISTFILES  = $(NAME)-$(PATCHFILES = 0001-forcing-lglib-2.0.patch
PATCHFILES = 0002-gi-backport.patch

GARCOMPILER = GCC4

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS = CSWlibffi-dev

# add this because we do not use the pyton category
# _MERGE_EXCLUDE_CATEGORY += .*/$(NAME)/test
# _MERGE_EXCLUDE_CATEGORY += .*/$(NAME)/test/.*


EXTRA_MODULATORS += PYTHON_VERSION
MODULATIONS_PYTHON_VERSION = 2.6 2.7
# We need 64 bit just once as it is without python anyway
SKIP_MODULATIONS += isa-sparcv9-python_version-2.7
SKIP_MODULATIONS += isa-amd64-python_version-2.7
PYTHON = $(bindir)/python$(PYTHON_VERSION)
MERGE_SCRIPTS_isa-default-python_version-2.6 += copy-all
MERGE_SCRIPTS_isa-default-python_version-2.7 += copy-all
MERGE_SCRIPTS_isa-default64-python_version-2.6 += copy-relocated-only
MERGE_DIRS_isa-default64-python_version-2.6 += $(libdir)

PACKAGES += CSWlibpyglib2-0python2-6-0
CATALOGNAME_CSWlibpyglib2-0python2-6-0 = libpyglib2_0python2_6_0
PKGFILES_CSWlibpyglib2-0python2-6-0 += $(call baseisadirs,$(libdir),libpyglib-2\.0-python2\.6\.so\.0\.0\.0)
PKGFILES_CSWlibpyglib2-0python2-6-0 += $(call baseisadirs,$(libdir),libpyglib-2\.0-python2\.6\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpyglib2-0python2-6-0 += $(DESCRIPTION), libpyglib-2.0-python2.6.so.0
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-6-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-6-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-6-0 += CSWlibglib2-0-0

RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-6-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-6-0 += $(RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-6-0_$(GARCH))


PACKAGES += CSWlibpyglib2-0python2-7-0
CATALOGNAME_CSWlibpyglib2-0python2-7-0 = libpyglib2_0python2_7_0
PKGFILES_CSWlibpyglib2-0python2-7-0 += $(call baseisadirs,$(libdir),libpyglib-2\.0-python2\.7\.so\.0\.0\.0)
PKGFILES_CSWlibpyglib2-0python2-7-0 += $(call baseisadirs,$(libdir),libpyglib-2\.0-python2\.7\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibpyglib2-0python2-7-0 += $(DESCRIPTION), libpyglib-2.0-python2.7.so.0
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-7-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-7-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-7-0 += CSWlibglib2-0-0

RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-7-0_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-7-0 += $(RUNTIME_DEP_PKGS_CSWlibpyglib2-0python2-7-0_$(GARCH))+= CSWlibglib2-0-0

PACKAGES += CSWpy-gobject-dev
OBSOLETED_BY_CSWpy-gobject-dev += CSWpygobject
SPKG_DESC_CSWpy-gobject-dev = Development files for the Python GObject library
RUNTIME_DEP_PKGS_CSWpy-gobgthread2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWlibglib2-0-liRUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWlibpyglib2-0python2-6-0
RUNTIME_DEP_PKGS_CSWpy-gobject-dev += CSWlibpyglib2-0python2-7-li-dev += CSWpython

# These are just comments
CHECKPKG_OVERRIDES_CSWpython-package-missing-py26-files
CHECKPKG_OVERRIDES_CSWpy-gobject-dev += python-package-missing-py-files0/codegen/h2def.py

PACKAGES#  += CSWpy-gobject
OBSOLETED_BY_CSWpy-gobject += CSWpygobject
SPKG_DESC_CSWpy-gobject = $(DESCRIPTION)
PKGFI+= $(libdir)/python.*/site-packages/.*
PKGFILES_CSWpy-gobject += $(datadir)/$(NAME)/$(MAJOR)\.2/.*
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibffi5
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgirepository1-0-1
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibglibt += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpygio2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibpyglib2-0python2-7-0
RUNTIME_DEP_PKGS_CSWpy-gobject += CSWlibpyglib2-0python2-6-0

RUNTIME_DEP_PKGS_CSWpy-gobject_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpy-gobject_sparc += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject_sparc += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWpy-gobject += $(RUNTIME_DEP_PKGS_CSWpy-gobject_$(GARCH))

STRIP_LIBTOOL = 1

EXTRA_CFLAGS = -std=c99 -D_XPG6 -D__EXTENSIONS__
EXTRA_BUILD_ENV = V=1
EXTRA_CONFIGURE_ENV = PYTHON=python$(PYTHON_VERSION)

CONFIGURE_ARGS  = $(DIRPATHS)
# GS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_TARGET = checPYCOMPILE = 1
EXTRA_MERGE_EXCLUDE_FILES += .*\.pyo .*\.pyc

include gar/category.mk

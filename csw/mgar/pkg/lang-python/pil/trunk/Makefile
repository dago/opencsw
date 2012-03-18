# $Id$

NAME = pil
VERSION = 1.1.7
CATEGORIES = python
GARTYPE = v2
DISTNAME = Imaging-$(VERSION)

define BLURB
	The Python Imaging Library (PIL) adds image processing capabilities to your
	Python interpreter. This library supports many file formats, and provides
	powerful image processing and graphics capabilities.
endef

MASTER_SITES = http://effbot.org/downloads/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpy-pil CSWpil

SPKG_DESC_CSWpy-pil = Python Imaging Library
SPKG_DESC_CSWpil = An empty transitional package

CATALOGNAME_CSWpy-pil = py_pil
CATALOGNAME_CSWpil    = pil

ARCHALL_CSWpil = 1

PKGFILES_CSWpil = NONE

RUNTIME_DEP_PKGS_CSWpy-pil += CSWftype2
RUNTIME_DEP_PKGS_CSWpy-pil += CSWjpeg
RUNTIME_DEP_PKGS_CSWpy-pil += CSWlcmsrt
RUNTIME_DEP_PKGS_CSWpy-pil += CSWtcl
RUNTIME_DEP_PKGS_CSWpy-pil += CSWtk
RUNTIME_DEP_PKGS_CSWpy-pil += CSWzlib

RUNTIME_DEP_PKGS_CSWpil += CSWpy-pil

UFILES_REGEX = Imaging-(\d+(?:\.\d+)*).tar.gz
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyc

# The empty transitional package still has the dependency on CSWpython added by
# GAR.  It's not really necessary, becayse CSWpy-pil depends on Python too, but
# it doesn't do any harm either.
CHECKPKG_OVERRIDES_CSWpil += surplus-dependency|CSWpython
# Transitional dependency.
CHECKPKG_OVERRIDES_CSWpil += surplus-dependency|CSWpy-pil

TEST_SCRIPTS =

LICENSE = README

include gar/category.mk


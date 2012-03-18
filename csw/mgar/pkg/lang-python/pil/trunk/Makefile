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

UFILES_REGEX = Imaging-(\d+(?:\.\d+)*).tar.gz
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyc

PACKAGES = CSWpy-pil
SPKG_DESC_CSWpy-pil = Python Imaging Library
RUNTIME_DEP_PKGS_CSWpy-pil += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpy-pil += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWpy-pil += CSWliblcms1
RUNTIME_DEP_PKGS_CSWpy-pil += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pil += CSWlibz1
RUNTIME_DEP_PKGS_CSWpy-pil += CSWtcl
RUNTIME_DEP_PKGS_CSWpy-pil += CSWtk

CHECKPKG_OVERRIDES_CSWpy-pil += surplus-dependency|CSWtcl
CHECKPKG_OVERRIDES_CSWpy-pil += surplus-dependency|CSWtk

OBSOLETED_BY_CSWpy-pil = CSWpil
CHECKPKG_OVERRIDES_CSWpil += surplus-dependency|CSWpython

TEST_SCRIPTS =

LICENSE = README

include gar/category.mk

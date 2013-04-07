# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = poster
VERSION = 0.8.1
GARTYPE = v2

DESCRIPTION = Streaming HTTP uploads and multipart/form-data encoding
define BLURB
endef

CATEGORIES = python

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
SKIPTEST = 1

ARCHALL_CSWpy-poster = 1

EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/python/site-packages/tests/__init__.py

include gar/category.mk

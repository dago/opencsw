# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = recutils
VERSION = 1.5
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = GNU Recutils
define BLURB
  GNU Recutils is a set of tools and libraries to access human-editable, plain text databases called recfiles.
  The data is stored as a sequence of records, each record containing an arbitrary number of named fields.
endef

MASTER_SITES = $(GNU_MIRROR)
MASTER_SITES += ftp://alpha.gnu.org/gnu/$(GNU_PROJ)/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWrecutils
SPKG_DESC_CSWrecutils = GNU recutils
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibrec0
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibreadline6
# This is just an emacs mode. It can be used when emacs is installed, no need to force dependency
CHECKPKG_OVERRIDES_CSWrecutils += missing-dependency|CSWemacscommon

PACKAGES += CSWlibrec0
SPKG_DESC_CSWlibrec0 = GNU recutils library, librec.so.0
PKGFILES_CSWlibrec0 += $(call pkgfiles_lib,librec.so.0)
RUNTIME_DEP_PKGS_CSWlibrec0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrec0 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibrec0 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibrec0 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibrec0 += CSWlibreadline6

PACKAGES += CSWlibrec-dev
SPKG_DESC_CSWlibrec-dev = Development files for librec.so.0
PKGFILES_CSWlibrec-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibrec-dev += CSWlibrec0

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset\.alias

include gar/category.mk


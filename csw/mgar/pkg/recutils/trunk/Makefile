# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = recutils
VERSION = 1.3.91
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

RUNTIME_DEP_PKGS_CSWrecutils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWrecutils += CSWemacscommon
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWrecutils += CSWlibgcrypt11

# I am not sure if anyone is actually developing against te library
# Looks like it is more like a private lib. Overwrite for now.
CHECKPKG_OVERRIDES_CSWrecutils += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/librec.so
CHECKPKG_OVERRIDES_CSWrecutils += shared-lib-pkgname-mismatch|file=opt/csw/lib/librec.so.0.0.0|soname=librec.so.0|pkgname=CSWrecutils|expected=CSWlibrec0

EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset\.alias

include gar/category.mk


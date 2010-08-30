# $Id$
GARNAME = libdnet
GARVERSION = 1.11
CATEGORIES = lib

DESCRIPTION = A simplified, portable interface to several low-level networking routines
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

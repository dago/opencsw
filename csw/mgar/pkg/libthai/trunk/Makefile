GARNAME = libthai
GARVERSION = 0.1.4
CATEGORIES = lib

DESCRIPTION = Thai language support routines
define BLURB
  LibThai is a set of Thai language support routines aimed to ease
  developers tasks to incorporate Thai language support in their applications.
  It includes important Thai-specific functions e.g. word breaking, input
  and output methods as well as basic character and string supports.
  LibThai is an Open Source and collaborative effort initiated by
  Thai Linux Working Group and opened for all contributors.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=34448
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://linux.thai.net/projects/libthai/

BUILD64 = 1
NORUNPATH = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

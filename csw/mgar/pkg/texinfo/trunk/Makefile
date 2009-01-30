GARNAME = texinfo
RELEASE = a
GARVERSION = 4.13
DISTVERSION = $(GARVERSION)$(RELEASE)
CATEGORIES = utils

DESCRIPTION = The GNU Documentation System
define BLURB
  Texinfo is a documentation system that uses a single source to produce both
  on-line information (info, HTML, XML, Docbook) and printed output (DVI, PDF).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES += $(call admfiles,CSWtexinfo,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWgsed CSWncurses CSWiconv CSWggettext

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

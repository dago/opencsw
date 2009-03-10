GARNAME = OLE-Storage_Lite
GARVERSION = 0.18
CATEGORIES = cpan
AUTHOR = JMCNAMARA

DESCRIPTION = Simple Class for OLE document interface
define BLURB
  This module allows you to read and write an OLE-Structured file.
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpmolestoragelite,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

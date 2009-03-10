GARNAME = Filesys-Df
GARVERSION = 0.92
CATEGORIES = cpan
AUTHOR = IGUTHRIE

DESCRIPTION = Perl extension for filesystem disk space information
define BLURB
  This module provides a way to obtain filesystem disk space information.
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpmfilesysdf,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

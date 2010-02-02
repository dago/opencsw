GARNAME = Filesys-Df
GARVERSION = 0.92
CATEGORIES = cpan
AUTHOR = IGUTHRIE

DESCRIPTION = Perl extension for filesystem disk space information
define BLURB
  This module provides a way to obtain filesystem disk space information.
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWpmfilesysdf
CATALOGNAME = pm_filesysdf

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

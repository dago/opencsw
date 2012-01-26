NAME = Filesys-Df
VERSION = 0.92
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = IGUTHRIE

DESCRIPTION = Perl extension for filesystem disk space information
define BLURB
  This module provides a way to obtain filesystem disk space information.
endef

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWpmfilesysdf
CATALOGNAME = pm_filesysdf

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

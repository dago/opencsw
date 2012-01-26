NAME = Archive-Extract
VERSION = 0.48
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BINGOS

DESCRIPTION = A generic archive extracting mechanism
define BLURB
  Archive::Extract is a generic archive extraction mechanism.  It allows you
  to extract any archive file of the type .tar, .tar.gz, .gz, tar.bz2, .tbz,
  .bz2 or .zip without having to worry how it does so, or use different
  interfaces for each type by using either perl modules, or commandline tools
  on your system.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-archive-extract
CATALOGNAME = pm_archive_extract
SPKG_DESC_CSWpm-archive-extract = $(DESCRIPTION)
ARCHALL = 1
OBSOLETED_BY_CSWpm-archive-extract = CSWpmarchiveextract
CATALOGNAME_CSWpmarchiveextract = pm_archiveextract

RUNTIME_DEP_PKGS += CSWpmipccmd CSWpmlclemktxtsimple CSWpmmodloadcond CSWpmprmscheck

EXTRA_MERGE_EXCLUDE_FILES = \/opt\/csw\/share\/man.*

include gar/category.mk


NAME = Archive-Extract
VERSION = 0.46
CATEGORIES = cpan
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

PACKAGES = CSWpmarchiveextract
CATALOGNAME = pm_archiveextract
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmipccmd CSWpmlclemktxtsimple CSWpmmodloadcond CSWpmprmscheck

EXTRA_MERGE_EXCLUDE_FILES = \/opt\/csw\/share\/man.*

include gar/category.mk


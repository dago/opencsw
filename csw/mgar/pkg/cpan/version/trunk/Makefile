NAME = version
VERSION = 0.88
CATEGORIES = cpan
AUTHOR = JPEACOCK

DESCRIPTION = Perl extension for Version Objects
define BLURB
  Overloaded version objects for all modern versions of Perl. This module
  implements all of the features of version objects which will be part of Perl
  5.10.0.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-version
CATALOGNAME = pm_version
SPKG_DESC_CSWpm-version = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-version = CSWpmversion
CATALOGNAME_CSWpmversion = pm_version_stub

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk

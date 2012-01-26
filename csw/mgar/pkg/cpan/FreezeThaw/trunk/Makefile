NAME = FreezeThaw
VERSION = 0.5001
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ILYAZ

DESCRIPTION = Converting Perl structures to strings and back.
define BLURB
  Converts data to/from stringified form, appropriate for saving-to and
  reading-from permanent storage.  Deals with objects, circular lists,
  repeated appearence of the same refence.  Does not deal with overloaded
  stringify operator yet.
endef

MASTER_SITES = $(addsuffix modules/,$(CPAN_MIRRORS))
DISTFILES = COPYING

PACKAGES = CSWpmfreezethaw
CATALOGNAME = pm_freezethaw

ARCHALL = 1

include gar/category.mk

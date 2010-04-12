GARNAME = Test-NoWarnings
GARVERSION = 1.01
CATEGORIES = cpan
AUTHOR = ADAMK

DESCRIPTION = Make sure you didn't emit any warnings while testing
define BLURB
  Make sure you didn't emit any warnings while testing
endef

PACKAGES = CSWpmtestnowarnings
CATALOGNAME = pm_testnowarnings
ARCHALL = 1

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk

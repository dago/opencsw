GARNAME = IDNA-Punycode
GARVERSION = 1.001
CATEGORIES = cpan
AUTHOR = CFAERBER

DESCRIPTION = Deprecated module for IDNA and Punyode
define BLURB
  Deprecated module for IDNA and Punyode
endef

PACKAGES = CSWpmidnapunycode
CATALOGNAME = pm_idnapunycode
#ARCHALL = 1

LICENSE = LICENSE

#Warning: prerequisite Net::IDN::Encode 1 not found.
#Warning: prerequisite Net::IDN::Punycode 1 not found.
#Warning: prerequisite Test::NoWarnings 0 not found.

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk

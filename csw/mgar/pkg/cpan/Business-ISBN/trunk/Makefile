NAME = Business-ISBN
VERSION = 2.05
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = BDFOY

DESCRIPTION = Work with International Standard Book Numbers
define BLURB
  Work with International Standard Book Numbers
endef

LICENSE = LICENSE

PACKAGES = CSWpm-business-isbn
CATALOGNAME = pm_business_isbn
ARCHALL = 1

#BUILD_DEP_PKGS += CSWpm-business-isbn-data
RUNTIME_DEP_PKGS += CSWpm-business-isbn-data

CHECKPKG_OVERRIDES_CSWpm-business-isbn += unidentified-dependency|CSWpm-business-isbn-data

CONFIGURE_ARGS =

include gar/category.mk


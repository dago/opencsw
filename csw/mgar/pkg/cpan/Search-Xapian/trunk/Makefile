NAME = Search-Xapian
VERSION = 1.0.16.0
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = OLLY

DESCRIPTION = A Perl XS frontend to the Xapian C++ search library
define BLURB
endef

PACKAGES = CSWpmsearchxapian
CATALOGNAME = pm_searchxapian

BUILD_DEP_PKGS = CSWxapiancore
RUNTIME_DEP_PKGS = $(BUILD_DEP_PKGS)

PATCHFILES = search-xapian-bool.patch
PATCHDIRLEVEL = 0

include gar/category.mk

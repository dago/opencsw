NAME = MIME-tools
VERSION = 5.428
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ERYQ

DESCRIPTION = Modules for parsing and creating MIME entities
define BLURB
  Modules for parsing (and creating!) MIME entities
endef

DEPENDS += cpan/Mail-Tools cpan/Convert-BinHex cpan/Unix-Syslog cpan/IO-stringy

PACKAGES = CSWpmmimetools
CATALOGNAME = pm_mimetools
ARCHALL = 1

COPYING = LICENSE

CHECKPKG_OVERRIDES_CSWpmmimetools += catalogname-does-not-match-pkgname|pkgname=CSWpmmimetools|catalogname=pm_mimetools|expected-catalogname=pmmimetools

include gar/category.mk

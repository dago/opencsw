NAME = FCGI
VERSION = 0.73
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = FLORA

DESCRIPTION = Fast CGI module
define BLURB
  Fast CGI module for Perl
endef

PACKAGES = CSWpmfcgi
CATALOGNAME = pm_fcgi

LICENSE = README

CHECKPKG_OVERRIDES_CSWpmfcgi += catalogname-does-not-match-pkgname|pkgname=CSWpmfcgi|catalogname=pm_fcgi|expected-catalogname=pmfcgi

include gar/category.mk

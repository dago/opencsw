NAME = CGI-SpeedyCGI
VERSION = 2.22
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = HORROCKS

DESCRIPTION = Speed up perl scripts by running them persistently
define BLURB
  SpeedyCGI is a way to run perl scripts persistently, which can make them run
  much more quickly.
endef

PATCHFILES  = 0001-Use-Newx-instead-of-deprecated-New.patch
PATCHFILES += 0003-mem-leak.patch

PACKAGES = CSWpmspeedycgiperl
CATALOGNAME = pm_speedycgiperl

# Don't build the apache/apache2 modules
PATCHFILES += build.diff

CHECKPKG_OVERRIDES_CSWpmspeedycgiperl += catalogname-does-not-match-pkgname|pkgname=CSWpmspeedycgiperl|catalogname=pm_speedycgiperl|expected-catalogname=pmspeedycgiperl

include gar/category.mk

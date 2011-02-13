NAME = CGI-SpeedyCGI
VERSION = 2.22
CATEGORIES = cpan
AUTHOR = HORROCKS

DESCRIPTION = Speed up perl scripts by running them persistently
define BLURB
  SpeedyCGI is a way to run perl scripts persistently, which can make them run
  much more quickly.
endef

PATCHFILES = 0001-Use-Newx-instead-of-deprecated-New.patch

PACKAGES = CSWpmspeedycgi
CATALOGNAME = pm_speedycgi

# Don't build the apache/apache2 modules
PATCHFILES += build.diff

include gar/category.mk

GARNAME = gettext
GARVERSION = 1.05
CATEGORIES = cpan
AUTHOR = PVANDRY

DESCRIPTION = Message handling functions
define BLURB
  The gettext module permits access from perl to the gettext() family
  of functions for retrieving message strings from databases constructed
  to internationalize software.
endef

PACKAGES = CSWpmlocalegettext
CATALOGNAME = pm_localegettext

REQUIRED_PKGS = CSWggettextrt

include gar/category.mk

BUILD_ARGS += OTHERLDFLAGS="-lintl -R$(libdir)"

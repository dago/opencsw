NAME = App-CLI
VERSION = 0.313
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CORNELIUS

DESCRIPTION = Dispatcher module for command line interface programs
define BLURB
endef

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWpm-app-cli
CATALOGNAME = pm_app_cli
SPKG_DESC_CSWpm-app-cli = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-app-cli = CSWpmappcli
CATALOGNAME_CSWpmappcli = pm_appcli

RUNTIME_DEP_PKGS  = CSWpm-locale-maketext-simple
RUNTIME_DEP_PKGS += CSWpm-pod-simple

ARCHALL = 1

include gar/category.mk

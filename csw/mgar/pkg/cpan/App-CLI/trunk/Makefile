NAME = App-CLI
VERSION = 0.313
CATEGORIES = cpan
AUTHOR = CORNELIUS

DESCRIPTION = Dispatcher module for command line interface programs
define BLURB
  App::CLI dispatches CLI (command line interface) based commands into command
  classes. It also supports subcommand and per-command options.
endef

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWpm-app-cli
CATALOGNAME = pm_app_cli
SPKG_DESC_CSWpm-app-cli = $(DESCRIPTION)
ARCHALL = 1
OBSOLETED_BY_CSWpm-app-cli = CSWpmappcli
CATALOGNAME_CSWpmappcli = pm_appcli

RUNTIME_DEP_PKGS = CSWpmlclemktxtsimple CSWpmpodsimple

#CHECKPKG_OVERRIDES_CSWpmappcli += surplus-dependency|CSWpmpodsimple
#CHECKPKG_OVERRIDES_CSWpmappcli += surplus-dependency|CSWpmlclemktxtsimple

include gar/category.mk

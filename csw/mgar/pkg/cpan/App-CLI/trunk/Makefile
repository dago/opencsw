NAME = App-CLI
VERSION = 0.08
CATEGORIES = cpan
AUTHOR = ALEXMV

DESCRIPTION = Dispatcher module for command line interface programs
define BLURB
  App::CLI dispatches CLI (command line interface) based commands into command
  classes. It also supports subcommand and per-command options.
endef

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWpmappcli
CATALOGNAME = pm_appcli
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmlclemktxtsimple CSWpmpodsimple

CHECKPKG_OVERRIDES_CSWpmappcli += surplus-dependency|CSWpmpodsimple
CHECKPKG_OVERRIDES_CSWpmappcli += surplus-dependency|CSWpmlclemktxtsimple

include gar/category.mk

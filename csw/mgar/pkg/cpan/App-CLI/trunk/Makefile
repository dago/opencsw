GARNAME = App-CLI
GARVERSION = 0.08
CATEGORIES = cpan
AUTHOR = ALEXMV

DESCRIPTION = Dispatcher module for command line interface programs
define BLURB
  App::CLI dispatches CLI (command line interface) based commands into command
  classes. It also supports subcommand and per-command options.
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpmappcli,)

REQUIRED_PKGS = CSWpmlclemktxtsimple CSWpmpodsimple

DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/Pod-Simple
DEPENDS += cpan/Getopt-Long

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

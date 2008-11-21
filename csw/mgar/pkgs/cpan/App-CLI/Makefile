GARNAME = App-CLI
GARVERSION = 0.07
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = Dispatcher module for command line interface programs
define BLURB
  App::CLI dispatches CLI (command line interface) based commands into command
  classes. It also supports subcommand and per-command options.
endef

DISTFILES += $(call admfiles,CSWpmappcli,depend prototype)

DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/Pod-Simple
DEPENDS += cpan/ExtUtils-AutoInstall

include ../category.mk


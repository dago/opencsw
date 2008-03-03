GARNAME = Gnome2-GConf
GARVERSION = 1.000
CATEGORIES = cpan
AUTHOR = RMCFARLA

DESCRIPTION = wrappers for the GConf configuration engine.
define BLURB
  This module allows you to use the GConf configuration system in order to
  store/retrieve the configuration of an application. The GConf system is a
  powerful configuration manager based on a user daemon that handles a set of
  key and value pairs, and notifies any changes of the value to every program
  that monitors those keys. GConf is used by GNOME 2.x.
endef

# Unstable branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += $(call admfiles,CSWpmgnome2gconf,depend)

DEPENDS += cpan/Gtk2

include ../category.mk

AUTHOR_ID := $(AUTHOR_ID)/Gtk2-Perl

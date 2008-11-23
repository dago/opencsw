GARNAME = Gnome2
GARVERSION = 1.001
CATEGORIES = cpan
AUTHOR = RMCFARLA

DESCRIPTION = interface to the 2.x series of the GNOME libraries
define BLURB
  Perl bindings to the 2.x series of the GNOME libraries. This module allows
  you to interface with the libgnome and libgnomeui libraries to create GNOME
  applications.
endef

# Unstable branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += $(call admfiles,CSWpmgnome2,depend)

DEPENDS += cpan/Gnome2-VFS
DEPENDS += cpan/Gnome2-Canvas

# Tests require Gnome session manager
TEST_SCRIPTS =

include gar/category.mk

AUTHOR_ID := $(AUTHOR_ID)/Gtk2-Perl

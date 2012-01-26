NAME = Gnome2-VFS
VERSION = 1.003
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RMCFARLA

DESCRIPTION = interface to the 2.x series of the GNOME VFS library
define BLURB
  Perl bindings to the 2.x series of the GNOME VFS library. This module allows
  you to interface with the gnome-vfs libraries.
endef

# Unstable branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += $(call admfiles,CSWpmgnome2vfs,depend)

DEPENDS += cpan/Gtk2

include gar/category.mk

AUTHOR_ID := $(AUTHOR_ID)/Gtk2-Perl

GARNAME = Gnome2-Canvas
GARVERSION = 1.001
CATEGORIES = cpan
AUTHOR = RMCFARLA

DESCRIPTION = interface to the Gnome Canvas
define BLURB
  The Gnome2::Canvas module allows a perl developer to use the Gnome Canvas.
  The Gnome Canvas is a high-level engine for structured graphics; see
  Frederico Mena Quintero's whitepaper for more info:
  http://developer.gnome.org/doc/whitepapers/canvas/canvas.html
endef

# Unstable branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += $(call admfiles,CSWpmgnome2canvas,depend)

DEPENDS += cpan/Gtk2

include ../category.mk

AUTHOR_ID := $(AUTHOR_ID)/Gtk2-Perl

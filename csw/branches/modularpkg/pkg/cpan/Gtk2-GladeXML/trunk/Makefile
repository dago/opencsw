GARNAME = Gtk2-GladeXML
GARVERSION = 1.004
CATEGORIES = cpan
AUTHOR = RMCFARLA

DESCRIPTION = wrappers for the Gtk2::GladeXML utilities.
define BLURB
  Glade is open source project that provides utilities for rapid user
  interface development. After designing an application with glade-2 the
  layout and configuration is saved in a XML formatted file. libglade is a
  library to load and use files of this particular XML format at application
  run time. This module is a set of mappings of libglade. More specifically
  the gladexml portion of libglade. These mappings allow access to libglade
  from PERL code.  Better yet you can load a file's contents into a PERL
  scalar do a few magical regular expressions to customize things and the load
  up the app. It doesn't get any easier.
endef

# Unstable branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += $(call admfiles,CSWpmgtk2gladexml,depend)

DEPENDS += cpan/Gtk2

include gar/category.mk

AUTHOR_ID := $(AUTHOR_ID)/Gtk2-Perl

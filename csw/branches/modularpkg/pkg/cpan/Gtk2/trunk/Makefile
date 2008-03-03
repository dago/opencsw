GARNAME = Gtk2
GARVERSION = 1.043
CATEGORIES = cpan
AUTHOR = RMCFARLA

DESCRIPTION =  interface to the 2.x series of the Gimp Toolkit library
define BLURB
  Perl bindings to the 2.x series of the Gtk+ widget set.  This module allows
  you to write graphical user interfaces in a perlish and object-oriented way,
  freeing you from the casting and memory management in C, yet remaining very
  close in spirit to original API.
endef

# Unstable branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += CSWpmgtk2.gspec CSWpmgtk2.depend

DEPENDS += lib/gtk2
DEPENDS += cpan/Glib

include gar/category.mk

AUTHOR_ID := $(AUTHOR_ID)/Gtk2-Perl

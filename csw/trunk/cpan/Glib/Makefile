GARNAME = Glib
GARVERSION = 1.043
CATEGORIES = cpan
AUTHOR = RMCFARLA

DESCRIPTION = wrappers for the GLib utility and Object libraries
define BLURB
  This module provides perl access to GLib and GLib's GObject libraries. GLib
  is a portability and utility library; GObject provides a generic type system
  with inheritance and a powerful signal system. Together these libraries are
  used as the foundation for many of the libraries that make up the Gnome
  environment, and are used in many unrelated projects.
endef

# Unstable branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += $(call admfiles,CSWpmglib,)

DEPENDS += lib/glib2
DEPENDS += cpan/ExtUtils-Depends
DEPENDS += cpan/ExtUtils-PkgConfig

include ../category.mk

AUTHOR_ID := $(AUTHOR_ID)/Gtk2-Perl

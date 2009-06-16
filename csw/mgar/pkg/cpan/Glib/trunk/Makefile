GARNAME = Glib
GARVERSION = 1.221
CATEGORIES = cpan
AUTHOR = TSCH

DESCRIPTION = wrappers for the GLib utility and Object libraries
define BLURB
  This module provides perl access to GLib and GLib's GObject libraries. GLib
  is a portability and utility library; GObject provides a generic type system
  with inheritance and a powerful signal system. Together these libraries are
  used as the foundation for many of the libraries that make up the Gnome
  environment, and are used in many unrelated projects.
endef

DISTFILES += $(call admfiles,CSWpmglib,)

DEPENDS += lib/glib2
DEPENDS += cpan/ExtUtils-Depends
DEPENDS += cpan/ExtUtils-PkgConfig

include gar/category.mk

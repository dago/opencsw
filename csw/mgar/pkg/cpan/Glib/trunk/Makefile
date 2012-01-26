NAME = Glib
VERSION = 1.223
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TSCH

DESCRIPTION = wrappers for the GLib utility and Object libraries
define BLURB
  This module provides perl access to GLib and GLib's GObject libraries. GLib
  is a portability and utility library; GObject provides a generic type system
  with inheritance and a powerful signal system. Together these libraries are
  used as the foundation for many of the libraries that make up the Gnome
  environment, and are used in many unrelated projects.
endef

BUILD_DEP_PKGS 	= CSWpmextutilsdepends CSWpmextutpkgconf
RUNTIME_DEP_PKGS_CSWpmglib = CSWpmextutilsdepends CSWpmextutpkgconf CSWggettextrt CSWglib2

CATALOGNAME 	= pm_glib
PACKAGES	= CSWpmglib

LICENSE = README

include gar/category.mk

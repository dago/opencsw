GARNAME = Gimp
GARVERSION = 2.0
CATEGORIES = cpan
AUTHOR = SJBURGES

DESCRIPTION = Perl extension for writing Gimp extensions
define BLURB
  This version of the module only works for gimp-1.3 CVS (as of 12/12/03) or
  higher (including 2.0).
endef

DISTFILES += CSWpmgimp.gspec CSWpmgimp.depend

DEPENDS += utils/gimp
DEPENDS += cpan/PDL cpan/Gtk2


PREREQUISITE_PKGS       = CSWpmpdl CSWpmgtk2 
PKGS_REQUIRED_CSWpmglib = CSWpmpdl CSWpmgtk2 CSWgimplibs

CATALOGNAME = pm_gimp
PACKAGES    = CSWpmgimp

ARCHALL_CSWpmgimp = 1

LICENSE = README

include gar/category.mk


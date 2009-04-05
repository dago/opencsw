GARNAME = libgoffice
GARVERSION = 0.7.4
CATEGORIES = gnome

DESCRIPTION = Document centric objects library
define BLURB
	GOffice is a library of document centric objects and utilities building on
	top of GLib and Gtk+.
endef

MASTER_SITES =  $(GNOME_ROOT)/goffice/$(GNOME_SUBV)/
DISTFILES  = goffice-$(GARVERSION).tar.gz
DISTNAME  = goffice-$(GARVERSION)

REQUIRED_PKGS += CSWgconf2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk
REQUIRED_PKGS += CSWlibcairo CSWlibglade2 CSWlibgsf CSWlibxml2 CSWlibxrender
REQUIRED_PKGS += CSWpango CSWsunmath CSWzlib
REQUIRED_PKGS += CSWbonobo2 CSWgnomekeyring CSWgnomevfs2 CSWlibart
REQUIRED_PKGS += CSWlibbonoboui CSWlibgnome CSWlibgnomecanvas CSWlibgnomeui
REQUIRED_PKGS += CSWlibpopt CSWorbit2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = goffice-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk

PATH :=/opt/csw/bin:/opt/csw/gnu:$(PATH)

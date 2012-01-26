NAME = libgoffice
VERSION = 0.7.4
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Document centric objects library
define BLURB
	GOffice is a library of document centric objects and utilities building on
	top of GLib and Gtk+.
endef

MASTER_SITES =  $(GNOME_ROOT)/goffice/$(GNOME_SUBV)/
DISTFILES  = goffice-$(VERSION).tar.gz
DISTNAME  = goffice-$(VERSION)

RUNTIME_DEP_PKGS += CSWgconf2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk
RUNTIME_DEP_PKGS += CSWlibcairo CSWlibglade2 CSWlibgsf CSWlibxml2 CSWlibxrender
RUNTIME_DEP_PKGS += CSWpango CSWsunmath CSWzlib
RUNTIME_DEP_PKGS += CSWbonobo2 CSWgnomekeyring CSWgnomevfs2 CSWlibart
RUNTIME_DEP_PKGS += CSWlibbonoboui CSWlibgnome CSWlibgnomecanvas CSWlibgnomeui
RUNTIME_DEP_PKGS += CSWlibpopt CSWorbit2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = goffice-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk

PATH :=/opt/csw/bin:/opt/csw/gnu:$(PATH)

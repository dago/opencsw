GARNAME = gnumeric
GARVERSION = 1.9.5
CATEGORIES = gnome

DESCRIPTION = GNOME spreadsheet program
define BLURB
 The project aims to become a drop in replacement for proprietary spreadsheets.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS += CSWbonobo2 CSWgconf2 CSWggettextrt CSWglib2 CSWgnomekeyring
REQUIRED_PKGS += CSWgnomevfs2 CSWgtk2 CSWlibart CSWlibatk CSWlibbonoboui
REQUIRED_PKGS += CSWlibcairo CSWlibglade2 CSWlibgnome CSWlibgnomecanvas
REQUIRED_PKGS += CSWlibgnomeui CSWlibgoffice CSWlibgsf CSWlibpopt CSWlibxml2
REQUIRED_PKGS += CSWorbit2 CSWpango CSWperl CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#PATCHFILES = mainpatch 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

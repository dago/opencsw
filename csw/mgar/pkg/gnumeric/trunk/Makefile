NAME = gnumeric
VERSION = 1.9.5
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GNOME spreadsheet program
define BLURB
 The project aims to become a drop in replacement for proprietary spreadsheets.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS += CSWbonobo2 CSWgconf2 CSWggettextrt CSWglib2 CSWgnomekeyring
RUNTIME_DEP_PKGS += CSWgnomevfs2 CSWgtk2 CSWlibart CSWlibatk CSWlibbonoboui
RUNTIME_DEP_PKGS += CSWlibcairo CSWlibglade2 CSWlibgnome CSWlibgnomecanvas
RUNTIME_DEP_PKGS += CSWlibgnomeui CSWlibgoffice CSWlibgsf CSWlibpopt CSWlibxml2
RUNTIME_DEP_PKGS += CSWorbit2 CSWpango CSWperl CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES  = md5.h.diff
PATCHFILES += numtheory.c.diff 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

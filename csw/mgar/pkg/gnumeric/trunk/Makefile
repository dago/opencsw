GARNAME = gnumeric
GARVERSION = 1.8.3
CATEGORIES = gnome

DESCRIPTION = Brief description
define BLURB
  Long description
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

PATCHFILES = mainpatch 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

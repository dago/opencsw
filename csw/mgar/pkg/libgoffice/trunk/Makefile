GARNAME = libgoffice
GARVERSION = 0.7.3
CATEGORIES = gnome

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = goffice-$(GARVERSION).tar.gz
DISTNAME  = goffice-$(GARVERSION)

REQUIRED_PKGS += CSWgconf2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk
REQUIRED_PKGS += CSWlibcairo CSWlibglade2 CSWlibgsf CSWlibxml2 CSWlibxrender
REQUIRED_PKGS += CSWpango CSWsunmath CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = goffice-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk

PATH :=/opt/csw/bin:/opt/csw/gnu:$(PATH)

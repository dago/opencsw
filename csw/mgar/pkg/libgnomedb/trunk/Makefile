GARNAME = libgnomedb
GARVERSION = 3.99.7
CATEGORIES = gnome

DESCRIPTION = The libgnomedb library
define BLURB
 libgnomedb provides data-bound UI widgets, using GTK+ and libgda.

 The libgnomedb library is released under the terms of the LGPL license,  which
 allows for commercial applications to be developed based on libgnomedb. The
 accompanying tools are under the GPL.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTNAME  = $(GARNAME)-$(GARVERSION)

#REQUIRED_PKGS += CSWgconf2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk
#REQUIRED_PKGS += CSWlibcairo CSWlibglade2 CSWlibgsf CSWlibxml2 CSWlibxrender
#REQUIRED_PKGS += CSWpango CSWsunmath CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

#TEST_TARGET =

include gar/category.mk

PATH :=/opt/csw/bin:/opt/csw/gnu:$(PATH)

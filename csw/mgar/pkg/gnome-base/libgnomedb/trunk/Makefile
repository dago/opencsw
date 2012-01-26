NAME = libgnomedb
VERSION = 3.99.7
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = The libgnomedb library
define BLURB
 libgnomedb provides data-bound UI widgets, using GTK+ and libgda.

 The libgnomedb library is released under the terms of the LGPL license,  which
 allows for commercial applications to be developed based on libgnomedb. The
 accompanying tools are under the GPL.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

#RUNTIME_DEP_PKGS += CSWgconf2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk
#RUNTIME_DEP_PKGS += CSWlibcairo CSWlibglade2 CSWlibgsf CSWlibxml2 CSWlibxrender
#RUNTIME_DEP_PKGS += CSWpango CSWsunmath CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

#TEST_TARGET =

include gar/category.mk

PATH :=/opt/csw/bin:/opt/csw/gnu:$(PATH)

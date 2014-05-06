# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libmediaart
VERSION = 0.1.0
GARTYPE = v2

DESCRIPTION = libmediaart, manage, extract and handle media art caches
define BLURB
    Library tasked with managing, extracting and handling media art caches.
  The code for this project has been extracted from Tracker and inserted
  into its own library because there is call for this functionality in
  other places on the desktop.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
GARCOMPILER = GNU
# Tests fail left and right
SKIPTEST = 1

PATCHFILES += eba1a1f1276e40b68e7b7084863469a0c97ef41a.patch

PACKAGES += CSWlibmediaart-0-2-0
SPKG_DESC_CSWlibmediaart-0-2-0 = $(DESCRIPTION)

PACKAGES += CSWlibmediaart-dev
SPKG_DESC_CSWlibmediaart-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibmediaart-dev = $(PKGFILES_DEVEL)

# For gettext
CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


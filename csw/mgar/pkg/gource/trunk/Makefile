NAME = gource
VERSION = 0.28
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Software version control visualization
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES  = 0001-Make-sure-we-have-a-prototype-for-sqrt.patch
PATCHFILES += 0002-Use-double-functions-and-proper-casts-in-lack-of-flo.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS += CSWlibsdl
DEP_PKGS += CSWpng
DEP_PKGS += CSWmesa
DEP_PKGS += CSWstlport
DEP_PKGS += CSWpcrert
DEP_PKGS += CSWftgl
DEP_PKGS += CSWsdlimage
DEP_PKGS += CSWglew
DEP_PKGS += CSWjpeg

EXTRA_CXXFLAGS = -library=stlport4
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

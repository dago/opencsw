GARNAME = freeglut
GARVERSION = 2.6.0
CATEGORIES = lib

DESCRIPTION = OpenSourced alternative to the OpenGL Utility Toolkit
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://freeglut.sourceforge.net/

DEP_PKGS = CSWmesa

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

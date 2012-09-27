# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tkimg
VERSION = 1.4
GARTYPE = v2
CATEGORIES = lang
LICENSE = license.terms
DEPENDS = CSWtcl
DISTNAME = $(NAME)$(VERSION)

DESCRIPTION = The "Img" package adds a lot of image formats to Tcl/Tk

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.bz2

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

LINKER_MAPS = 

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_SCRIPTS = custom

TEST_SCRIPTS = 

TEST_TARGET = 

install-custom:
	gmake -C $(WORKSRC) INSTALL_ROOT=$(DESTDIR) install
	$(MAKECOOKIE)

include gar/category.mk

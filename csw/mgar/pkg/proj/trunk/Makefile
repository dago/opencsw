# $Id$
NAME = proj
VERSION = 4.7.0
CATEGORIES = lib

GARTYPE = v2-defaultchange

DESCRIPTION = Cartographic Projections Library
define BLURB
The PROJ.4 Cartographic Projections library was originally written by Gerald Evenden then of the USGS.
endef

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += $(NAME)-datumgrid-1.5.zip

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated:
	@(cp $(FILEDIR)/libproj.so.0.4.2.$(GARCH) \
		$(DESTDIR)$(libdir)/libproj.so.0.4.2 )
	@$(MAKECOOKIE)

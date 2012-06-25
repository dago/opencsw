# $Id$

NAME = pstoedit
VERSION = 3.60
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Translates PostScript and PDF files to editable vector graphics converter
define BLURB
  translates PostScript and PDF graphics into other vector formats.
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.gz

BUILD_DEP_PKGS		+=	CSWimagemagick-dev
BUILD_DEP_PKGS		+=	CSWlibgd-dev
BUILD_DEP_PKGS		+=	CSWplotutils-dev

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-libplot
CONFIGURE_ARGS	+=	--without-emf
CONFIGURE_ARGS	+=	--without-swf

LICENSE			=	copying

include gar/category.mk

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

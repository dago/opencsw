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
BUILD_DEP_PKGS		+=	CSWbison

GARCOMPILER			=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-libplot
CONFIGURE_ARGS	+=	--without-emf
CONFIGURE_ARGS	+=	--without-swf

LICENSE			=	copying

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/php5/bin:$(PATH)

openmpList	=	\
				Makefile \
				config/Makefile \
				msdev/Makefile \
				misc/swffonts/Makefile \
				misc/Makefile \
				m4/Makefile \
				othersrc/gsdllinc/Makefile \
				othersrc/Makefile \
				contrib/java/java2/Makefile \
				contrib/java/Makefile \
				contrib/java/java1/Makefile \
				contrib/Makefile \
				contrib/cairo/Makefile \
				src/Makefile \
				examples/Makefile \
				doc/Makefile \
				os2/Makefile

post-configure-modulated:
	cd $(WORKSRC) && sed --in-place --expression='s/ -xopenmp//' $(openmpList)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

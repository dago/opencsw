# $Id$

NAME	=	libdvdcss
VERSION	=	1.2.13
GARTYPE	=	v2

DESCRIPTION	=	L

DESCRIPTION = library for accessing DVDs like a block device without having to bother 
define BLURB
	L

DESCRIPTION = library for accessing DVDs like a block device without having to bother endef

MASTER_SITES	=	http://download.videolan.org/pub/$(NAME)/$(VERSION)/
DISTFILES 		=	$(NAME)-$(VERSION).tar.bz2
PATCHFILES		+=	0001-fix-uscsi-detection.patch

GARCOMPILER		=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)

RUNTIME_DEP_PKGS_CSWlibdvdcss += CSWlibgcc-s1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	cd $(WORKSRC); autoreconf -fi
	@$(MAKECOOKIE)e
# $Id$

NAME			=	leocad
VERSION			=	0.79.3
PIECES_VERSION	=	7114
GARTYPE			=	v2

DESCRIPTION = Virtual Lego brick CAD software
define BLURB
  CAD program that allows people to build virtual models using bricks similar
  to those found in LEGO toys
endef

MASTER_SITES	=	$(GOOGLE_MIRROR)
DISTNAME		=	$(NAME)
DISTFILES		=	$(NAME)-$(VERSION)-src.tgz
DISTFILES		+=	pieces-$(PIECES_VERSION).zip
# this raises "warning: 1 line adds whitespace errors"; choosed to ignore
PATCHFILES		+=	0001-Use-POSIX-to-determine-the-file-type.patch

GARCOMPILER			=	GNU

CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_SCRIPTS	=	custom

BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibgtk2-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev
BUILD_DEP_PKGS		+=	CSWlibjpeg-dev
BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	CSWmesa

TEST_SCRIPTS		=

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

configure-custom:
	cd $(WORKSRC) && $(MAKE) config PREFIX=$(prefix)
	$(MAKECOOKIE)

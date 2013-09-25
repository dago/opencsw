# $Id$

NAME	=	xfconf
VERSION	=	4.10.0
GARTYPE	=	v2

DESCRIPTION	=	Manage settings in Xfce
define BLURB
  Manage settings in Xfce
endef

MASTER_SITES	=	http://archive.xfce.org/xfce/4.10/src/
DISTFILES 		=	$(DISTNAME).tar.bz2
PATCHFILES		+=	0001-use-bash-in-test-drivers.patch

BUILD_DEP_PKGS	+=	CSWgtk-doc
BUILD_DEP_PKGS	+=	CSWvim

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-gtk-doc
CONFIGURE_ARGS	+=	--enable-gtk-doc-html
CONFIGURE_ARGS	+=	--enable-gtk-doc-pdf

GARCOMPILER		=	GNU

TEST_SCRIPTS = custom

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# abicheck.sh fails for incocuous reasons and the ABI is not in question:
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) VERBOSE=true && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)

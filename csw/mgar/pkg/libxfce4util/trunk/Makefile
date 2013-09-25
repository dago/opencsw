# $Id$

NAME	=	libxfce4util
VERSION	=	4.10.0
GARTYPE	=	v2

DESCRIPTION	=	Basic utility library for Xfce4
define BLURB
  Basic utility library for Xfce4.
endef

MASTER_SITES	=	http://archive.xfce.org/xfce/4.10/src/
DISTFILES 		=	$(DISTNAME).tar.bz2

BUILD_DEP_PKGS	+=	CSWgtk-doc
BUILD_DEP_PKGS	+=	CSWvim

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-gtk-doc
CONFIGURE_ARGS	+=	--enable-gtk-doc-html
CONFIGURE_ARGS	+=	--enable-gtk-doc-pdf

GARCOMPILER		=	GNU

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

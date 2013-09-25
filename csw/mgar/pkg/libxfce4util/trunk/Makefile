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
PATCHFILES		+=	0001-search-fallback-for-pixmaps.patch

BUILD_DEP_PKGS	+=	CSWgtk-doc
BUILD_DEP_PKGS	+=	CSWvim

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-gtk-doc
CONFIGURE_ARGS	+=	--enable-gtk-doc-html
CONFIGURE_ARGS	+=	--enable-gtk-doc-pdf

GARCOMPILER		=	GNU

PACKAGES							+=	CSWlibxfce4util
CATALOGNAME_CSWlibxfce4util			=	libxfce4util
SPKG_DESC_CSWlibxfce4util			+=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWlibxfce4util	+=	CSWlibxfce4util6

PACKAGES							+=	CSWlibxfce4util6
CATALOGNAME_CSWlibxfce4util6		=	libxfce4util6
PKGFILES_CSWlibxfce4util6			+=	$(call baseisadirs,$(libdir),libxfce4util\.so\.6\.0\.0)
PKGFILES_CSWlibxfce4util6			+=	$(call baseisadirs,$(libdir),libxfce4util\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibxfce4util6			+=	$(DESCRIPTION), libxfce4util.so.6
RUNTIME_DEP_PKGS_CSWlibxfce4util6	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibxfce4util6	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibxfce4util6	+=	CSWlibglib2-0-0
CHECKPKG_OVERRIDES_CSWlibxfce4util6	+=	file-with-bad-content|/usr/local|root/opt/csw/lib/libxfce4util.so.6.0.0
CHECKPKG_OVERRIDES_CSWlibxfce4util6	+=	file-with-bad-content|/usr/share|root/opt/csw/lib/libxfce4util.so.6.0.0

PACKAGES								+=	CSWlibxfce4util-dev
CATALOGNAME_CSWlibxfce4util-dev			=	libxfce4util_dev
SPKG_DESC_CSWlibxfce4util-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWlibxfce4util-dev			+=	/opt/csw/lib/libxfce4util.so
PKGFILES_CSWlibxfce4util-dev			+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibxfce4util-dev	+=	CSWlibxfce4util6
ARCHALL_CSWlibxfce4util-dev				=	1
CHECKPKG_OVERRIDES_CSWlibxfce4util-dev	+=	archall-devel-package

PACKAGES						+=	CSWlibxfce4util-doc
CATALOGNAME_CSWlibxfce4util-doc	=	libxfce4util_doc
SPKG_DESC_CSWlibxfce4util-doc	+=	$(DESCRIPTION), documentation
PKGFILES_CSWlibxfce4util-doc	+=	$(datadir)/gtk-doc/.*
ARCHALL_CSWlibxfce4util-doc		=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

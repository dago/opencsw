# $Id$

NAME	=	exo
VERSION	=	0.8.0
GARTYPE	=	v2

DESCRIPTION	=	An extension library to Xfce
define BLURB
  An extension library to Xfce, developed by os-cillation. While Xfce
  comes with quite a few libraries that are targeted at desktop
  development, libexo is targeted at application development.
endef

MASTER_SITES	=	http://archive.xfce.org/xfce/4.10/src/
DISTFILES 		=	$(DISTNAME).tar.bz2

BUILD_DEP_PKGS	+=	CSWgtk-doc
BUILD_DEP_PKGS	+=	CSWvim
BUILD_DEP_PKGS	+=	CSWlibxfce4util-dev
BUILD_DEP_PKGS	+=	CSWlibxfce4ui-dev

CONFIGURE_ARGS	=	$(DIRPATHS)

GARCOMPILER		=	GNU

PACKAGES				+=	CSWexo
CATALOGNAME_CSWexo		=	exo
SPKG_DESC_CSWexo		+=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWexo	+=	CSWlibexo1-0

PACKAGES						+=	CSWlibexo1-0
CATALOGNAME_CSWlibexo1-0		=	libexo1_0
PKGFILES_CSWlibexo1-0			+=	$(call baseisadirs,$(libdir),libexo-1\.so\.0\.0\.0)
PKGFILES_CSWlibexo1-0			+=	$(call baseisadirs,$(libdir),libexo-1\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibexo1-0			+=	$(DESCRIPTION), libexo-1.so.0
RUNTIME_DEP_PKGS_CSWlibexo1-0	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibexo1-0	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibexo1-0	+=	CSWlibglib2-0-0

PACKAGES						+=	CSWexo-dev
CATALOGNAME_CSWexo-dev			=	exo_dev
SPKG_DESC_CSWexo-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWexo-dev				+=	/opt/csw/lib/libexo-1.so
PKGFILES_CSWexo-dev				+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWexo-dev		+=	CSWlibexo1-0
ARCHALL_CSWexo-dev				=	1
CHECKPKG_OVERRIDES_CSWexo-dev	+=	archall-devel-package

PACKAGES					+=	CSWexo-doc
CATALOGNAME_CSWexo-doc	=	exo_doc
SPKG_DESC_CSWexo-doc	+=	$(DESCRIPTION), documentation
PKGFILES_CSWexo-doc		+=	$(datadir)/gtk-doc/.*
ARCHALL_CSWexo-doc		=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

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
BUILD_DEP_PKGS	+=	CSWlibxfce4util-dev

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-gtk-doc
CONFIGURE_ARGS	+=	--enable-gtk-doc-html
CONFIGURE_ARGS	+=	--enable-gtk-doc-pdf

GARCOMPILER		=	GNU

TEST_SCRIPTS = custom

PACKAGES						+=	CSWxfconf
CATALOGNAME_CSWxfconf			=	xfconf
SPKG_DESC_CSWxfconf				+=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWxfconf		+=	CSWlibxfconf0-2

PACKAGES							+=	CSWlibxfconf0-2
CATALOGNAME_CSWlibxfconf0-2			=	libxfconf0_2
PKGFILES_CSWlibxfconf0-2			+=	$(call baseisadirs,$(libdir),libxfconf-0\.so\.2\.0\.0)
PKGFILES_CSWlibxfconf0-2			+=	$(call baseisadirs,$(libdir),libxfconf-0\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibxfconf0-2			+=	$(DESCRIPTION), libxfconf-0.so.2
RUNTIME_DEP_PKGS_CSWlibxfconf0-2	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibxfconf0-2	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibxfconf0-2	+=	CSWlibglib2-0-0

PACKAGES							+=	CSWxfconf-dev
CATALOGNAME_CSWxfconf-dev			=	xfconf_dev
SPKG_DESC_CSWxfconf-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWxfconf-dev				+=	/opt/csw/lib/libxfconf-0.so
PKGFILES_CSWxfconf-dev				+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWxfconf-dev		+=	CSWlibxfconf0-2
ARCHALL_CSWxfconf-dev				=	1
CHECKPKG_OVERRIDES_CSWxfconf-dev	+=	archall-devel-package

PACKAGES					+=	CSWxfconf-doc
CATALOGNAME_CSWxfconf-doc	=	xfconf_doc
SPKG_DESC_CSWxfconf-doc	+=	$(DESCRIPTION), documentation
PKGFILES_CSWxfconf-doc		+=	$(datadir)/gtk-doc/.*
ARCHALL_CSWxfconf-doc		=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# abicheck.sh fails for incocuous reasons and the ABI is not in question:
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) VERBOSE=true && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)

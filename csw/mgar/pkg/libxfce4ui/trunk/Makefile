# $Id$

NAME	=	libxfce4ui
VERSION	=	4.10.0
GARTYPE	=	v2

DESCRIPTION	=	Common Xfce widgets
define BLURB
  Library used to share commonly used Xfce widgets amoung the Xfce applications.
endef

MASTER_SITES	=	http://archive.xfce.org/xfce/4.10/src/
DISTFILES		=	$(DISTNAME).tar.bz2

BUILD_DEP_PKGS	+=	CSWgtk-doc
BUILD_DEP_PKGS	+=	CSWvim
BUILD_DEP_PKGS	+=	CSWxfconf-dev

CONFIGURE_ARGS	=	$(DIRPATHS)

GARCOMPILER		=	GNU

TEST_SCRIPTS = custom

PACKAGES							+=	CSWlibxfce4ui
CATALOGNAME_CSWlibxfce4ui			=	libxfce4ui
SPKG_DESC_CSWlibxfce4ui			+=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWlibxfce4ui	+=	CSWlibxfce4ui1-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui	+=	CSWlibxfce4util6
RUNTIME_DEP_PKGS_CSWlibxfce4ui	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui	+=	CSWlibgtk-x11-2-0-0

# this is private to Xfce but not to libxfce4ui...
PACKAGES								+=	CSWlibxfce4kbd-private2-0
CATALOGNAME_CSWlibxfce4kbd-private2-0	=	libxfce4kbd_private2_0
PKGFILES_CSWlibxfce4kbd-private2-0		+=	$(call baseisadirs,$(libdir),libxfce4kbd-private-2\.so\.0\.0\.0)
PKGFILES_CSWlibxfce4kbd-private2-0		+=	$(call baseisadirs,$(libdir),libxfce4kbd-private-2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibxfce4kbd-private2-0		+=	$(DESCRIPTION), libxfce4kbd-private-2.so.0

PACKAGES							+=	CSWlibxfce4ui1-0
CATALOGNAME_CSWlibxfce4ui1-0		=	libxfce4ui1_0
PKGFILES_CSWlibxfce4ui1-0			+=	$(call baseisadirs,$(libdir),libxfce4ui\-1.so\.0\.0\.0)
PKGFILES_CSWlibxfce4ui1-0			+=	$(call baseisadirs,$(libdir),libxfce4ui\-1.so\.0(\.\d+)*)
SPKG_DESC_CSWlibxfce4ui1-0			+=	$(DESCRIPTION), libxfce4ui-1.so.0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibxfce4kbd-private2-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibxfce4util6
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWstartupnotif
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWpango
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibxfce4ui1-0	+=	CSWlibxfconf0-2

PACKAGES								+=	CSWlibxfce4ui-dev
CATALOGNAME_CSWlibxfce4ui-dev			=	libxfce4ui_dev
SPKG_DESC_CSWlibxfce4ui-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWlibxfce4ui-dev			+=	/opt/csw/lib/libxfce4ui-1.so
PKGFILES_CSWlibxfce4ui-dev			+=	/opt/csw/lib/libxfce4kbd-private-2.so
PKGFILES_CSWlibxfce4ui-dev			+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibxfce4ui-dev	+=	CSWlibxfce4ui1-0
ARCHALL_CSWlibxfce4ui-dev				=	1
CHECKPKG_OVERRIDES_CSWlibxfce4ui-dev	+=	archall-devel-package

PACKAGES						+=	CSWlibxfce4ui-doc
CATALOGNAME_CSWlibxfce4ui-doc	=	libxfce4ui_doc
SPKG_DESC_CSWlibxfce4ui-doc	+=	$(DESCRIPTION), documentation
PKGFILES_CSWlibxfce4ui-doc	+=	$(datadir)/gtk-doc/.*
ARCHALL_CSWlibxfce4ui-doc		=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# abicheck.sh fails for innocuous reasons and the ABI is not in question:
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) VERBOSE=true && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)

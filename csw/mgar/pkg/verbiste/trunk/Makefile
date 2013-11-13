# $Id$

NAME	=	verbiste
VERSION	=	0.1.40
GARTYPE	=	v2

DESCRIPTION	=	French conjugation system
define BLURB
  Système de conjugaison française.
endef

MASTER_SITES	=	http://perso.b2b2c.ca/sarrazip/dev/
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-fix-locale.patch

BUILD_DEP_PKGS	+=	CSWlibglib2-dev
BUILD_DEP_PKGS	+=	CSWlibgtk2-dev
BUILD_DEP_PKGS	+=	CSWlibcairo-dev
BUILD_DEP_PKGS	+=	CSWlibpango-dev
BUILD_DEP_PKGS	+=	CSWlibgdk-pixbuf-dev
BUILD_DEP_PKGS	+=	CSWlibatk-dev
BUILD_DEP_PKGS	+=	CSWlibgnomeui-devel
BUILD_DEP_PKGS	+=	CSWlibbonobo2
BUILD_DEP_PKGS	+=	CSWlibbonoboui
BUILD_DEP_PKGS	+=	CSWlibgnomecanvas-dev
BUILD_DEP_PKGS	+=	CSWlibart
BUILD_DEP_PKGS	+=	CSWlibgnome-dev
BUILD_DEP_PKGS	+=	CSWgnomevfs2-dev
BUILD_DEP_PKGS	+=	CSWorbit2
BUILD_DEP_PKGS	+=	CSWlibfreetype-dev

GARCOMPILER		=	GNU
GARFLAVOR		=	DBG

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-gtk-app
CONFIGURE_ARGS	+=	--with-gnome-app
CONFIGURE_ARGS	+=	--with-console-app

EXTRA_CXXFLAGS	+=	-I${includedir}/glib-2.0
EXTRA_CXXFLAGS	+=	-I${libdir}/glib-2.0/include
EXTRA_CXXFLAGS	+=	-I${includedir}/gtk-2.0
EXTRA_CXXFLAGS	+=	-I${libdir}/gtk-2.0/include
EXTRA_CXXFLAGS	+=	-I${includedir}/cairo
EXTRA_CXXFLAGS	+=	-I${includedir}/pango-1.0
EXTRA_CXXFLAGS	+=	-I${includedir}/gdk-pixbuf-2.0
EXTRA_CXXFLAGS	+=	-I${includedir}/atk-1.0
EXTRA_CXXFLAGS	+=	-I${includedir}/libgnomeui-2.0
EXTRA_CXXFLAGS	+=	-I${includedir}/libbonobo-2.0
EXTRA_CXXFLAGS	+=	-I${includedir}/libbonoboui-2.0
EXTRA_CXXFLAGS	+=	-I${includedir}/libgnomecanvas-2.0
EXTRA_CXXFLAGS	+=	-I${includedir}/libart-2.0
EXTRA_CXXFLAGS	+=	-I${includedir}/libgnome-2.0
EXTRA_CXXFLAGS	+=	-I${includedir}/gnome-vfs-2.0

EXTRA_LDFLAGS	=	-lintl

PACKAGES						+=	CSWverbiste
CATALOGNAME_CSWverbiste			=	verbiste
SPKG_DESC_CSWverbiste			=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgnomeui2-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibpopt0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWlibverbiste0-1-0
RUNTIME_DEP_PKGS_CSWverbiste	+=	CSWorbit2
CHECKPKG_OVERRIDES_CSWverbiste	+=	surplus-dependency|CSWlibatk1-0-0
CHECKPKG_OVERRIDES_CSWverbiste	+=	surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWverbiste	+=	surplus-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWverbiste	+=	surplus-dependency|CSWorbit2
CHECKPKG_OVERRIDES_CSWverbiste	+=	surplus-dependency|CSWlibpango1-0-0

PACKAGES								+=	CSWlibverbiste0-1-0
CATALOGNAME_CSWlibverbiste0-1-0			=	libverbiste0_1_0
PKGFILES_CSWlibverbiste0-1-0			+=	$(call baseisadirs,$(libdir),libverbiste-0\.1\.so\.0\.0\.0)
PKGFILES_CSWlibverbiste0-1-0			+=	$(call baseisadirs,$(libdir),libverbiste-0\.1\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibverbiste0-1-0			+=	$(DESCRIPTION), libverbiste-0.1.so.0
RUNTIME_DEP_PKGS_CSWlibverbiste0-1-0	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibverbiste0-1-0	+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibverbiste0-1-0	+=	CSWlibxml2-2

PACKAGES							+=	CSWverbiste-dev
CATALOGNAME_CSWverbiste-dev			=	verbiste_dev
SPKG_DESC_CSWverbiste-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWverbiste-dev			+=	/opt/csw/lib/libverbiste-0.1.so
PKGFILES_CSWverbiste-dev			+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWverbiste-dev	+=	CSWlibverbiste0-1-0
CHECKPKG_OVERRIDES_CSWverbiste-dev	+=	surplus-dependency|CSWlibverbiste0-1-0
ARCHALL_CSWverbiste-dev				=	1
CHECKPKG_OVERRIDES_CSWverbiste-dev	+=	archall-devel-package
include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	cd $(WORKSRC); autoreconf -fi
	@$(MAKECOOKIE)

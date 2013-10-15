# $Id$

NAME	=	libdvdnav
VERSION	=	4.2.0
GARTYPE	=	v2

DESCRIPTION = Library that allows easy use of sophisticated DVD navigation
define BLURB
	libdvdnav is a library that allows easy use of sophisticated DVD
	navigation features such as DVD menus, multiangle playback and
	even interactive DVD games.
endef

GITHUB_USER		=	microe
GITHUB_REFERENCE=	73a49e6
MASTER_SITES	=	$(GITHUB_MIRROR)
VENDOR_URL		=	http://dvdnav.mplayerhq.hu/
DISTNAME		=	$(GITHUB_USER)-$(NAME)-$(GITHUB_REFERENCE)
DISTFILES		=	$(NAME)-$(VERSION)$(GITHUB_BALL_EXT)

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

GARCOMPILER		=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)

BUILD_DEP_PKGS	+=	CSWlibdvdread-dev

PACKAGES						=	CSWlibdvdnav4
PKGFILES_CSWlibdvdnav4			+=	$(call baseisadirs,$(libdir),libdvdnav\.so\.4(\.\d+)*)
PKGFILES_CSWlibdvdnav4			+=	$(call baseisadirs,$(libdir),libdvdnav\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibdvdnav4			+=	$(DESCRIPTION), libdvdnav.so.4
RUNTIME_DEP_PKGS_CSWlibdvdnav4	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdvdnav4	+=	CSWlibdvdread4

PACKAGES							+=	CSWlibdvdnavmini4
PKGFILES_CSWlibdvdnavmini4			+=	$(call baseisadirs,$(libdir),libdvdnavmini\.so\.4(\.\d+)*)
PKGFILES_CSWlibdvdnavmini4			+=	$(call baseisadirs,$(libdir),libdvdnavmini\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibdvdnavmini4			+=	$(DESCRIPTION), libdvdnavmini.so.4
RUNTIME_DEP_PKGS_CSWlibdvdnavmini4	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdvdnavmini4	+=	CSWlibdvdread4

PACKAGES							+=	CSWlibdvdnav-dev
SPKG_DESC_CSWlibdvdnav-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWlibdvdnav-dev			+=	$(PKGFILES_DEVEL)
PKGFILES_CSWlibdvdnav-dev			+=	/opt/csw/lib/libdvdnav.so
RUNTIME_DEP_PKGS_CSWlibdvdnav-dev	+=	CSWlibdvdnav4
RUNTIME_DEP_PKGS_CSWlibdvdnav-dev	+=	CSWlibdvdnavmini4

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	cd $(WORKSRC); autoreconf -fi
	@$(MAKECOOKIE)

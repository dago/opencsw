# $Id$

NAME = libdvdread
VERSION = 4.2.0
GARTYPE = v2

DESCRIPTION = Library for reading DVD-Video images
define BLURB
	libdvdread currently uses libdl to dynamically probe for libdvdcss at
	runtime.  If libdvdcss is found, then it will be used to decrypt the
	encrypted sections of a DVD.
endef

GITHUB_USER		=	microe
GITHUB_REFERENCE=	3762e09
MASTER_SITES	=	$(GITHUB_MIRROR)
VENDOR_URL		=	http://dvdnav.mplayerhq.hu/
DISTNAME		=	$(GITHUB_USER)-$(NAME)-$(GITHUB_REFERENCE)
DISTFILES		=	$(NAME)-$(VERSION)$(GITHUB_BALL_EXT)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

GARCOMPILER = GNU

PACKAGES =

PACKAGES += CSWlibdvdread4
PKGFILES_CSWlibdvdread4 += $(call baseisadirs,$(libdir),libdvdread\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibdvdread4 += $(DESCRIPTION), libdvdread.so.4
RUNTIME_DEP_PKGS_CSWlibdvdread4 += CSWlibgcc-s1

PACKAGES += CSWlibdvdread-dev
SPKG_DESC_CSWlibdvdread-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibdvdread-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibdvdread-dev += CSWlibdvdread4

OBSOLETED_BY_CSWlibdvdread4 = CSWlibdvdread
OBSOLETED_BY_CSWlibdvdread-dev = CSWlibdvdreaddevel

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC); autoreconf -fi
	@$(MAKECOOKIE)

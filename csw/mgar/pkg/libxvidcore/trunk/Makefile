# $Id$

NAME = libxvidcore
VERSION = 1.3.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A high performance and high quality MPEG-4 video de-/encoding solution
define BLURB
  A high performance and high quality MPEG-4 video de-/encoding solution
endef

DISTNAME		=	xvidcore
MASTER_SITES	=	http://downloads.xvid.org/downloads/
DISTFILES  		=	$(DISTNAME)-$(VERSION).tar.gz
PATCHFILES		+=	0001-Adapt-examples-build-and-bench.patch
PATCHFILES		+=	0002-Map-instead-of-version.patch
PATCHFILES		+=	0003-Generic-linker-soname-argument.patch

LICENSE			=	LICENSE
GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--disable-assembly

RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1 

CONFIGURE_SCRIPTS	=	custom
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS	=
INSTALL_SCRIPTS		=	custom

PACKAGES						+=	CSWlibxvidcore4
CATALOGNAME_CSWlibxvidcore4 	=	libxvidcore4
PKGFILES_CSWlibxvidcore4		+=	$(call baseisadirs,$(libdir),libxvidcore\.so\.4\.3)
PKGFILES_CSWlibxvidcore4		+=	$(call baseisadirs,$(libdir),libxvidcore\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibxvidcore4		+=	$(DESCRIPTION), libxvidcore.so.4
RUNTIME_DEP_PKGS_CSWlibxvidcore	+=	CSWlibxvidcore4
OBSOLETED_BY_CSWlibxvidcore4	=	CSWlibxvidcore
CATALOGNAME_CSWlibxvidcore		=	libxvidcore_stub

PACKAGES						+=	CSWlibxvidcore-dev
CATALOGNAME_CSWlibxvidcore-dev	=	libxvidcore_dev
SPKG_DESC_CSWlibxvidcore-dev	+=	$(DESCRIPTION), development files
PKGFILES_CSWlibxvidcore-dev		+=	/opt/csw/lib/libxvidcore.4.so
PKGFILES_CSWlibxvidcore-dev		+=	$(PKGFILES_DEVEL)
OBSOLETED_BY_CSWlibxvidcore-dev	=	CSWlibxvidcoredevel
CATALOGNAME_CSWlibxvidcore-dev	=	libxvidcore_devel_stub
ARCHALL_CSWlibxvidcore-dev		=	1
CHECKPKG_OVERRIDES_CSWlibxvidcore-dev += archall-devel-package

include gar/category.mk

configure-custom:
	cd $(WORKSRC)/build/generic && ./configure $(CONFIGURE_ARGS)
	$(MAKECOOKIE)

build-custom:
	mgar --directory $(WORKSRC)/build/generic
	$(MAKECOOKIE)

install-custom:
	mgar DESTDIR=$(DESTDIR) --directory $(WORKSRC)/build/generic install
	$(MAKECOOKIE)

post-install-modulated:
	cd $(DESTDIR)/$(libdir) && ln -s libxvidcore.4.3.so libxvidcore.4.so
	cd $(DESTDIR)/$(libdir) && ln -s libxvidcore.4.so libxvidcore.so
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

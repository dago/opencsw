# $Id$

NAME = libxvidcore
VERSION = 1.3.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A high performance and high quality MPEG-4 video de-/encoding solution
define BLURB
  A high performance and high quality MPEG-4 video de-/encoding solution
endef

shortName		=	xvidcore
WORKSRC			=	$(WORKDIR)/$(shortName)/build/generic
PATCHDIR		=	$(WORKDIR)/$(shortName)
MASTER_SITES	=	http://downloads.xvid.org/downloads/
DISTFILES  		=	$(shortName)-$(VERSION).tar.gz
PATCHFILES		+=	0001-Adapt-examples-build-and-bench.patch
PATCHFILES		+=	0002-Map-instead-of-version.patch
PATCHFILES		+=	0003-Generic-linker-soname-argument.patch

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--disable-assembly

TEST_SCRIPTS	=

RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1 

include gar/category.mk

post-install-modulated:
	cd $(DESTDIR)/$(libdir) && ln -s libxvidcore.4.3.so libxvidcore.4.so
	cd $(DESTDIR)/$(libdir) && ln -s libxvidcore.4.so libxvidcore.so
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

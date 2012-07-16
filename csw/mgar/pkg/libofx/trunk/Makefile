# $Id$

NAME = libofx
VERSION = 0.9.5
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Library designed to allow applications to very easily support OFX command responses
define BLURB
  A parser and an API designed to allow applications to very easily
  support OFX command responses, usually provided by financial
  institutions for statement downloads.
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-Permissive-cast.patch

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-opensp-includes=$(includedir)/OpenSP
CONFIGURE_ARGS	+=	--with-opensp-libs=$(libdir)

BUILD_DEP_PKGS	+=	CSWopensp-dev
BUILD_DEP_PKGS	+=	CSWlibxml2-dev
BUILD_DEP_PKGS	+=	CSWgengetopt
BUILD_DEP_PKGS	+=	CSWlibiconv-dev
BUILD_DEP_PKGS	+=	CSWlibcurl-dev
BUILD_DEP_PKGS	+=	CSWhelp2man
BUILD_DEP_PKGS	+=	CSWgawk
BUILD_DEP_PKGS	+=	CSWlibgnugetopt-dev

EXTRA_LINKER_FLAGS	=	-lgnugetopt

RUNTIME_DEP_PKGS	+=	CSWlibosp5

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	@echo "executing $@"
	cd $(WORKSRC) && libtoolize
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && automake -a
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done

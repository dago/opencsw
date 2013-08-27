# $Id$

NAME			=	sip
VERSION			=	4.14.7
CATEGORIES		=	python
PYTHON_VERSION	=	2_7
GARTYPE			=	v2

DESCRIPTION	=	Tool for creating Python bindings for C and C++
define BLURB
  SIP is a tool that makes it very easy to create Python bindings for
  C and C++ libraries. It was originally developed to create PyQt,
  the Python bindings for the Qt toolkit, but can be used to create
  bindings for any C or C++ library.
endef

MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJECT		=	pyqt
SPKG_SOURCEURL	=	$(MASTER_SITES)
DISTFILES 		=	$(DISTNAME).tar.gz

LICENSE			=	LICENSE-GPL3

GARCOMPILER			=	GNU
CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_SCRIPTS	=	custom

BUILD_DEP_PKGS	+=	CSWpython-dev
BUILD_DEP_PKGS	+=	CSWpython27-dev

BUILD_SCRIPTS	=	custom

TEST_SCRIPTS	=

INSTALL_SCRIPTS	=	custom

RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

configure-custom:
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			bash -c '$(PYTHON_EXECUTABLE) configure.py \
				--platform=solaris-g++ \
				CC="$${CC}" \
				CFLAGS="$${CFLAGS}" \
				CXX="$${CXX}" \
				CXXFLAGS="$${CXXFLAGS}" \
				INCDIR="$${includedir}" \
				'
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(BUILD_ENV) \
			$(MAKE)
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(INSTALL_ENV) \
			$(MAKE) install
	@$(MAKECOOKIE)

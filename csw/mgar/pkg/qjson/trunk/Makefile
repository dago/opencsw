# $Id$

NAME = qjson
VERSION = 1.0.0
GARTYPE = v2

DESCRIPTION = Qt-based library that maps JSON data to QVariant objects
define BLURB
  QJson is a Qt-based library that maps JSON data to QVariant objects:
  JSON arrays will be mapped to QVariantList instances, while JSON
  objects will be mapped to QVariantMap.
endef

GITHUB_USER		=	flavio
GITHUB_REFERENCE=	1_0_0
MASTER_SITES	=	$(GITHUB_MIRROR)
VENDOR_URL		=	http://qjson.sourceforge.net/
DISTNAME		=	$(GITHUB_USER)-$(NAME)-101a7c5
DISTFILES		=	$(NAME)-$(VERSION)$(GITHUB_BALL_EXT)
PATCHFILES		+=	0001-Inhibit-GUI-for-tests.patch

BUILD_DEP_PKGS	+=	CSWcmake
BUILD_DEP_PKGS	+=	CSWqt4-dev

GARCOMPILER			=	GNU
CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_SCRIPTS	=	custom

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS	+=	-DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS	+=	-DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS	+=	-DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS	+=	-DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS	+=	-DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS	+=	"-DCMAKE_C_FLAGS=$(CFLAGS)"
CMAKE_ARGS	+=	"-DCMAKE_CXX_FLAGS=$(CXXFLAGS)"
CMAKE_ARGS	+=	-DCMAKE_VERBOSE_MAKEFILE=ON
CMAKE_ARGS	+=	-DQJSON_BUILD_TESTS=yes

TEST_SCRIPTS	=	custom

PACKAGES						+=	CSWlibqjson1
CATALOGNAME_CSWlibqjson1		=	libqjson1
PKGFILES_CSWlibqjson1			+=	$(call baseisadirs,$(libdir),libqjson\.so\.1\.0\.0)
PKGFILES_CSWlibqjson1			+=	$(call baseisadirs,$(libdir),libqjson\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibqjson1			+=	$(DESCRIPTION), libqjson.so.1
RUNTIME_DEP_PKGS_CSWlibqjson1	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibqjson1	+=	CSWlibqtcore4

PACKAGES						+=	CSWqjson-dev
CATALOGNAME_CSWqjson-dev		=	qjson_dev
SPKG_DESC_CSWqjson-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWqjson-dev			+=	/opt/csw/lib/libqjson.so
PKGFILES_CSWqjson-dev			+=	$(PKGFILES_DEVEL)
PKGFILES_CSWqjson-dev			+=	/opt/csw/lib/cmake/qjson/.*
RUNTIME_DEP_PKGS_CSWqjson-dev	+=	CSWlibqjson1
ARCHALL_CSWqjson-dev			=	1
CHECKPKG_OVERRIDES_CSWqjson-dev	+=	archall-devel-package

include gar/category.mk

configure-custom:
	(cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)

test-custom:
	(cd $(WORKSRC)/tests && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			$(MAKE) test)
	@$(MAKECOOKIE)

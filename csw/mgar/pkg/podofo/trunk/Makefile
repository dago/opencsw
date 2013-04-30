# $Id$

NAME	=	podofo
VERSION	=	0.9.2
GARTYPE	=	v2

DESCRIPTION	=	A library to work with the PDF file format
define BLURB
  The PoDoFo library is a free, portable C++ library which includes
  classes to parse PDF files and modify their contents into
  memory. The changes can be written back to disk easily. The parser
  can also be used to extract information from a PDF file (for example
  the parser could be used in a PDF viewer). Besides parsing PoDoFo
  includes also very simple classes to create your own PDF files. All
  classes are documented so it is easy to start writing your own
  application using PoDoFo.
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-replace-deprecated-LUA-API-calls.patch
PATCHFILES		+=	0002-Build-with-install-RPATH.patch

BUILD_DEP_PKGS	+=	CSWcmake
BUILD_DEP_PKGS	+=	CSWlua-dev

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
CMAKE_ARGS	+=	-DPODOFO_BUILD_SHARED:BOOL=TRUE
CMAKE_ARGS	+=	-DPODOFO_BUILD_STATIC:BOOL=FALSE

TEST_SCRIPTS	=	custom

PACKAGES								+=	CSWlibpodofo-utils
CATALOGNAME_CSWlibpodofo-utils			=	libpodofo_utils
SPKG_DESC_CSWlibpodofo-utils			+=	$(DESCRIPTION), utilities
RUNTIME_DEP_PKGS_CSWlibpodofo-utils		+=	CSWlibpodofo0-9-1
RUNTIME_DEP_PKGS_CSWlibpodofo-utils		+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibpodofo-utils		+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibpodofo-utils		+=	CSWliblua5-2
CHECKPKG_OVERRIDES_CSWlibpodofo-utils	+=	surplus-dependency|CSWlibpodofo0-9-1

PACKAGES							+=	CSWlibpodofo0-9-1
CATALOGNAME_CSWlibpodofo0-9-1		=	libpodofo0_9_1
PKGFILES_CSWlibpodofo0-9-1			+=	$(call baseisadirs,$(libdir),libpodofo\.so\.0\.9\.1)
PKGFILES_CSWlibpodofo0-9-1			+=	$(call baseisadirs,$(libdir),libpodofo\.so\.0\.9\.1(\.\d+)*)
SPKG_DESC_CSWlibpodofo0-9-1			+=	$(DESCRIPTION), libpodofo.so.0.9.1
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibpodofo0-9-1	+=	CSWlibgcc-s1

PACKAGES							+=	CSWlibpodofo-dev
CATALOGNAME_CSWlibpodofo-dev		=	libpodofo_dev
SPKG_DESC_CSWlibpodofo-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWlibpodofo-dev			+=	/opt/csw/lib/libpodofo.so
PKGFILES_CSWlibpodofo-dev			+=	$(PKGFILES_DEVEL)
ARCHALL_CSWlibpodofo-dev			=	1
RUNTIME_DEP_PKGS_CSWlibpodofo-dev	+=	CSWlibpodofo0-9-1
CHECKPKG_OVERRIDES_CSWlibpodofo-dev	+=	archall-devel-package

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
	(cd $(WORKSRC)/test && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			$(MAKE))
	@$(MAKECOOKIE)

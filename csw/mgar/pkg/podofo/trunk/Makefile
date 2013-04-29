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

BUILD_DEP_PKGS	+=	CSWcmake
BUILD_DEP_PKGS	+=	CSWlua-dev

GARCOMPILER			=	GNU
CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_SCRIPTS	=	custom

# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS	+=	-DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS	+=	-DINSTALL_LAYOUT=RPM
CMAKE_ARGS	+=	-DMYSQL_DATADIR=$(localstatedir)
CMAKE_ARGS	+=	-DSYSCONFDIR=$(sysconfdir)
CMAKE_ARGS	+=	-DINSTALL_BINDIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS	+=	-DINSTALL_SBINDIR=$(subst $(prefix)/,,$(libexecdir))
# CMAKE_ARGS	+=	-DINSTALL_MANDIR=$(subst $(prefix)/,,$(mandir))
CMAKE_ARGS	+=	-DINSTALL_LIBDIR=$(subst $(prefix)/,,$(libdir))
CMAKE_ARGS	+=	-DINSTALL_PLUGINDIR=$(subst $(prefix)/,,$(libdir))/$(NAME)/plugin
CMAKE_ARGS	+=	-DWITH_READLINE=1
CMAKE_ARGS	+=	-DWITH_LIBWRAP=1
CMAKE_ARGS	+=	-DWITH_SSL=system
CMAKE_ARGS	+=	-DWITH_ZLIB=system
CMAKE_ARGS	+=	-DDEFAULT_CHARSET=utf8
CMAKE_ARGS	+=	-DDEFAULT_COLLATION=utf8_general_ci
CMAKE_ARGS	+=	-DWITH_COMMENT='OpenCSW'
CMAKE_ARGS	+=	-DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS	+=	-DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS	+=	-DBUILD_CONFIG=mysql_release
# CMAKE_ARGS	+=	-DOPENSSL_INCLUDE_DIR="$(includedir)"
# CMAKE_ARGS	+=	-DCMAKE_LIBRARY_PATH="$(libdir)"
# CMAKE_ARGS	+=	-DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS	+=	-DOPENSSL_ROOT_DIR=$(prefix)
# CMAKE_ARGS	+=	-DOPENSSL_SSL_LIBRARIES=$(libdir)/libssl.so
# CMAKE_ARGS	+=	-DOPENSSL_CRYPTO_LIBRARIES=$(libdir)/libcrypto.so
CMAKE_ARGS	+=	-DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS	+=	-DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS	+=	"-DCMAKE_C_FLAGS=$(CFLAGS)"
CMAKE_ARGS	+=	"-DCMAKE_CXX_FLAGS=$(CXXFLAGS)"
CMAKE_ARGS	+=	-DCMAKE_VERBOSE_MAKEFILE=ON
CMAKE_ARGS	+=	-DWITH_DEBUG=1
CMAKE_ARGS	+=	-DPODOFO_BUILD_SHARED:BOOL=TRUE
CMAKE_ARGS	+=	-DPODOFO_BUILD_STATIC:BOOL=FALSE

TEST_SCRIPTS	=	custom

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

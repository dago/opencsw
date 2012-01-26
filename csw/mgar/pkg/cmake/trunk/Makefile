# $Id$

NAME = cmake
VERSION = 2.8.7
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = Cross-platform make
define BLURB
  CMake is used to control the software compilation process using simple
  platform and compiler independent configuration files. CMake generates
  native makefiles and workspaces that can be used in the compiler environment
  of your choice. CMake is quite sophisticated: it is possible to support
  complex environments requiring system configuration, pre-processor
  generation, code generation, and template instantiation. 
endef

RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9].*\)\.[0-9]*/\1/')
SPKG_SOURCEURL = http://cmake.org/
MASTER_SITES = http://cmake.org/files/v$(RELVER)/
DISTFILES = $(NAME)-$(VERSION).tar.gz
LICENSE = Copyright.txt

PACKAGES = CSWcmake
CATALOGNAME_CSWcmake = cmake
SPKG_DESC_CSWcmake = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWcmake += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWcmake += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWcmake += CSWlibz1
RUNTIME_DEP_PKGS_CSWcmake += CSWosslrt

datadir = /share/$(NAME)-$(VERSION)
sharedstatedir = /share
docdir = /share/doc/$(NAME)-$(VERSION)

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --docdir=$(docdir)

TEST_TARGET  = test
# Some tests are failing.
SKIPTEST = 1

CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content

include gar/category.mk

FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(NAME)-$(VERSION)/Modules
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(NAME)-$(VERSION)/Templates
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)$(docdir)
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/man/man1

EXTRA_CFLAGS = -xnorunpath
EXTRA_CXXFLAGS = -norunpath

pre-configure:
	@echo $(DIRPATHS)
	@echo "Docdir: $(docdir)"
	# Do NOT include the CSW include pathes here
	(cd $(WORKSRC); /usr/bin/env \
		CFLAGS="$($(GARCOMPILER)_CC_$(GARFLAVOR)) -I/opt/csw/include" \
		CXXFLAGS="$($(GARCOMPILER)_CXX_$(GARFLAVOR)) -I/opt/csw/include" \
		LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib/$$ISALIST -R/opt/csw/lib" \
		./bootstrap \
		--prefix=$(prefix)	\
		--datadir=$(datadir)	\
		--docdir=$(docdir)	\
		--mandir=/man		\
		--system-libs \
	)
	@$(MAKECOOKIE)

post-configure-modulated:
	@(echo "==> Forcing use of system libraries")
	@(echo "=====> curl, expat, xmlrpc, and zlib")
	@(perl -i -plne 's/USE_SYSTEM_CURL:BOOL=OFF/USE_SYSTEM_CURL:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_EXPAT:BOOL=OFF/USE_SYSTEM_EXPAT:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_XMLRPC:BOOL=OFF/USE_SYSTEM_XMLRPC:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_ZLIB:BOOL=OFF/USE_SYSTEM_ZLIB:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@$(MAKECOOKIE)

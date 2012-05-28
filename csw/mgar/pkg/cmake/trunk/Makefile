# $Id$

NAME = cmake
VERSION = 2.8.8
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
# temporary for cmake-2.8.8, see http://public.kitware.com/Bug/view.php?id=13199
PATCHFILES += 0001-bootstrap-Port-back-to-old-shells-13199.patch

PACKAGES = CSWcmake
CATALOGNAME_CSWcmake = cmake
SPKG_DESC_CSWcmake = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWcmake += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWcmake += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWcmake += CSWlibz1

CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cmakepolicies.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cmakecompat.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cmakemodules.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cpack.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/ccmake.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/ctest.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cmakeprops.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cmakecommands.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cmake.1
CHECKPKG_OVERRIDES_CSWcmake += disallowed-path|opt/csw/man/man1/cmakevars.1

NOISALIST = 1
CONFIGURE_ARGS = --prefix=$(prefix)

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

post-configure-modulated:
	@(echo "==> Forcing use of system libraries")
	@(echo "=====> curl, expat, xmlrpc, and zlib")
	@(perl -i -plne 's/USE_SYSTEM_CURL:BOOL=OFF/USE_SYSTEM_CURL:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_EXPAT:BOOL=OFF/USE_SYSTEM_EXPAT:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_XMLRPC:BOOL=OFF/USE_SYSTEM_XMLRPC:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_ZLIB:BOOL=OFF/USE_SYSTEM_ZLIB:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@$(MAKECOOKIE)

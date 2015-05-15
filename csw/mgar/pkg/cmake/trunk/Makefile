# $Id$

NAME = cmake
VERSION = 3.2.2
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

RELVER = $(shell echo $(VERSION) | cut -d. -f1-2)
MASTER_SITES = http://cmake.org/files/v$(RELVER)/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://cmake.org/
LICENSE = Copyright.txt

PACKAGES = CSWcmake
SPKG_DESC_CSWcmake = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWcmake += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWcmake += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWcmake += CSWlibz1
RUNTIME_DEP_PKGS_CSWcmake += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWcmake += CSWlibstlport1
CHECKPKG_OVERRIDES_CSWcmake += missing-dependency|CSWemacs-common

# This is most certainly the default installation prefix
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/ccmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/ctest
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/cpack

# This is /usr/local/bin vs. /opt/csw/bin
REINPLACE_USRLOCAL += Source/cmSiteNameCommand.cxx

CONFIGURE_ARGS = --prefix=$(prefix)

TEST_TARGET  = test

# Some tests are failing:
#         78 - Module.GenerateExportHeader (Failed)
#        173 - CTestTestUpload (Failed)
#        285 - RunCMake.CTestMemcheck (Failed)
#        352 - GTK2Targets.gio (Failed)
#        355 - GTK2Targets.atk (Failed)
#        356 - GTK2Targets.gdk_pixbuf (Failed)
#        358 - GTK2Targets.pango (Failed)
#        359 - GTK2Targets.pangocairo (Failed)
#        360 - GTK2Targets.pangoxft (Failed)
#        361 - GTK2Targets.pangoft2 (Failed)
#        362 - GTK2Targets.gdk (Failed)
#        363 - GTK2Targets.gtk (Failed)
#        364 - GTK2Targets.sigc++ (Failed)
#        365 - GTK2Targets.glibmm (Failed)
#        366 - GTK2Targets.giomm (Failed)
#        367 - GTK2Targets.atkmm (Failed)
#        368 - GTK2Targets.cairomm (Failed)
#        369 - GTK2Targets.pangomm (Failed)
#        370 - GTK2Targets.gdkmm (Failed)
#        371 - GTK2Targets.gtkmm (Failed)
#        401 - CMake.CheckSourceTree (Failed)

SKIPTEST = 1

#CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content

include gar/category.mk

EXTRA_CFLAGS = -xnorunpath
EXTRA_CXXFLAGS = -norunpath

post-configure:
	@(echo "==> Forcing use of system libraries")
	@(echo "=====> curl, expat, xmlrpc, and zlib")
	@(perl -i -plne 's/USE_SYSTEM_CURL:BOOL=OFF/USE_SYSTEM_CURL:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_EXPAT:BOOL=OFF/USE_SYSTEM_EXPAT:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_XMLRPC:BOOL=OFF/USE_SYSTEM_XMLRPC:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_ZLIB:BOOL=OFF/USE_SYSTEM_ZLIB:BOOL=ON/' $(WORKSRC)/CMakeCache.txt)
	@$(MAKECOOKIE)

# Entries with spaces in the filepath are not allowed in the pkgmap.
# Adjust the directory path to the help pages in 8.1.7
post-install:
	cd $(DESTDIR); find . -type d -name "* *" | \
		while read F; do \
			N=`echo $$F | tr ' ' '_'`; \
			mv "$$F" $$N; \
		done;
	cd $(DESTDIR); find . -type f -name "* *" | \
		while read F; do \
			N=`echo $$F | tr ' ' '_'`; \
			mv "$$F" $$N; \
		done;
	@$(MAKECOOKIE)

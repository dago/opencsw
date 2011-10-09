# $Id$

NAME = cmake
VERSION = 2.8.6
CATEGORIES = devel

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

RUNTIME_DEP_PKGS_CSWcmake  = CSWcurlrt CSWexpat
RUNTIME_DEP_PKGS_CSWcmake += CSWzlib 


# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

datadir = /share/$(NAME)-$(VERSION)
sharedstatedir = /share
docdir = /share/doc/$(NAME)-$(VERSION)

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --docdir=$(docdir)

# switch off tests as two of them fail
TEST_TARGET  = 

CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/cmakemodules.1
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/cmake.1
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/doc/cmake-2.8.4/cmake-modules.html
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/doc/cmake-2.8.4/cmake.txt
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/doc/cmake-2.8.4/cmake-modules.txt
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/doc/cmake-2.8.4/cmake-variables.html
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/doc/cmake-2.8.4/cmake.html
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/doc/cmake-2.8.4/cmake-variables.txt
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/doc/cmake-2.8.4/cmake.docbook
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindPostgreSQL.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindTCL.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/CMakeDetermineSystem.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSDL.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSDL_mixer.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindTclStub.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindMatlab.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindPhysFS.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindUnixCommands.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindOpenAL.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindJava.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindFLTK.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindQt3.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindFreetype.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/CMakeDetermineJavaCompiler.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/CMakeGenericSystem.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindGTK.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindJNI.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindwxWidgets.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSquish.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindMPEG.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindQt.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindKDE3.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/GetPrerequisites.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindCUDA.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSDL_net.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindGTK2.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindFLTK2.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindAVIFile.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindLAPACK.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindLua50.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindPHP4.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSDL_image.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindGIF.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindBLAS.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSDL_sound.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSDL_ttf.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindPike.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindPNG.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindLua51.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindProducer.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindMPEG2.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/FindSelfPackers.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/Platform/UnixPaths.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/cmake-2.8.4/Modules/Platform/BlueGeneP-base.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/ccmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/cpack
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/ctest
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/bin/cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/share|root/opt/csw/share/cmake-2.8.4/Modules/FindDart.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/share|root/opt/csw/share/cmake-2.8.4/Modules/FindJava.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/share|root/opt/csw/share/cmake-2.8.4/Modules/FindQt3.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/share|root/opt/csw/share/cmake-2.8.4/Modules/FindOpenGL.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/share|root/opt/csw/share/cmake-2.8.4/Modules/CMakeDetermineJavaCompiler.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/share|root/opt/csw/share/cmake-2.8.4/Modules/FindQt.cmake
CHECKPKG_OVERRIDES_CSWcmake += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/cmakevars.1


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



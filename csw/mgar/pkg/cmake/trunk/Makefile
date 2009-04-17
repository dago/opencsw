GARNAME = cmake
GARVERSION = 2.6.3
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

RELVER = $(shell echo $(GARVERSION) |gsed 's/\(^[0-9].*\)\.[0-9]*/\1/')
SPKG_SOURCEURL = http://www.cmake.org/
MASTER_SITES = http://www.cmake.org/files/v$(RELVER)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWcmake
CATALOGNAME_CSWcmake = cmake
SPKG_DESC_CSWcmake = $(DESCRIPTION)

REQUIRED_PKGS_CSWcmake  = CSWcurlrt CSWexpat CSWlibidn CSWoldaprt
REQUIRED_PKGS_CSWcmake += CSWosslrt CSWxmlrpc-c CSWzlib 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

datadir = /share/$(GARNAME)-$(GARVERSION)
sharedstatedir = /share
docdir = /share/doc/$(GARNAME)-$(GARVERSION)

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --docdir=$(docdir)

include gar/category.mk

FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(GARNAME)-$(GARVERSION)/Modules
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(GARNAME)-$(GARVERSION)/Templates
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)$(docdir)
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/man/man1

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
	@(perl -i -plne 's/USE_SYSTEM_CURL:BOOL=OFF/USE_SYSTEM_CURL:BOOL=ON/' \
		$(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_EXPAT:BOOL=OFF/USE_SYSTEM_EXPAT:BOOL=ON/' \
		$(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_XMLRPC:BOOL=OFF/USE_SYSTEM_XMLRPC:BOOL=ON/' \
		$(WORKSRC)/CMakeCache.txt)
	@(perl -i -plne 's/USE_SYSTEM_ZLIB:BOOL=OFF/USE_SYSTEM_ZLIB:BOOL=ON/' \
		$(WORKSRC)/CMakeCache.txt)
	@$(MAKECOOKIE)



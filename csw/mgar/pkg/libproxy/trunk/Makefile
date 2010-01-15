GARNAME = libproxy
GARVERSION = 0.3.0
CATEGORIES = lib

DESCRIPTION = A library that provides automatic proxy configuration management
define BLURB
  libproxy exists to answer the question: Given a network resource, how do I
  reach it? It handles all the details, enabling you to get back to programming.
  GNOME? KDE? Command line? WPAD? PAC? Network changed? It doesn't matter! Just
  ask libproxy what proxy to use: you get simple code and your users get correct,
  consistant behavior and broad infrastructure compatibility.
endef

MASTER_SITES = http://libproxy.googlecode.com/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#PATCHFILES  = 0001-Use-xc99-for-Sun-Studio-compiler.patch
PATCHFILES += 0002-Dont-preset-CFLAGS.patch
# For Solaris 10 targets
#PATCHFILES_isa-amd64 += SunStudio-have-no-stdc99-flag.patch
#PATCHFILES_isa-sparcv8 += SunStudio-have-no-stdc99-flag.patch
#PATCHFILES_isa-sparcv9 += SunStudio-have-no-stdc99-flag.patch
#PATCHFILES_isa-i386 += SunStudio-have-no-stdc99-flag.patch
#For Solaris 8 targets
PATCHFILES_isa-amd64 += SunStudio-have-no-stdc99-flag.patch
PATCHFILES_isa-sparcv8 += Solaris8-have-no-stdc99-flag.patch
PATCHFILES_isa-sparcv8 += stdfiles.patch
PATCHFILES_isa-sparcv8 += proxy.c.patch
PATCHFILES_isa-sparcv9 += Solaris8-have-no-stdc99-flag.patch
PATCHFILES_isa-sparcv9 += stdfiles.patch
PATCHFILES_isa-sparcv9 += proxy.c.patch
PATCHFILES_isa-i386 += Solaris8-have-no-stdc99-flag.patch
PATCHFILES_isa-i386 += stdfiles.patch
PATCHFILES_isa-i386 += proxy.c.patch

PACKAGES = CSWlibproxy CSWlibproxydevel CSWpy-libproxy
CATALOGNAME_CSWlibproxy = libproxy
CATALOGNAME_CSWlibproxydevel = libproxy_devel
CATALOGNAME_CSWpy-libproxy = py_libproxy
SPKG_DESC_CSWlibproxy = A library that provides automatic proxy configuration management
SPKG_DESC_CSWlibproxydevel = A library that provides automatic proxy configuration management - development files
SPKG_DESC_CSWpy-libproxy = A library that provides automatic proxy configuration management - Python bindings

REQUIRED_PKGS_CSWlibproxy += CSWlibice CSWlibsm CSWlibx11 CSWlibxmu CSWlibxt
REQUIRED_PKGS_CSWlibproxydevel += CSWlibproxy
REQUIRED_PKGS_CSWpy-libproxy += CSWpython CSWlibproxy
PREREQUISITE_PKGS += CSWlibx11devel CSWlibxmudevel CSWlibdbusdev
#Disable Mozilla/Firefox/Seamonkey plugin until there is a 64-bit version
#PREREQUISITE_PKGS += CSWmozilla CSWseamonkey CSWfirefox

PKGFILES_CSWlibproxydevel = $(PKGFILES_DEVEL)
PKGFILES_CSWpy-libproxy = $(libdir).*/python/site-packages/.*

ARCHALL_CSWpy-libproxy = 1

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

EXTRA_LINKER_FLAGS = -lnsl
BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#Disable Mozilla/Firefox/Seamonkey plugin until there is a 64-bit version
#EXTRA_PKG_CONFIG_DIRS += $(prefix)/mozilla/lib
#EXTRA_PKG_CONFIG_DIRS += $(prefix)/mozilla/firefox/lib
#EXTRA_PKG_CONFIG_DIRS += $(prefix)/mozilla/seamonkey/lib


CONFIGURE_ARGS = $(DIRPATHS)
#Disable Mozilla/Firefox/Seamonkey plugin until there is a 64-bit version
CONFIGURE_ARGS += --without-mozjs
CONFIGURE_ARGS += --with-python
CONFIGURE_ARGS += --disable-silent-rules

TEST_TARGET = check

include gar/category.mk

#pre-configure-modulated:
#	@echo " ==> Regenerating build tools..."
#	@(cd $(WORKSRC) ; \
#		aclocal                       && \
#		autoconf                      && \
#		libtoolize --automake --force && \
#		aclocal                       && \
#		automake -a )
#	@$(MAKECOOKIE)


# There is actually the cpp executable in /usr/lib
PATH := $(PATH):/usr/lib

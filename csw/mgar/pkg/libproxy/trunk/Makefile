NAME = libproxy
VERSION = 0.3.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library that provides automatic proxy configuration management
define BLURB
  libproxy exists to answer the question: Given a network resource, how do I
  reach it? It handles all the details, enabling you to get back to programming.
  GNOME? KDE? Command line? WPAD? PAC? Network changed? It doesn't matter! Just
  ask libproxy what proxy to use: you get simple code and your users get correct,
  consistant behavior and broad infrastructure compatibility.
endef

MASTER_SITES = http://libproxy.googlecode.com/files/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += SunStudio-have-no-stdc99-flag.patch
DISTFILES += Solaris8-have-no-stdc99-flag.patch
DISTFILES += stdfiles.patch
DISTFILES += proxy.c.patch
DISTFILES += 0002-Dont-preset-CFLAGS.patch

PACKAGING_PLATFORMS = solaris8-sparc solaris8-i386
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# For Solaris 10 targets
PATCHFILES_solaris10-sparc += SunStudio-have-no-stdc99-flag.patch
PATCHFILES_solaris10-i386 += SunStudio-have-no-stdc99-flag.patch
#For Solaris 8 targets
PATCHFILES_solaris8-sparc += Solaris8-have-no-stdc99-flag.patch
PATCHFILES_solaris8-sparc += stdfiles.patch
PATCHFILES_solaris8-sparc += proxy.c.patch
PATCHFILES_solaris8-i386_isa-amd64 += SunStudio-have-no-stdc99-flag.patch
PATCHFILES_solaris8-i386_isa-i386 += Solaris8-have-no-stdc99-flag.patch
PATCHFILES_solaris8-i386_isa-i386 += stdfiles.patch
PATCHFILES_solaris8-i386_isa-i386 += proxy.c.patch
#For Solaris 9 targets
PATCHFILES_solaris9-sparc += Solaris8-have-no-stdc99-flag.patch
PATCHFILES_solaris9-sparc += proxy.c.patch
PATCHFILES_solaris9-sparc += stdfiles.patch
PATCHFILES_solaris9-i386_isa-amd64 += SunStudio-have-no-stdc99-flag.patch
PATCHFILES_solaris9-i386_isa-i386 += Solaris8-have-no-stdc99-flag.patch
PATCHFILES_solaris9-i386_isa-i386 += stdfiles.patch
PATCHFILES_solaris9-i386_isa-i386 += proxy.c.patch
#For all targets
PATCHFILES += 0002-Dont-preset-CFLAGS.patch
# Merge them all together
PATCHFILES += $(PATCHFILES_$(GAR_PLATFORM))
PATCHFILES += $(PATCHFILES_$(GAR_PLATFORM)_$(MODULATION))


PACKAGES = CSWlibproxy CSWlibproxydevel CSWpy-libproxy
PACKAGES += CSWlibproxykde CSWlibproxygnome
CATALOGNAME_CSWlibproxy = libproxy
CATALOGNAME_CSWlibproxydevel = libproxy_devel
CATALOGNAME_CSWpy-libproxy = py_libproxy
CATALOGNAME_CSWlibproxykde = libproxy_kde
CATALOGNAME_CSWlibproxygnome = libproxy_gnome
SPKG_DESC_CSWlibproxy = $(DESCRIPTION)
SPKG_DESC_CSWlibproxydevel = $(DESCRIPTION) - development files
SPKG_DESC_CSWpy-libproxy = $(DESCRIPTION) - Python bindings
SPKG_DESC_CSWlibproxykde = $(DESCRIPTION) - kde module
SPKG_DESC_CSWlibproxygnome = $(DESCRIPTION) - gnome module

RUNTIME_DEP_PKGS_CSWlibproxy += 

RUNTIME_DEP_PKGS_CSWlibproxydevel += CSWlibproxy

RUNTIME_DEP_PKGS_CSWpy-libproxy += CSWpython CSWlibproxy

RUNTIME_DEP_PKGS_CSWlibproxygnome += CSWlibice
RUNTIME_DEP_PKGS_CSWlibproxygnome += CSWlibproxy
RUNTIME_DEP_PKGS_CSWlibproxygnome += CSWlibsm
RUNTIME_DEP_PKGS_CSWlibproxygnome += CSWlibx11
RUNTIME_DEP_PKGS_CSWlibproxygnome += CSWlibxmu
RUNTIME_DEP_PKGS_CSWlibproxygnome += CSWlibxt

RUNTIME_DEP_PKGS_CSWlibproxykde += CSWlibice
RUNTIME_DEP_PKGS_CSWlibproxykde += CSWlibproxy
RUNTIME_DEP_PKGS_CSWlibproxykde += CSWlibsm
RUNTIME_DEP_PKGS_CSWlibproxykde += CSWlibx11
RUNTIME_DEP_PKGS_CSWlibproxykde += CSWlibxmu
RUNTIME_DEP_PKGS_CSWlibproxykde += CSWlibxt

BUILD_DEP_PKGS += CSWlibx11devel CSWlibxmudevel CSWlibdbusdev

CHECKPKG_OVERRIDES_CSWpy-libproxy += surplus-dependency|CSWlibproxy
CHECKPKG_OVERRIDES_CSWlibproxy += soname-not-found|libm.so.2
CHECKPKG_OVERRIDES_CSWlibproxykde += soname-not-found|libm.so.2
CHECKPKG_OVERRIDES_CSWlibproxydevel += surplus-dependency|CSWlibproxy
CHECKPKG_OVERRIDES_CSWlibproxygnome += soname-not-found|libm.so.2

#Disable Mozilla/Firefox/Seamonkey plugin until there is a 64-bit version
#BUILD_DEP_PKGS += CSWmozilla CSWseamonkey CSWfirefox

PKGFILES_CSWlibproxydevel = $(PKGFILES_DEVEL)
PKGFILES_CSWpy-libproxy = $(libdir).*/python/site-packages/.*
PKGFILES_CSWlibproxykde = $(libdir).*/config_kde.so
PKGFILES_CSWlibproxygnome = $(libdir).*/config_gnome.so

ARCHALL_CSWpy-libproxy = 1

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_LINKER_FLAGS = -lnsl

BUILD64_LIBS_ONLY = 1

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

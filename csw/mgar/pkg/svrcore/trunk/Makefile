# $Id$
#
NAME = svrcore
MAJOR_VERSION = 4
MIN_VERSION = 0.4
VERSION = $(MAJOR_VERSION).$(MIN_VERSION)
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Mozilla LDAP SVR Core
define BLURB
  This is the Mozilla SVR Core needed by LDAP SDK
endef

MASTER_SITES = http://ftp.mozilla.org/pub/directory/svrcore/releases/4.0.4/src/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

PACKAGES += CSWlibsvrcore0
CATALOGNAME_CSWlibsvrcore0 = libsvrcore0
SPKG_DESC_CSWlibsvrcore0 += $(DESCRIPTION)
PKGFILES_CSWlibsvrcore0 = $(call pkgfiles_lib,libsvrcore.so.0)
RUNTIME_DEP_PKGS_CSWlibsvrcore0 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibsvrcore0 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibsvrcore0 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibsvrcore0 += CSWlibplds4

PACKAGES += CSWlibsvrcore0-dev
CATALOGNAME_CSWlibsvrcore0-dev = libsvrcore0_dev
SPKG_DESC_CSWlibsvrcore0-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibsvrcore0-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsvrcore0-dev += /opt/csw/lib/libsvrcore.so
PKGFILES_CSWlibsvrcore0-dev += /opt/csw/lib/sparcv9/libsvrcore.so
ARCHALL_CSWgnutlsdevel = 1
RUNTIME_DEP_PKGS_CSWlibsvrcore0-dev += CSWlibsvrcore0

# Move the include files to include/nspr to prevent polluting the main
# header file namespace.
# includedir = $(prefix)/include/nspr

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS_64 = --enable-64bit
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))
CONFIGURE_ARGS_OPT += --enable-optimize="-xO3"
CONFIGURE_ARGS_OPT += --disable-debug
CONFIGURE_ARGS_OPT += --enable-strip
CONFIGURE_ARGS_DBG += --enable-debug
CONFIGURE_ARGS_DBG += --disable-strip
CONFIGURE_ARGS += --with-nss-inc=$(includedir)/nss
CONFIGURE_ARGS += --with-nss-lib=$(libdir)
CONFIGURE_ARGS += --with-nspr-inc=$(includedir)/nspr
CONFIGURE_ARGS += --with-nspr-lib=/$(libdir)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

BUILD64_LIBS_ONLY = 1

include gar/category.mk


NAME = libdatrie
VERSION = 0.2.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Double array tree library
define BLURB
endef

MASTER_SITES = ftp://linux.thai.net/pub/ThaiLinux/software/libthai/
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0001-Remove-unnecessary-inclusing-of-stdint.h.patch

VENDOR_URL = http://linux.thai.net/~thep/datrie/datrie.html

PACKAGES += CSWlibdatrie1
SPKG_DESC_CSWlibdatrie1 = Double array tree library, libdatrie.so.1
PKGFILES_CSWlibdatrie1 += $(call pkgfiles_lib,libdatrie.so.1)
OBSOLETED_BY_CSWlibdatrie1 += CSWlibdatrie

PACKAGES += CSWlibdatrie-dev
SPKG_DESC_CSWlibdatrie-dev = Development files for libdatrie.so.1
PKGFILES_CSWlibdatrie-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibdatrie-dev += $(docdir)/libdatrie-dev/.*
RUNTIME_DEP_PKGS_CSWlibdatrie-dev += CSWlibdatrie1

PACKAGES += CSWlibdatrie-utils
SPKG_DESC_CSWlibdatrie-utils = Utility programs using libdatrie
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibdatrie-utils += CSWlibdatrie1
RUNTIME_DEP_PKGS_CSWlibdatrie-utils += CSWlibiconv2

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-html-docdir=$(docdir)/libdatrie-dev/html

# This is not properly detected
BUILD_OVERRIDE_VARS = ICONV_LIBS
BUILD_OVERRIDE_VAR_ICONV_LIBS = -liconv

include gar/category.mk

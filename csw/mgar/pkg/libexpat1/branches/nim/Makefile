NAME = expat
VERSION = 2.1.0
GARTYPE = bts lib
GARTYPE = v2

DESCRIPTION = XML parser toolkit
define BLURB
  This is James Clark's Expat XML parser library in C. It is a stream oriented
  parser that requires setting handlers to deal with the structure that the
  parser discovers in the document.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz

# This is for legacy packaNIMOSSexpat to use libexpat.so.0
FOREIGN_PACKAGES += NIMOSSlibexpat0

PACKAGES += NIMOSSlibexpat1
SPKG_DESC_NIMOSSlibexpat1 = XML parser toolkit, libexpat.so.1
PKGFILES_NIMOSSlibexpat1 += $(call pkgfiles_lib,libexpat.so.1)

PACKAGES += NIMOSSlibexpat-dev
SPKG_DESC_NIMOSSlibexpat-dev += Development files for libexpat.so.1
PKGFILES_NIMOSSlibexpat-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_NIMOSSlibexpat-dev += NIMOSSlibexpat1

PACKAGES += NIMOSSexpat
SPKG_DESC_NIMOSSexpat = XML parser toolkit utility
RUNTIME_DEP_PKGS_NIMOSSexpat += NIMOSSlibexpat1
# This is for legacy packages depending on NIMOSSexpat to use libexpat.so.0
RUNTIME_DEP_PKGS_NIMOSSexpat += NIMOSSlibexpat0
CHECKPKG_OVERRIDES_NIMOSSexpat += surplus-dependency|NIMOSSus-dependency|CSWlibexpat0

# Testsuite needs __func__
EXTRA_CXXFLAGS = -features=extensions

BUILD64 = 1
ISAEXEC = 1

include
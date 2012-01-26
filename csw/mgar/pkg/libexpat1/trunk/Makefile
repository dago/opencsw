NAME = expat
VERSION = 2.0.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = XML parser toolkit
define BLURB
  This is James Clark's Expat XML parser library in C. It is a stream oriented
  parser that requires setting handlers to deal with the structure that the
  parser discovers in the document.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz

FOREIGN_PACKAGES += CSWlibexpat0

PACKAGES += CSWlibexpat1
SPKG_DESC_CSWlibexpat1 = XML parser toolkit, libexpat.so.1
PKGFILES_CSWlibexpat1 += $(call pkgfiles_lib,libexpat.so.1)

PACKAGES += CSWlibexpat-dev
SPKG_DESC_CSWlibexpat-dev += Development files for libexpat.so.1
PKGFILES_CSWlibexpat-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibexpat-dev += CSWlibexpat1

PACKAGES += CSWexpat
SPKG_DESC_CSWexpat = XML parser toolkit utility
RUNTIME_DEP_PKGS_CSWexpat += CSWlibexpat1
# This is for legacy packages depending on CSWexpat to use libexpat.so.0
RUNTIME_DEP_PKGS_CSWexpat += CSWlibexpat0
CHECKPKG_OVERRIDES_CSWexpat += surplus-dependency|CSWlibexpat0

# Testsuite needs __func__
EXTRA_CXXFLAGS = -features=extensions

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

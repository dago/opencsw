NAME = expat
VERSION = 1.95.8
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = XML parser toolkit
define BLURB
  This is James Clark's Expat XML parser library in C. It is a stream oriented
  parser that requires setting handlers to deal with the structure that the
  parser discovers in the document.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWlibexpat0
SPKG_DESC_CSWlibexpat0 = XML parser toolkit, libexpat.so.0
PKGFILES_CSWlibexpat0 += $(call pkgfiles_lib,libexpat.so.0)

BUILD64_LIBS_ONLY = 1

INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir libdir includedir man1dir

include gar/category.mk

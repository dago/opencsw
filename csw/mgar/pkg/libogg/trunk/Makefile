NAME = libogg
VERSION = 1.3.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Ogg bitstream format support library
define BLURB
  libogg is the bitstream and framing library for the Ogg project. It provides
  functions which are necessary to codec libraries like libvorbis.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ogg/
DISTFILES  = $(DISTNAME).tar.xz

PACKAGES += CSWlibogg0
CATALOGNAME_CSWlibogg0 = libogg0
SPKG_DESC_CSWlibogg0 = Ogg bitstream format support library, libogg.so.0
PKGFILES_CSWlibogg0 = $(call pkgfiles_lib,libogg.so.0)
OBSOLETED_BY_CSWlibogg0 = CSWlibogg

PACKAGES += CSWlibogg-dev
CATALOGNAME_CSWlibogg-dev = libogg_dev
SPKG_DESC_CSWlibogg-dev = Development files for libogg.so.0
RUNTIME_DEP_PKGS_CSWlibogg-dev = CSWlibogg0

VENDOR_URL = http://www.vorbis.com/

BUILD64_LIBS_ONLY = 1

include gar/category.mk

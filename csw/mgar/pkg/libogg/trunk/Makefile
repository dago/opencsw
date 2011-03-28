NAME = libogg
VERSION = 1.2.2
CATEGORIES = lib

DESCRIPTION = Ogg bitstream format support library
define BLURB
  libogg is the bitstream and framing library for the Ogg project. It provides
  functions which are necessary to codec libraries like libvorbis.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ogg/
DISTFILES  = $(NAME)-$(VERSION).tar.xz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWlibogg0
CATALOGNAME_CSWlibogg0 = libogg0
SPKG_DESC_CSWlibogg0 = Ogg bitstream format support library providing libogg.so.0
PKGFILES_CSWlibogg0 = $(call baseisadirs,$(libdir),libogg\.so\.0(\.\d+)*)
OBSOLETED_BY_CSWlibogg0 = CSWlibogg

PACKAGES += CSWlibogg-dev
CATALOGNAME_CSWlibogg-dev = libogg_dev
SPKG_DESC_CSWlibogg-dev = Development files for libogg.so
RUNTIME_DEP_PKGS_CSWlibogg-dev = CSWlibogg0

VENDOR_URL = http://www.vorbis.com/

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

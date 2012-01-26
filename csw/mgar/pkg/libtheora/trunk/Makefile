NAME = libtheora
VERSION = 1.1.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Theora video codec support library
define BLURB
  Theora is a free and open video compression format from the Xiph.org Foundation.
  Like all our multimedia technology it can be used to distribute film and video
  online and on disc without the licensing and royalty fees or vendor lock-in
  associated with other formats. 
endef

MASTER_SITES = http://downloads.xiph.org/releases/theora/
DISTFILES  = $(NAME)-$(VERSION).tar.xz

VENDOR_URL = http://www.theora.org

BUILD_DEP_PKGS = CSWtransfig

PACKAGES += CSWlibtheora0
PKGFILES_CSWlibtheora0 += $(call pkgfiles_lib,libtheora.so.0)
SPKG_DESC_CSWlibtheora0 += Theora video codec support library, libtheora.so.0
RUNTIME_DEP_PKGS_CSWlibtheora0 += CSWlibogg0
OBSOLETED_BY_CSWlibtheora0 = CSWtheora
CATALOGNAME_CSWtheora = libtheora_stub

PACKAGES += CSWlibtheoradec1
PKGFILES_CSWlibtheoradec1 += $(call pkgfiles_lib,libtheoradec.so.1)
SPKG_DESC_CSWlibtheoradec1 += Theora video codec support library, libtheoradec.so.1
OBSOLETED_BY_CSWlibtheora0 = CSWtheora

PACKAGES += CSWlibtheoraenc1
PKGFILES_CSWlibtheoraenc1 += $(call pkgfiles_lib,libtheoraenc.so.1)
SPKG_DESC_CSWlibtheoraenc1 += Theora video codec support library, libtheoraenc.so.1
RUNTIME_DEP_PKGS_CSWlibtheoraenc1 += CSWlibogg0
OBSOLETED_BY_CSWlibtheora0 = CSWtheora

PACKAGES += CSWlibtheora-dev
SPKG_DESC_CSWlibtheora-dev = Development files for libtheora.so.0, libtheoradec.so.1 and libtheoraenc.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtheora-dev += CSWlibtheora0
RUNTIME_DEP_PKGS_CSWlibtheora-dev += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibtheora-dev += CSWlibtheoraenc1

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-examples
CONFIGURE_ARGS += --disable-asm

EXTRA_PAX_ARGS += -s ',^\.$(docdir)/$(NAME)-$(VERSION),.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME),'

include gar/category.mk

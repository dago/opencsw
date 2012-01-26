NAME = freetype
VERSION = 2.4.8
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A free and portable TrueType font rendering engine
define BLURB
  FreeType 2 is a high-quality and portable font engine that is capable of
  supporting several font formats (be they bitmapped or scalable) through a
  simple and uniform interface. Its design is modular and allows independent
  "font driver" modules to be added, even at runtime, to support additional
  formats. It also provides a high-quality anti-aliasing renderer, an innovative
  auto-hinting engine, and support for the following font formats: TrueType
  Type1, CID-Type 1, Multiple Masters Type 1 OpenType/CFF, pure CFF, and CEF
  Windows FNT/FON.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(NAME)-$(VERSION).tar.bz2

LICENSE = docs/LICENSE.TXT

VENDOR_URL = http://www.freetype.org/

PACKAGES += CSWlibfreetype6
SPKG_DESC_CSWlibfreetype6 = A free and portable TrueType font rendering engine, libfreetype.so.6
PKGFILES_CSWlibfreetype6 += $(call pkgfiles_lib,libfreetype.so.6)
RUNTIME_DEP_PKGS_CSWlibfreetype6 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibfreetype6 += CSWlibz1
OBSOLETED_BY_CSWlibfreetype6 += CSWftype2
CATALOGNAME_CSWftype2 = freetype2_stub

# This is inside a comment
CHECKPKG_OVERRIDES_CSWlibfreetype-dev += file-with-bad-content|/usr/local|root/opt/csw/include/ft2build.h

PACKAGES += CSWlibfreetype-dev
SPKG_DESC_CSWlibfreetype-dev = Development files for libfreetype.so.6
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibfreetype-dev += CSWlibfreetype6

GNUMAKE = gmake
EXTRA_CONFIGURE_EXPORTS = GNUMAKE

BUILD64_LIBS_ONLY = 1

include gar/category.mk

GARNAME = freetype
GARVERSION = 2.3.9
CATEGORIES = lib

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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PACKAGES = CSWftype2
CATALOGNAME_CSWftype2 = freetype2
SPKG_SOURCEURL = http://www.freetype.org/

REQUIRED_PKGS_CSWftype2 = CSWzlib

CONFIGURE_ARGS = $(DIRPATHS)
GNUMAKE = gmake
EXTRA_CONFIGURE_EXPORTS = GNUMAKE

BUILD64 = 1
NO_ISAEXEC = 1

TEST_TARGET = check

include gar/category.mk

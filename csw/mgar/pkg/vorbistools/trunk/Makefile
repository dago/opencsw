NAME = vorbistools
VERSION = 1.4.0
CATEGORIES = utils

DESCRIPTION = Vorbis audio tools
define BLURB
    Ogg Vorbis is a high-quality lossy audio codec which is free of intellectual
    property restrictions (like those surrounding MP3). These are the tools that
    one needs to create and play Ogg Vorbis files on the commandline, as well as a
    simple commentor.
endef

DISTNAME = vorbis-tools-$(VERSION)
MASTER_SITES = http://downloads.xiph.org/releases/vorbis/
DISTFILES = $(DISTNAME).tar.gz

VENDOR_URL = http://www.vorbis.com

PACKAGES = CSWvtools
CATALOGNAME = vorbistools

BUILD_DEP_PKGS = CSWcurldevel

RUNTIME_DEP_PKGS += CSWcurlrt
RUNTIME_DEP_PKGS += CSWflac
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWlibao
RUNTIME_DEP_PKGS += CSWlibogg
RUNTIME_DEP_PKGS += CSWspeex
RUNTIME_DEP_PKGS += CSWsunmath
RUNTIME_DEP_PKGS += CSWvorbis

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_LINKER_FLAGS += -lrt

BUILD64 = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis pentium_pro

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

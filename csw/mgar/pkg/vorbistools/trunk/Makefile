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

PACKAGES = CSWvorbistools
SPKG_DESC_CSWvorbistools = Vorbis audio tools
OBSOLETED_BY_CSWvorbistools = CSWvtools
CATALOGNAME_CSWvtools = vorbistools_stub

BUILD_DEP_PKGS += CSWlibcurl-dev
BUILD_DEP_PKGS += CSWlibkate-dev
BUILD_DEP_PKGS += CSWlibogg-dev
BUILD_DEP_PKGS += CSWlibvorbis-dev
BUILD_DEP_PKGS += CSWlibflac-dev
BUILD_DEP_PKGS += CSWlibao-dev
BUILD_DEP_PKGS += CSWlibspeex-dev
BUILD_DEP_PKGS += CSWggettext-dev

RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibkate1
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibogg0
RUNTIME_DEP_PKGS_CSWvorbistools += CSWliboggkate1
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibflac8
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibao4
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWvorbistools += CSWlibintl8
RUNTIME_DEP_PKGS_CSWvorbistools += CSWiconv

EXTRA_LINKER_FLAGS += -lrt

BUILD64 = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis pentium_pro

include gar/category.mk

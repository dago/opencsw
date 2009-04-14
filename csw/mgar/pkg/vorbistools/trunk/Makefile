GARNAME = vorbistools
GARVERSION = 1.2.0
CATEGORIES = utils

DESCRIPTION = Vorbis audio tools
define BLURB
    Ogg Vorbis is a high-quality lossy audio codec which is free of intellectual
    property restrictions (like those surrounding MP3). These are the tools that
    one needs to create and play Ogg Vorbis files on the commandline, as well as a
    simple commentor.
endef

DISTNAME = vorbis-tools-$(GARVERSION)
MASTER_SITES = http://downloads.xiph.org/releases/vorbis/
DISTFILES = $(DISTNAME).tar.gz
DISTFILES += fixme.sh

SPKG_SOURCEURL = http://www.vorbis.com

PACKAGES = CSWvtools
CATALOGNAME = vorbistools

REQUIRED_PKGS = CSWcurlrt CSWflac CSWggettextrt CSWiconv CSWlibao
REQUIRED_PKGS += CSWlibogg CSWspeex CSWsunmath CSWvorbis

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

BUILD64 = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis pentium_pro

EXTRA_LINKER_FLAGS += -lrt

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-configure-modulated:
	@echo " ==> Fixing libtool files"
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	@$(MAKECOOKIE)


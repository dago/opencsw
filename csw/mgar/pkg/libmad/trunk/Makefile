GARNAME = libmad
GARVERSION = 0.15.1b
CATEGORIES = lib

DESCRIPTION = MPEG Audio Decoder
define BLURB
  MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1 and the
  MPEG-2 extension to lower sampling frequencies, as well as the de facto MPEG 2.5
  format. All three audio layers - Layer I, Layer II, and Layer III (i.e. MP3) -
  are fully implemented.
endef

SF_PROJ = mad
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz
DISTFILES += mad-32.pc mad-64.pc

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.underbit.com/products/mad/

CONFIGURE_ARGS  = $(DIRPATHS)

BUILD64 = 1

TEST_TARGET = check

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(libdir)/pkgconfig
	ginstall $(WORKDIR)/mad-$(MEMORYMODEL).pc $(DESTDIR)$(libdir)/pkgconfig/mad.pc
	@$(MAKECOOKIE)

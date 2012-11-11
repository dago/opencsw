NAME = libmad
VERSION = 0.15.1b
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = MPEG Audio Decoder
define BLURB
  MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1 and the
  MPEG-2 extension to lower sampling frequencies, as well as the de facto MPEG 2.5
  format. All three audio layers - Layer I, Layer II, and Layer III (i.e. MP3) -
  are fully implementeECTd.
endef

SF_PROJ = mad
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz
DISTFILES += mad-32.pc mad-64.pc

VENDOR_URL = http://www.underbit.com/products/mad/

PACKAGES += CSWlibmad0
SPKG_DESC_CSWlibmad0 = MPEG audio decoder library, libmad.so.0
PKGFILES_CSWlibmad0 += $(call pkgfiles_lib,libmad.so.0)
OBSOLETED_BY_CSWlibmad0 = CSWlibmad

PACKAGES += CSWlibmad-dev
SPKG_DESC_CSWlibmad-dev = Development files for libmad.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibmad-dev = CSWlibmad0

BUILD64_LIBS_ONLY = 1

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(libdir)/pkgconfig
	ginstall $(WORKDIR)/mad-$(MEMORYMODEL).pc $(DESTDIR)$(libdir)/pkgconfig/mad.pc
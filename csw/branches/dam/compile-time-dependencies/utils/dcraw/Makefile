GARNAME = dcraw
GARVERSION = 8.77
CATEGORIES = utils

DESCRIPTION = Raw Digital Photo Decoder
define BLURB
  dcraw (pronounced "dee-see-raw") is a raw photo decoder. It decodes raw (CCD)
  data of most modern digital cameras and outputs PPM or PSD files.
endef

MASTER_SITES = http://cybercom.net/~dcoffin/dcraw/
DISTFILES  = dcraw.c dcraw.1
DISTFILES += clean_crw.c
DISTFILES += $(call admfiles,CSWdcraw,prototype depend)
DISTFILES += Makefile LICENSE

CONFIGURE_SCRIPTS =
#BUILD_SCRIPTS =
TEST_TARGET =

COPY_FILES = download/dcraw.c download/dcraw.1 download/clean_crw.c
COPY_FILES += download/Makefile

SPKG_SOURCEURL = http://cybercom.net/~dcoffin/dcraw/
SPKG_PKGBASE = $(DESTDIR)$(prefix)

include ../category.mk

pre-build:
	test -d $(WORKSRC) || mkdir -p $(WORKSRC)
	cp -p $(COPY_FILES) $(WORKSRC)

#build: $(WORKSRC)/dcraw
#	cc -o $(WORKSRC)/dcraw $(LDFLAGS) $(WORKSRC)/dcraw.o -lm -ljpeg

#$(WORKSRC)/dcraw.o: $(WORKSRC)/dcraw.c
#	cc -o $(WORKSRC)/dcraw.o -c $(CFLAGS) $(WORKSRC)/dcraw.c

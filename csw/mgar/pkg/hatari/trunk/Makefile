GARNAME = hatari
GARVERSION = 1.2.0
CATEGORIES = apps

DESCRIPTION = Atari ST emulator
define BLURB
Hatari is an Atari ST and STE emulator for GNU/Linux, BSD, BeOS, Mac OS X and other systems that are supported by the SDL library.
endef

MASTER_SITES = http://download.berlios.de/hatari/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWhatari, depend )

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LICENSE = gpl.txt
PATCHFILES = stdint.h.diff
GARCOMPILER = GNU
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS) LIBS='-lm -lsocket'
BUILD_ARGS = LD_OPTIONS='-R/opt/csw/lib/$ISALIST -R/opt/csw/lib -L/opt/csw/lib'
include gar/category.mk

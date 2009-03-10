GARNAME = hatari
GARVERSION = 1.2.0
CATEGORIES = apps

DESCRIPTION = Atari ST emulator
define BLURB
Hatari is an Atari ST and STE emulator for GNU/Linux, BSD, BeOS, Mac OS X and other systems that are supported by the SDL library.
endef

MASTER_SITES = http://download.berlios.de/hatari/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWhatari,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
GARNAME = moonbuggy
GARVERSION = 1.0.51
CATEGORIES = apps

DESCRIPTION = Moon-buggy is a simple character graphics game
define BLURB
Moon-buggy is a simple character graphics game where you drive some kind of car across the moon's surface. Unfortunately there are dangerous craters there. Fortunately your car can jump over them! 
endef

MASTER_SITES = http://seehuhn.de/media/programs/ 
DISTFILES  = moon-buggy-$(GARVERSION).tar.gz
DISTNAME = moon-buggy-$(GARVERSION)

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)


SKIPTEST = 1

include gar/category.mk

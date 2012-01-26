# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = moonbuggy
VERSION = 1.0.51
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Moon-buggy is a simple character graphics game
define BLURB
Moon-buggy is a simple character graphics game where you drive some kind of car across the moon's surface. Unfortunately there are dangerous craters there. Fortunately your car can jump over them! 
endef

MASTER_SITES = http://seehuhn.de/media/programs/ 
DISTFILES  = moon-buggy-$(VERSION).tar.gz
DISTNAME = moon-buggy-$(VERSION)

# File name regex to get notifications about upstream software releases
UFILES_REGEX = moon-buggy-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)


SKIPTEST = 1

include gar/category.mk

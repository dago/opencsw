NAME = lcms2
VERSION = 2.2
CATEGORIES = apps

DESCRIPTION = The little color management system and tools
define BLURB
	Little cms intends to be a small-footprint, speed optimized 
	color management engine in open source form. Since the initial release, 
	back in 1998, lcms has been continuously evolving, mostly thanks to 
	contributions done by skilled programmers, who generously donated 
	their valuable time to review the engine and the documentation. 
	For now, little cms has been ported to a big number of platforms and 
	is currently used in many open source and commercial products, 
	as well as being distributed in major linux environments. 
endef

SF_PROJ = lcms
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Remove-hardcoded-Wall.patch

VENDOR_URL = http://www.littlecms.com/

# Probably make separate package for Solaris 10 as it has float support
EXTRA_CPPFLAGS-5.9 = -Dpowf=pow -Dfabsf=labs
EXTRA_CPPFLAGS = $(EXTRA_CPPFLAGS-$(GAROSREL))

EXTRA_LINKER_FLAGS = -lm

OPT_FLAGS_SOS = -xO0

BUILD64 = 1

include gar/category.mk

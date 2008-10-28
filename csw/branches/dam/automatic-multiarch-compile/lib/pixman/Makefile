GARNAME = pixman
GARVERSION = 0.12.0
CATEGORIES = lib

DESCRIPTION = Cairo's image surface backend
define BLURB
endef

MASTER_SITES = http://www.cairographics.org/releases/
SOURCEFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES  = $(SOURCEFILES)
DISTFILES += $(call admfiles,CSWpixman,)

CONFIGURE_ARGS  = $(DIRPATHS)
# Only for testing, GTK needs pixman, so breakup circular dependency
CONFIGURE_ARGS += --disable-gtk

BUILD64 = 1

include ../category.mk

GARNAME = transmission
GARVERSION = 1.42
CATEGORIES = net

DESCRIPTION = Fast, easy, and free multi-platform BitTorrent client
define BLURB
endef

MASTER_SITES = http://mirrors.m0k.org/transmission/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWtransmission,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)

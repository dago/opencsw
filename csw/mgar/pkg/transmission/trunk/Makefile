GARNAME = transmission
GARVERSION = 1.60
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
EXTRA_CFLAGS = -DNO_SYS_QUEUE_H

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)

GARNAME = libdvdcss
GARVERSION = 1.2.9
CATEGORIES = lib

DESCRIPTION = library for accessing DVDs like a block device without having to bother about decryption
define BLURB
library for accessing DVDs like a block device without having to bother about decryption
endef

MASTER_SITES = http://download.videolan.org/pub/libdvdcss/1.2.9/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibdvdcss, depend )

GARCOMPILER ?= GNU

CONFIGURE_ARGS = $(DIRPATHS)

#ENABLE_TEST = 0

include ../category.mk

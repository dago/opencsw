GARNAME = libsigsegv
GARVERSION = 2.6
CATEGORIES = lib

DESCRIPTION = stuff
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWlibsigsegv)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static --enable-shared

BUILD64 = 1

TEST_TARGET = check

include ../category.mk

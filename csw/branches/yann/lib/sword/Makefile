GARNAME = sword
GARVERSION = 1.5.8
CATEGORIES = lib

DESCRIPTION = SWORD Engine (gcc3)
define BLURB
The SWORD Engine is a software framework that allows research manipulation of Biblical texts. There are a number of projects that use The SWORD Engine, including Bibletime, GnomeSword, and The SWORD Project for Windows. Many of these projects already include The SWORD Engine in their distribution, so only download if you were instructed to do so, or are a software developer wishing to develop Bible software.
endef

MASTER_SITES = http://www.crosswire.org/ftpmirror/pub/sword/source/v1.5
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsword, depend )

GARCOMPILER ?= GNU

CONFIGURE_ARGS = $(DIRPATHS)

ENABLE_TEST = 0

include ../category.mk

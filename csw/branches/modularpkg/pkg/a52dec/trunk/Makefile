GARNAME = a52dec
GARVERSION = 0.7.4
CATEGORIES = lib

DESCRIPTION = a free ATSC A/52 stream decoder
define BLURB
  liba52 is a free library for decoding ATSC A/52 streams. It is released under the terms of the GPL license. The A/52 standard is used in a variety of applications, including digital television and DVD. It is also known as AC-3.
endef

MASTER_SITES = http://liba52.sourceforge.net/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWliba52, depend)

CONFIGURE_ARGS = $(DIRPATHS) --enable-shared --disable-static


include gar/category.mk


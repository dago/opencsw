GARNAME = libgpod
GARVERSION = 0.4.2
CATEGORIES = lib

DESCRIPTION = Interface to Apple iPods
define BLURB
  libgpod is a shared library to access the contents of
  an iPod.  This library is based on code used in the
  gtkpod project.  libgpod supports playlists, smart
  playlists, playcounts, ratings, podcasts and cover art.
endef

SF_PROJ = gtkpod
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWlibgpod,depend)

GARCOMPILER = GNU
GNU_CC_HOME = /opt/csw/gcc4

DEPENDS += cpan/XML-Parser

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += PATH=/opt/csw/bin:$$PATH
#CONFIGURE_ARGS += TAGLIB_CFLAGS="-I/opt/csw/include/taglib" TAGLIB_LIBS="-ltag"

include ../category.mk

jwtest:
	echo $(DEPEND_LIST)

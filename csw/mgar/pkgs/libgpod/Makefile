GARNAME = libgpod
GARVERSION = 0.6.0
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
#GCC4 won't work. There are too many libtool deps using GCC3
GNU_CC_HOME = /opt/csw/gcc3

CONFIGURE_ARGS = $(DIRPATHS) --includedir=/opt/csw/include
TEST_SCRIPTS =

include ../category.mk

post-install: remove-libtool-files

remove-libtool-files:
	(gfind $(DESTDIR)/opt/csw/lib -name \*.la -exec rm {} \;)
	(gfind $(DESTDIR)/opt/csw/lib -name \*.a -exec rm {} \;)

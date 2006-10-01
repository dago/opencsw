GARNAME = libgpod
GARVERSION = 0.3.2
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
DISTFILES   += $(call admfiles,CSWlibgpod,depend prototype)
PATCHFILES += headerdir.diff

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk

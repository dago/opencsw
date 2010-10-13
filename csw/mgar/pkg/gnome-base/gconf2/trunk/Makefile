GARNAME = gconf2
GNOME_PROJ = GConf
GARVERSION = 2.28.1
CATEGORIES = apps

DESCRIPTION = GNOME configuration database system
define BLURB
  GConf is a system for storing application preferences. It is intended
  for user preferences; not configuration of something like Apache, or
  arbitrary data storage.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTNAME = GConf-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://projects.gnome.org/gconf/


#Normally, woudl split out doc. but the doc part is tiny compared
# to the rest of it, so makes no sense.
# 
##PACKAGES=CSWgconf2 CSWgconf2doc
##SPKG_DESC_CSWgconf2doc = Documentation for gconf2
##PKGFILES_CSWgconf2doc = $(sharedstatedir)/gtk-doc/.*

RUNTIME_DEP_PKGS_CSWgconf2 += CSWfconfig CSWftype2 CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWgconf2 += CSWgtk2 CSWlibcairo CSWlibxml2 
RUNTIME_DEP_PKGS_CSWgconf2 += CSWorbit2 CSWpango
# Arg it's absurd gconf is this complex...
RUNTIME_DEP_PKGS_CSWgconf2 += CSWlibdbus CSWdbusglib CSWlibatk


#BUILD64 = 1
#NOISAEXEC = 1

TEST_TARGET = check

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --disable-defaults-service
#The "defaults service" requires polkit. and dbus.
#We're better off without em.

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

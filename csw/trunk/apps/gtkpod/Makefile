GARNAME = gtkpod
GARVERSION = 0.99.10
CATEGORIES = apps

DESCRIPTION = gtk2 application for Apple iPods
define BLURB
  gtkpod is a platform independent Graphical User
  Interface for Apple's iPod using GTK2.  It supports
  the first to fifth Generation including the iPod
  mini, iPod Photo, iPod Shuffle, iPod nano, and iPod
  Video.
endef

SF_PROJ = gtkpod
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWgtkpod)#,depend)
#PATCHFILES += gthread-fix.diff libs.diff mp4v2.diff
PATCHFILES  = file_convert.diff

GARCOMPILER = GNU
GNU_CC_HOME = /opt/csw/gcc4

LIBDEPS += lib/libgpod

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += CPPFLAGS="-I. -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

#CONFIGURE_SCRIPTS = custom $(WORKSRC)/configure

include ../category.mk

#configure-custom:
#	@touch $(WORKSRC)/config.h

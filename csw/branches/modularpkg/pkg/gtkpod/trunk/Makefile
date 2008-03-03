GARNAME = gtkpod
GARVERSION = 0.99.12
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
DISTFILES += $(call admfiles,CSWgtkpod)
PATCHFILES  = file_convert.diff

GARCOMPILER = GNU

LIBDEPS += lib/libgpod

#libgpod uses a non-standard include path
EXTRA_INC=$(DESTDIR)/opt/csw/include/gpod-1.0

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
LDFLAGS += -lvorbis

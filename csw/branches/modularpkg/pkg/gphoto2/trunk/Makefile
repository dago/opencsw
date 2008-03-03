GARNAME = gphoto2
GARVERSION = 2.3.1
CATEGORIES = utils

DESCRIPTION = gphoto2 is a command-line frontend to libgphoto2
define BLURB
  gPhoto2 is a free, redistributable, ready to use digital camera
  command-line application for Unix-like systems. It uses libgphoto2 and
  supports more than 700 cameras.
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgphoto2,prototype depend)
# 'cc' is a shell script to hack around libtool craziness
DISTFILES += cc

DEPENDS += lib/libgphoto2

PWD = $(shell pwd)
LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib
# Make sure we pick up libgphoto2 from our local installation rather than
# the system libraries
LIBGPHOTO2_CFLAGS = $(DESTDIR)$(includedir)/gphoto2
LIBGPHOTO2_LIBS = -L$(DESTDIR)$(libdir) -lgphoto2
LIBINTL = -lintl
INTLLIB = $(LIBINTL)

LIBGPHOTO_PATH = $(DESTDIR)$(libdir)
export LD_OPTIONS LIBGPHOTO2_CFLAGS LIBGPHOTO2_LIBS LIBINTL INTLLIB
export LIBGPHOTO_PATH

SUN_CPP_FLAGS = -D__EXTENSIONS__
EXTRA_INC = $(DESTDIR)$(includedir)/gphoto2
EXT_LDFLAGS = $(DESTDIR)$(libdir)

CONFIGURE_ARGS += $(DIRPATHS) --without-libintl-prefix

# gphoto2 doesn't have a test target
#TEST_TARGET =

SPKG_SOURCEURL = http://www.gphoto.org/

include gar/category.mk

# This ensures that make picks up the 'cc' shell script as compiler
PATH := $(PWD)/$(WORKDIR):$(PATH)
export PATH

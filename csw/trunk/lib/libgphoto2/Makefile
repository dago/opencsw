GARNAME = libgphoto2
GARVERSION = 2.2.1
CATEGORIES = lib

DESCRIPTION = libgphoto2 - libgphoto2 is a library that can be used by applications to access digital cameras
define BLURB
  libgphoto2 is the core library designed to allow access to digital camera
  by external programs. It abstracts communication ports and camera
  protocol, to allow a complete modularity.
endef

PATCHFILES = sunstudio.patch

MASTER_SITES = http://www.gphoto.org/proj/libgphoto2/
#MASTER_SITES = http://superb-west.dl.sourceforge.net/sourceforge/gphoto/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibgphoto2,prototype depend)
DISTFILES += sunstudio.patch

CONFIGURE_ARGS = $(DIRPATHS) --with-libusb=no
#--with-exif-prefix=/opt/csw

# libgphoto2 doesn't have a test target
TEST_TARGET =

SPKG_SOURCEURL = http://www.gphoto.org/

include ../category.mk

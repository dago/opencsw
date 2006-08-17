GARNAME = libgphoto2
GARVERSION = 2.2.1
CATEGORIES = lib

DESCRIPTION = libgphoto2 - libgphoto2 is a library that can be used by applications to access digital cameras
define BLURB
  libgphoto2 is the core library designed to allow access to digital camera
  by external programs. It abstracts communication ports and camera
  protocol, to allow a complete modularity.
endef

MASTER_SITES = http://www.gphoto.org/proj/libgphoto2/
#MASTER_SITES = http://superb-west.dl.sourceforge.net/sourceforge/gphoto/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibgphoto2,)

CONFIGURE_ARGS = $(DIRPATHS) --with-libusb=no
#--with-exif-prefix=/opt/csw

# Remove the following rules and uncomment the
# include before building.

include ../category.mk

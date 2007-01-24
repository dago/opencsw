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

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibgphoto2,prototype depend)
DISTFILES += sunstudio.patch

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

LIBUSB_LIBS="-L/usr/sfw/lib -R/usr/sfw/lib -lusb"
LIBUSB_CFLAGS=-I/usr/sfw/include

export LIBUSB_LIBS
export LIBUSB_CFLAGS

CONFIGURE_ARGS = $(DIRPATHS)
#--with-libusb=no
#--with-exif-prefix=/opt/csw

# libgphoto2 doesn't have a test target
TEST_TARGET =

SPKG_SOURCEURL = http://www.gphoto.org/

include ../category.mk

post-configure:
	(cd $(WORKSRC); \
	test -d $(DESTDIR)/opt/csw/include || mkdir -p $(DESTDIR)/opt/csw/include \
	cp -pr gphoto2 $(DESTDIR)/opt/csw/include)

GARNAME = libgphoto2
GARVERSION = 2.3.1
CATEGORIES = lib

DESCRIPTION = libgphoto2 - library to be used by applications to access digital cameras
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

LIBUSB_LIBS=-L/usr/sfw/lib -R/usr/sfw/lib -lusb
LIBUSB_CFLAGS=-I/usr/sfw/include

# We need these directories in EXTRA_INC to make sure they appear before
# -I/opt/csw/include in CFLAGS. While 'configure' does make sure to add
# these directories to CFLAGS, it does so after -I/opt/csw/include, which
# means the build is at risk of picking up system installed (i.e. older)
# libgphoto2 includes from /opt/csw/include first.
EXTRA_INC=../.. ../../libgphoto2_port ../libgphoto2_port/gphoto2

export LIBUSB_LIBS
export LIBUSB_CFLAGS
#export EXTRA_INC

OS_RELEASE=`uname -r`

CONFIGURE_ARGS = $(DIRPATHS)
ifeq ($OS_REL, 5.8)
	CONFIGURE_ARGS += --with-libusb=no
endif
#--with-exif-prefix=/opt/csw

# libgphoto2 doesn't have a test target
TEST_TARGET =

SPKG_SOURCEURL = http://www.gphoto.org/

include ../category.mk

post-configure:
	(cd $(WORKSRC); \
	test -d $(DESTDIR)/opt/csw/include || mkdir -p $(DESTDIR)/opt/csw/include \
	cp -pr gphoto2 $(DESTDIR)/opt/csw/include;\
	cp -pr libgphoto2_port/gphoto2 $(DESTDIR)/opt/csw/include)

#post-build:
#	rm -rf $(DESTDIR)/opt/csw/include

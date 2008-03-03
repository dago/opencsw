GARNAME = libgphoto2
GARVERSION = 2.3.1
CATEGORIES = lib

DESCRIPTION = library to be used by applications to access digital cameras
define BLURB
  libgphoto2 is the core library designed to allow access to digital camera
  by external programs. It abstracts communication ports and camera
  protocol, to allow a complete modularity.
endef

PATCHFILES = sunstudio.patch

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibgphoto2,depend \
	prototype.i386.sol10 prototype.i386.sol8 \
	prototype.sparc.sol10 prototype.sparc.sol8)
DISTFILES += sunstudio.patch
# 'cc' is a shell script to hack around libtool craziness
DISTFILES += cc

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

# We need these directories in EXTRA_INC to make sure they appear before
# -I/opt/csw/include in CFLAGS. While 'configure' does make sure to add
# these directories to CFLAGS, it does so after -I/opt/csw/include, which
# means the build is at risk of picking up system installed (i.e. older)
# libgphoto2 includes from /opt/csw/include first.
EXTRA_INC=../.. ../../libgphoto2_port ../libgphoto2_port/gphoto2

#export EXTRA_INC

LIBGPHOTO_PATH = $(DESTDIR)$(libdir)
export LIBGPHOTO_PATH

CONFIGURE_ARGS = $(DIRPATHS)

# This is a bit of a hack. If I find a nicer way of doing this, I'll re-
# implement it.
OS_RELEASE=$(shell uname -r | sed -e 's/^5\.//')
OS_PLATFORM=$(shell uname -p)
SUPPORT_USB=$(shell if [ $(OS_RELEASE) -ge 10 ]; then echo 1; else echo 0; fi)

ifeq ($(SUPPORT_USB), 0)
	CONFIGURE_ARGS += --with-libusb=no
else
	LIBUSB_LIBS=-L/usr/sfw/lib -R/usr/sfw/lib -lusb
	LIBUSB_CFLAGS=-I/usr/sfw/include
	export LIBUSB_LIBS
	export LIBUSB_CFLAGS
endif

PROTOTYPE=CSW$(GARNAME).prototype.$(OS_PLATFORM).sol$(OS_RELEASE)

#--with-exif-prefix=/opt/csw

# libgphoto2 doesn't have a test target
TEST_TARGET =

SPKG_SOURCEURL = http://www.gphoto.org/

include gar/category.mk

# This ensures that make picks up the 'cc' shell script as compiler
#PATH := $(PWD)/$(WORKDIR):$(PATH)
#export PATH

post-extract:
	(cd $(WORKSRC)/..; \
	rm -f CSW$(GARNAME).prototype; \
	ln -s $(PROTOTYPE) CSW$(GARNAME).prototype)

post-configure:
	(cd $(WORKSRC); \
	test -d $(DESTDIR)/opt/csw/include || mkdir -p $(DESTDIR)/opt/csw/include; \
	cp -pr gphoto2 $(DESTDIR)/opt/csw/include;\
	cp -p libgphoto2_port/gphoto2/*.h $(DESTDIR)/opt/csw/include/gphoto2)

#post-build:
#	rm -rf $(DESTDIR)/opt/csw/include

post-install:
	cp -p files/README.CSW $(DESTDIR)/opt/csw/share/doc/libgphoto2
	cp -p files/solaris-10-usb-digital-camera-howto.txt $(DESTDIR)/opt/csw/share/doc/libgphoto2

GARNAME = x11vnc
GARVERSION = 0.9.9
CATEGORIES = apps

DESCRIPTION = Allows one to view remotely and interact with real X displays
define BLURB
endef

SF_PROJ = libvncserver
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.karlrunge.com/x11vnc/

BUILD_DEP_PKGS = CSWossldevel CSWzlib CSWjpeg
RUNTIME_DEP_PKGS = CSWosslrt CSWzlib CSWjpeg

PACKAGING_PLATFORMS  = solaris8-sparc solaris8-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# This is to make sure the X11 path is prepended to the front of lib pathes.
# Otherwise the wrong X11 gets picked up.
EXTRA_LIB_garosrel-5.8  = /usr/openwin/lib
# We can't add /usr/sfw/lib because then openssl is pickedup from there too.
#EXTRA_LIB_garosrel-5.10 = /usr/X11/lib /usr/sfw/lib
EXTRA_LIB_garosrel-5.10 = /usr/X11/lib
EXTRA_LIB = $(EXTRA_LIB_garosrel-$(GAROSREL))

CONFIGURE_ARGS_garosrel-5.8  = --x-includes=/usr/openwin/include
CONFIGURE_ARGS_garosrel-5.8 += --x-libraries=/usr/openwin/lib 
CONFIGURE_ARGS_garosrel-5.10  = --x-includes=/usr/X11/include
CONFIGURE_ARGS_garosrel-5.10 += --x-libraries=/usr/X11/lib 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_garosrel-$(GAROSREL))

TEST_TARGET = check

include gar/category.mk

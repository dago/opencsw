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

# This is to make sure the X11 path is prepended to the front of lib pathes.
# Otherwise the wrong X11 gets picked up.
EXTRA_LIB = /usr/openwin/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib

TEST_TARGET = check

include gar/category.mk

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
RUNTIME_DEP_PKGS += CSWlibx11 CSWlibxdamage CSWlibxext CSWlibxfixes CSWlibxinerama CSWlibxtst

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

include gar/category.mk

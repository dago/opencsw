NAME = x11vnc
VERSION = 0.9.12
CATEGORIES = apps

DESCRIPTION = Allows one to view remotely and interact with real X displays
define BLURB
endef

SF_PROJ = libvncserver
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.karlrunge.com/x11vnc/

BUILD_DEP_PKGS = CSWossldevel CSWzlib CSWjpeg
RUNTIME_DEP_PKGS = CSWosslrt CSWzlib CSWjpeg

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

NAME = system-tray-applet
VERSION = 0.15
GARTYPE = v1
CATEGORIES = gnome

DESCRIPTION = Gnome 2 System Tray Applet
define BLURB
  System tray for Gnome panel.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(VERSION)/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

# No test suite
TEST_SCRIPTS =

include gar/category.mk

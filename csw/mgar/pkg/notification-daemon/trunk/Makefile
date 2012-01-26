NAME = notification-daemon
VERSION = 0.3.7
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = Daemon to aid libnotify
define BLURB
endef

MASTER_SITES = http://www.galago-project.org/files/releases/source/notification-daemon/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bzw

VENDOR_URL = http://www.galago-project.org

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

GARNAME = gnome-panel
GARVERSION = 0.15
CATEGORIES = gnome

DESCRIPTION = Gnome 2 Panel
define BLURB
  Gnome panel.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(GARNAME)/$(GARVERSION)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

LIBDEPS += gnome/system-tray-applet

CONFIGURE_ARGS = $(DIRPATHS)

# No test suite
ENABLE_TEST = 0

include ../category.mk

GARNAME = hicolor-icon-theme
GARVERSION = 0.5
CATEGORIES = xtra

DESCRIPTION = Default Gtk icon theme.
define BLURB
  Default Gtk icon theme.
endef

MASTER_SITES = http://freedesktop.org/Software/icon-theme/releases/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS)
INSTALL_ARGS = -j1

# No test suite for icons
TEST_SCRIPTS =

include ../category.mk

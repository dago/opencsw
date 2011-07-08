NAME = hicolor-icon-theme
VERSION = 0.5
GARTYPE = v1
CATEGORIES = xtra

DESCRIPTION = Default Gtk icon theme.
define BLURB
  Default Gtk icon theme.
endef

MASTER_SITES = http://freedesktop.org/Software/icon-theme/releases/
DISTFILES = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS = $(WORKSRC)/configure
BUILD_SCRIPTS = $(WORKSRC)/Makefile
INSTALL_SCRIPTS = $(WORKSRC)/Makefile

CONFIGURE_ARGS = $(DIRPATHS)
INSTALL_ARGS = -j1

# No test suite for icons
TEST_SCRIPTS =

include gar/category.mk

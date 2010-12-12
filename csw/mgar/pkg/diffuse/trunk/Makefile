NAME = diffuse
VERSION = 0.4.1
CATEGORIES = utils

DESCRIPTION = Graphical tool for comparing and merging text files
define BLURB
  Graphical tool for comparing and merging text files
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

RUNTIME_DEP_PKGS = CSWpython CSWpygtk
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo "Installing $(NAME) (custom)"
	( cd $(WORKSRC); \
          ./install.py --destdir=$(DESTDIR) --prefix=/opt/csw  --sysconfdir=/etc/opt/csw --mandir=/opt/csw/share/man --files-only )
	@$(MAKECOOKIE)

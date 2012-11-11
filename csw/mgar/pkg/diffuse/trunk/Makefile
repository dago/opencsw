NAME       = diffuse
VERSION    = 0.4.5
GARTYPE = v2

DESCRIPTION = Graphical tool for comparing and merging text files
define BLURB
  Graphical tool for comparing and merging text files
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(NAME)-$(VERSION).tar.bz2

RUNTIME_DEP_PKGS  = CSWpython
RUNTIME_DEP_PKGS += CSWpygtk
ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

CHECKPKG_OVERRIDES_CSWdiffuse += surplus-dependency|CSWpygtk
CHECKPKG_OVERRIDES_CSWdiffuse += surplus-dependency|CSWpython
# This is in a comment
CHECKPKG_OVERRIDES_CSWdiffuse += file-with-bad-content|/usr/share|root/opt/csw/bin/diffuse

include gar/category.mk

install-custom:
	@echo "Installing $(NAME) (custom)"
	( cd $(WORKSRC); \
          ./install.py --destdir=$(DESTDIR) --prefix=/opt/csw  --sysconfdir=/etc/opt/csw --mandir=/opt/csw/share/man --files-only )
	@$(MAKECOOKIE)

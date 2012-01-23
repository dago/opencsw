NAME = eggdbus
VERSION = 0.6
CATEGORIES = lib

DESCRIPTION = D-Bus bindings for GObject
define BLURB
EggDBus aims to be an easy-to-use set of GObject bindings for interacting
with DBus.  Currently, this interaction is done using libdbus-1 but that
is subject to change.
endef

VENDOR_URL = http://cgit.freedesktop.org/~david/eggdbus
MASTER_SITES = http://cgit.freedesktop.org/~david/eggdbus/snapshot/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibeggdbus CSWlibeggdbusdevel
CATALOGNAME_CSWlibeggdbus = libeggdbus
CATALOGNAME_CSWlibeggdbusdevel = libeggdbus_devel
SPKG_DESC_CSWlibeggdbus = $(DESCRIPTION)
SPKG_DESC_CSWlibeggdbusdevel = $(DESCRIPTION) - developer package

RUNTIME_DEP_PKGS_CSWlibeggdbus += CSWdbusglib
RUNTIME_DEP_PKGS_CSWlibeggdbus += CSWglib2
RUNTIME_DEP_PKGS_CSWlibeggdbus += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibeggdbus += CSWlibdbus
RUNTIME_DEP_PKGS_CSWlibeggdbusdevel += CSWlibeggdbus

PREREQUISITE_PKGS += $(REQUIRED_PKGS_CSWlibeggdbus)

CHECKPKG_OVERRIDES_CSWlibeggdbusdevel += surplus-dependency|CSWlibeggdbus

PKGFILES_CSWlibeggdbusdevel = $(PKGFILES_DEVEL)

# libdbus isn't 64-bit yet
#BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@( cd $(WORKSRC) ; ./autogen.sh )
	@$(MAKECOOKIE)

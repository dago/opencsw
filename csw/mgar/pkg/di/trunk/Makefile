NAME = di
VERSION = 4.26
CATEGORIES = utils

DESCRIPTION = Disk information utility
define BLURB
  'di' is a disk information utility, displaying everything (and more)
  that your 'df' command does. It features the ability to display your
  disk usage in whatever format you desire/prefer/are used to. It is
  designed to be portable across many platforms.
endef

MASTER_SITES = http://www.gentoo.com/di/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWggettextrt

LICENSE = LICENSE

CONFIGURE_SCRIPTS = 

TEST_SCRIPTS =

INSTALL_OVERRIDE_DIRS = prefix

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)

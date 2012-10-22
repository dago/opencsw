NAME = di
VERSION = 4.32
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Disk information utility
define BLURB
  'di' is a disk information utility, displaying everything (and more)
  that your 'df' command does. It features the ability to display your
  disk usage in whatever format you desire/prefer/are used to. It is
  designed to be portable across many platforms.
endef

MASTER_SITES = http://www.gentoo.com/di/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS_CSWdi += CSWlibintl8

LICENSE = LICENSE

PACKAGING_PLATFORMS  = solaris9-sparc solaris9-i386
# Make extra packages for Solaris 10 as di is zone-aware
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

CONFIGURE_SCRIPTS = 

# Make sure the locale is configured to the right directory
BUILD_OVERRIDE_VARS = prefix
BUILD_OVERRIDE_VAR_prefix = $(prefix)

TEST_SCRIPTS =

INSTALL_OVERRIDE_DIRS = prefix

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)

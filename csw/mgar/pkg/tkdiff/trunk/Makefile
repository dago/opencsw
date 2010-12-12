NAME = tkdiff
VERSION = 4.1.4
CATEGORIES = utils

DESCRIPTION = A graphical diff tool
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(NAME)-$(VERSION)-unix
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES = force-csw-wish.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-unix.tar.gz

DEP_PKGS = CSWtk

VENDOR_URL = http://tkdiff.sourceforge.net/

BUILD_SCRIPTS =
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/tkdiff $(DESTDIR)$(bindir)/tkdiff
	@$(MAKECOOKIE)

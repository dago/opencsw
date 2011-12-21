NAME = tkdiff
VERSION = 4.2
CATEGORIES = utils

DESCRIPTION = A graphical diff tool
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(NAME)-$(VERSION).tar.gz
DISTNAME = tkdiff-unix
PATCHFILES += force-csw-wish.patch

VENDOR_URL = http://tkdiff.sourceforge.net/

LICENSE = LICENSE.txt

PACKAGES += CSWtkdiff
SPKG_DESC_CSWtkdiff = A graphical diff tool
# PKGFILES is catchall
ARCHALL_CSWtkdiff = 1
# We need "wish" from CSWtk which is not detected by checkpkg
RUNTIME_DEP_PKGS_CSWtkdiff += CSWtk
CHECKPKG_OVERRIDES_CSWtkdiff += surplus-dependency|CSWtk

BUILD_SCRIPTS =
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/tkdiff $(DESTDIR)$(bindir)/tkdiff
	@$(MAKECOOKIE)

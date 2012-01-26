NAME = svclog
VERSION = 1.5
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Displays log file content for SMF services
define BLURB
  Long description
endef

VENDOR_URL   = http://www2.petervg.nl/software/source/svclog
MASTER_SITES = http://www2.petervg.nl/software/source/
DISTFILES    = svclog
DISTFILES   += COPYING

ARCHALL = 1

# Only makes sense on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Simple script copy, none of the usual steps required
EXTRACT_SCRIPTS   =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

include gar/category.mk

install-custom:
	ginstall -Dm755 $(WORKDIR)/svclog $(DESTDIR)$(bindir)/svclog
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)

install-changelog-%:
	ginstall -Dm 644 $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)

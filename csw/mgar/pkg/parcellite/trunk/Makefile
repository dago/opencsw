GARNAME = parcellite
GARVERSION = 0.9.2
CATEGORIES = utils

DESCRIPTION = Lightweight GTK+ clipboard manager
define BLURB
  Parcellite is a stripped down, basic-features-only clipboard manager
  with a small memory footprint for those who like simplicity. 
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz

# There's no test suite
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

# Not quite sure why "pkg-config gtk+-2.0 --libs" doesn't yield -lX11 also
EXTRA_LDFLAGS = -lX11

include gar/category.mk

# Requires GNU gettext
PATH := /opt/csw/gnu:$(PATH)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)

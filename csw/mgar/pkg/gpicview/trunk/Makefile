# TODO (release-critical prefixed with !, non release-critical with *)
NAME = gpicview
VERSION = 0.2.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A Simple and Fast Image Viewer for X
define BLURB
endef

VENDOR_URL   = http://lxde.sourceforge.net/gpicview/
MASTER_SITES = $(ECTSF_MIRRORS)
SF_PROJ      = lxde
DISTFILES    = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS += CSWlibatk
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWfconfig
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWgtk2
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWjpeg

# No test suite available
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LDFLAGS  = -lm -lX11

include gar/category.mk

# Requires GNU gettext in PATH
PATH := $(prefix)/gnu:$(PATH)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.C
NAME = Pango
VERSION = 1.221
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TSCH

DESCRIPTION = Layout and render international text
define BLURB
  Layout and render international text
endef

PACKAGES = CSWpmpango
CATALOGNAME = pm_pango

LICENSE = LICENSE

RUNTIME_DEP_PKGS = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWlibcairo CSWpango
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

include gar/category.mk

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(prefix)/share/checkpkg/overrides
	echo "CSWpmpango: symbol-not-found" \
	  > $(PKGROOT)$(prefix)/share/checkpkg/overrides/$(CATALOGNAME)
	@$(MAKECOOKIE)


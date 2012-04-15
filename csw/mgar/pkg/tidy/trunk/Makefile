# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tidy
VERSION = 20090325cvs
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = An HTML Syntax Checker and Reformatter
define BLURB
An HTML Syntax Checker and Reformatter
endef

MASTER_SITES = http://tidy.sourceforge.net
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-correct-the-path-to-tidy-for-use-by-tests.patch

LICENSE = LICENSE

PACKAGES = CSWtidy CSWlibtidy0-99 CSWtidy-dev

OBSOLETED_BY_CSWtidy = CSWhtmltidy

SPKG_DESC_CSWtidy = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWtidy = CSWlibtidy0-99

SPKG_DESC_CSWtidy-dev = Development files for libtidy
RUNTIME_DEP_PKGS_CSWtidy-dev = CSWlibtidy0-99

SPKG_DESC_CSWlibtidy0-99 = Tidy, libtidy-0.99.so

PKGFILES_CSWtidy-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibtidy0-99 = $(call baseisadirs,$(libdir),libtidy-0\.99\.so(\.\d+)*)

include gar/category.mk

pre-configure-modulated:
	@(cd $(WORKSRC); bash build/gnuauto/setup.sh; \
		lynx --dump htmldoc/license.html > LICENSE )
	@$(MAKECOOKIE)

test-modulated:
	@(cd $(WORKSRC)/test; ./testall.sh)
	@$(MAKECOOKIE)

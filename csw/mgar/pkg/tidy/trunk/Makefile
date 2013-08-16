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

MASTER_SITES = http://t/idy.sourceforge.net
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-correct-the-path-to-tidy-for-use-by-tests.patch

LICENSE = LICENSE

SPKG_DESC_CSWtidy = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWtidy = CSWlibtidy0-99-0
OBSOLETED_BY_CSWtidy = CSWhtmltidy
# Catchall

PACKAGES += CSWtidy-dev
SPKG_DESC_CSWtidy-dev = Development files for libtidy
PKGFILES_CSWtidy-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWtidy-dev += CSWlibtidy0-99-0

PACKAGES += CSWlibtidy0-99-0
CATALOGNAME_CSWlibtidy0-99-0 = libtidy0_99_0
PKGFILES_CSWlibtidy0-99-0 += $(call baseisadirs,$(libdir),libtidy-0\.99\.so\.0\.0\.0)
PKGFILES_CSWlibtidy0-99-0 += $(call baseisadirs,$(libdir),libtidy-0\.99\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibtidy0-99-0 += $(DESCRIPTION), libtidy-0.99.so.0
OBSOLETED_BY_CSWlibtidy0-99-0 += CSWlibtidy0-99

BUILD64 = 1
ISAEXEC = 1-0\.99\.so(\.\d+)*)

include gar/category.mk

pre-configure-modulated:
	@(cd $(WORKSRC); bash build/gnuauto/setup.sh; \
		lynx --dump htmldoc/license.html > LICENSE )
	@$(MAKECOOKIE)

test-modulated:
	@(cd $(WORKSRC)/test; ./testall.s
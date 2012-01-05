# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = sfpC
VERSION = 0.6
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Solaris fingerprint companion
define BLURB
endef

MASTER_SITES = http://wesunsolve.net/downloads/
DISTNAME = $(NAME)-v$(VERSION)
DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += COPYING
PATCHFILES += 0001-Force-CSW-Perl.patch

PACKAGES += CSWwesunsolve-sfpc
SPKG_DESC_CSWwesunsolve-sfpc = Solaris fingerprint companion sfpc
RUNTIME_DEP_PKGS_CSWwesunsolve-sfpc += CSWperl
RUNTIME_DEP_PKGS_CSWwesunsolve-sfpc += CSWpm-libwww-perl
RUNTIME_DEP_PKGS_CSWwesunsolve-sfpc += CSWpm-html-parser
ARCHALL_CSWwesunsolve-sfpc = 1
# No Perl checks in checkpkg
CHECKPKG_OVERRIDES_CSWwesunsolve-sfpc += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWwesunsolve-sfpc += surplus-dependency|CSWpm-libwww-perl
CHECKPKG_OVERRIDES_CSWwesunsolve-sfpc += surplus-dependency|CSWpm-html-parser

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/sfpC.pl $(DESTDIR)$(bindir)/sfpc
	ginstall -d $(DESTDIR)$(docdir)/wesunsolve_sfpc
	ginstall -m 0644 $(WORKSRC)/README.* $(DESTDIR)$(docdir)/wesunsolve_sfpc/
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mirmon
VERSION = 2.9
GARTYPE = v2

DESCRIPTION = Monitor the status of mirrors

MASTER_SITES = http://www.staff.science.uu.nl/~penni101/mirmon/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.staff.science.uu.nl/~penni101/mirmon/
LICENSE = LICENSE

PACKAGES += CSWmirmon
SPKG_DESC_CSWmirmon = Monitor the status of mirrors
# PKGFILES is catchall
ARCHALL_CSWmirmon = 1
RUNTIME_DEP_PKGS_CSWmirmon += CSWperl
RUNTIME_DEP_PKGS_CSWmirmon += CSWrsync
RUNTIME_DEP_PKGS_CSWmirmon += CSWwget
CHECKPKG_OVERRIDES_CSWmirmon += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWmirmon += surplus-dependency|CSWrsync
CHECKPKG_OVERRIDES_CSWmirmon += surplus-dependency|CSWwget

PACKAGES += CSWpm-mirmon
SPKG_DESC_CSWpm-mirmon = OO interface for mirmon objects
ARCHALL_CSWpm-mirmon = 1
PKGFILES_CSWpm-mirmon += $(bindir)/mirmon.pl
PKGFILES_CSWpm-mirmon += $(sharedstatedir)/perl/.*
RUNTIME_DEP_PKGS_CSWpm-mirmon += CSWperl

# These are just examples
CHECKPKG_OVERRIDES_CSWmirmon += file-with-bad-content|/usr/local|root/opt/csw/bin/mirmon
CHECKPKG_OVERRIDES_CSWpm-mirmon += file-with-bad-content|/usr/local|root/opt/csw/bin/mirmon.pl

REINPLACEMENTS += perl
REINPLACE_MATCH_perl = /usr/bin/perl
REINPLACE_WITH_perl = $(bindir)/perl
REINPLACE_FILES_perl = *

REINPLACEMENTS += wget
REINPLACE_MATCH_wget = /usr/bin/wget
REINPLACE_WITH_wget = $(bindir)/wget
REINPLACE_FILES_wget += probe

REINPLACEMENTS += rsync
REINPLACE_MATCH_rsync = /usr/bin/rsync
REINPLACE_WITH_rsync = $(bindir)/rsync
REINPLACE_FILES_rsync += probe

REINPLACEMENTS += mirmonpm
REINPLACE_MATCH_mirmonpm = \\'\\.\\'
REINPLACE_WITH_mirmonpm = \\'$(sharedstatedir)/perl/csw\\'
REINPLACE_FILES_mirmonpm += mirmon.pl

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(PKGROOT)$(docdir)/mirmon
	cd $(WORKSRC) && ginstall -m 0644 RELEASE-NOTES $(PKGROOT)$(docdir)/mirmon
	ginstall -d $(PKGROOT)$(bindir)
	cd $(WORKSRC) && ginstall -m 0755 mirmon mirmon.pl probe $(PKGROOT)$(bindir)
	ginstall -d $(PKGROOT)$(mandir)/man1
	cd $(WORKSRC) && ginstall -m 0644 mirmon.1 mirmon.pm.1 $(PKGROOT)$(mandir)/man1
	ginstall -d $(PKGROOT)$(sharedstatedir)/mirmon
	cd $(WORKSRC) && cp -r countries.list icons $(PKGROOT)$(sharedstatedir)/mirmon
	ginstall -d $(PKGROOT)$(sharedstatedir)/perl/csw
	cd $(WORKSRC) && cp -r Mirmon.pm $(PKGROOT)$(sharedstatedir)/perl/csw
	@$(MAKECOOKIE)

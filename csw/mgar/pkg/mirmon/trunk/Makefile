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

# These are just examples
CHECKPKG_OVERRIDES_CSWmirmon += file-with-bad-content|/usr/local|root/opt/csw/bin/mirmon
CHECKPKG_OVERRIDES_CSWmirmon += file-with-bad-content|/usr/local|root/opt/csw/bin/mirmon.pl

REINPLACEMENTS += perl
REINPLACE_MATCH_perl = /usr/bin/perl
REINPLACE_WITH_perl = $(bindir)/perl
REINPLACE_FILES_perl = *

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
	@$(MAKECOOKIE)

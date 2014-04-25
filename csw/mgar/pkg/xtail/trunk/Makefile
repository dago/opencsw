# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xtail
VERSION = 2.1
GARTYPE = v2

DESCRIPTION = Watch the growth of files

MASTER_SITES += http://www.unicom.com/files/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += 20120219-patch-aalto.zip

VENDOR_URL = http://www.unicom.com/sw/xtail

# Package does not have a testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += bindir
INSTALL_OVERRIDE_VARS += mandir
INSTALL_OVERRIDE_VAR_bindir = $(DESTDIR)$(bindir)
INSTALL_OVERRIDE_VAR_mandir = $(DESTDIR)$(mandir)

include gar/category.mk

# Apple patches contained in 20120219-patch-aalto.zip
post-extract:
	cd $(WORKSRC) && gpatch -p1 < ../0001-Use-ISO8601-Fix-Gcc-header-Use-C-c.patch
	cd $(WORKSRC) && gpatch -p1 < ../0001-xtail.1-remove-SIGQUIT.patch
	cd $(WORKSRC) && gpatch -p1 < ../xtail_2.1-5-debian-local-changes.patch
	@$(MAKECOOKIE)

pre-install:
	ginstall -d -m 0755 $(DESTDIR)$(bindir)
	ginstall -d -m 0755 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)

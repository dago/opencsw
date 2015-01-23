# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = MigrationTools
VERSION = 47

DESCRIPTION = PADL LDAP Mirgation Tools

MASTER_SITES = http://www.padl.com/download/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWpadl-ldap-migration-tools
SPKG_DESC_CSWpadl-ldap-migration-tools = PADL LDAP Mirgation Tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpadl-ldap-migration-tools += CSWperl

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

REINPLACE_USRLOCAL += *\.pl
REINPLACE_USRLOCAL += *\.sh

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(prefix)/MigrationTools
	ginstall -m 0755 $(WORKSRC)/migrate_* $(DESTDIR)$(prefix)/MigrationTools
	@$(MAKECOOKIE)

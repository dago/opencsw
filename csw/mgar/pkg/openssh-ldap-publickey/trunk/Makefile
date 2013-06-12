# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = openssh-ldap-publickey
VERSION = 0.2
GARTYPE = v2

DESCRIPTION = Wrapper for OpenSSH to store public keys inside the OpenLDAP entry

GITHUB_USER = AndriiGrytsenko
MASTER_SITES = $(GITHUB_MIRROR)
DISTNAME = $(GITHUB_USER)-$(NAME)-51da7d8
DISTFILES = $(NAME)-$(VERSION)$(GITHUB_BALL_EXT)

PACKAGES += CSWopenssh-ldap-publickey
SPKG_DESC_CSWopenssh-ldap-publickey = Wrapper for OpenSSH to store public keys inside the OpenLDAP entry
RUNTIME_DEP_PKGS_CSWopenssh-ldap-publickey += CSWpm-ldap
CHECKPKG_OVERRIDES_CSWopenssh-ldap-publickey += surplus-dependency|CSWpm-ldap
ARCHALL_CSWopenssh-ldap-publickey = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

REINPLACEMENTS += cswperl
REINPLACE_MATCH_cswperl = /usr/bin/perl
REINPLACE_WITH_cswperl = $(bindir)/perl
REINPLACE_FILES_cswperl += bin/openssh-ldap-publickey

REINPLACEMENTS += ldapconf
REINPLACE_MATCH_ldapconf = /etc/ldap.conf
REINPLACE_WITH_ldapconf = $(sysconfdir)/ldap.conf
REINPLACE_FILES_ldapconf += bin/openssh-ldap-publickey

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/bin/openssh-ldap-publickey $(DESTDIR)$(bindir)/openssh-ldap-publickey
	ginstall -d $(PKGROOT)$(sysconfdir)/openldap/schema
	ginstall -m 0644 $(WORKSRC)/misc/openssh-lpk-openldap.schema $(PKGROOT)$(sysconfdir)/openldap/schema/openssh-lpk-openldap.schema
	ginstall -d $(PKGROOT)$(sharedstatedir)/doc/$(CATALOGNAME)
	ginstall -m 0644 $(WORKSRC)/README.md $(PKGROOT)$(sharedstatedir)/doc/$(CATALOGNAME)
	ginstall -d $(PKGROOT)$(mandir)/man8
	ginstall -m 0644 $(WORKSRC)/man/openssh-ldap-publickey.8 $(PKGROOT)$(mandir)/man8
	@$(MAKECOOKIE)

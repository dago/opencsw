GARNAME = smbldap-tools
GARVERSION = 0.9.4
CATEGORIES = utils

DESCRIPTION = smbldap-tools 
define BLURB
	smbldap-tools is a set of scripts designed to help integrate Samba 
	and a LDAP directory. They target both users and administrators of Unix systems.
endef

MASTER_SITES = http://download.gna.org/smbldap-tools/packages/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWsmbldap-tools,depend)

#PREREQUISITE_PKGS = CSWpmldap CSWpmdigestsha1 CSWpmunicodemap

PATCHFILES = header-confdir-fix.diff

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

install-custom:
	@mkdir -p $(DESTDIR)$(sbindir)
	@mkdir -p $(DESTDIR)$(sysconfdir)/smbldap-tools/
	@ginstall -m0755  $(WORKSRC)/smbldap-*  $(WORKSRC)/smbldap_tools.pm $(DESTDIR)$(sbindir)
	@ginstall -m0644  $(WORKSRC)/smbldap.conf $(DESTDIR)$(sysconfdir)/smbldap-tools/
	@ginstall -m0600  $(WORKSRC)/smbldap_bind.conf $(DESTDIR)$(sysconfdir)/smbldap-tools/


NAME = smbldap-tools
VERSION = 0.9.9
GARTYPE = v2

DESCRIPTION = Samba LDAP ToolsON = smbldap-tools 
define BLURB
	smbldap-tools is a set of scripts designed to help integrate Samba 
	and a LDAP directory. They target both users and administrators of Unix systems.
endef

MASTER_SITES = http://download.gnasources/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz


#BUILD_DEP_PKGS = CSWpmldap CSWpmdigestsha1 CSWpmunicodemap
ARCHALL_CSWsmbldap-tools = 1
RUNTIME_DEP_PKGS_CSWsmbldap-tools += CSWperl

REINPLACE_USRLOCAL += smbldap_tools.pm

REINPLACEMENTS += etc
REINPLACE_MATCH_etc = /etc/smbldap-tools
REINPLACE_WITH_etc = /etc/opt/csw/smbldap-tools
REINPLACE_FILES_etc += smbldap-* smbldap_tools.pm

# no check target
SKIPTEST = 1

include gar/category.mk

post-install-modulated:
	@ginstall -d -m755 $(DESTDIR)$(sysconfdir)/smbldap-tools/(DESTDIR)$(sbindir)
	@ginstall -m0644  $(WORKSRC)/smbldap.conf $(DESTDIR)$(sysconfdir)/smbldap-tools/
	@ginstall -m0600  $(WORKSRC)/smbldap_bind.conf $(DESTDIR)$(sysconfd	@$(MAKECOOKIES)

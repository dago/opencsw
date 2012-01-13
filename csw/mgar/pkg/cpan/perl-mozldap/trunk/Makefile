NAME = perl-mozldap
VERSION = 1.5.2
CATEGORIES = cpan

DESCRIPTION = Mozilla SDK based Lightweight Directory Access Protocol
define BLURB
This package offers a direct interface to the LDAP C API calls from Perl. It is used internally by the other Mozilla::LDAP modules. It is highly suggested that you use the object oriented interface in Mozilla::LDAP::Conn and Mozilla::LDAP::Entry unless you need to use asynchronous calls or other functionality not available in the OO interface.
endef

MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/directory/perldap/releases/$(VERSION)/src
DISTFILES = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE

LICENSE = LICENSE 

PACKAGES = CSWpm-mozldap
CATALOGNAME = pm_mozldap
SPKG_DESC_CSWpm-mozldap = $(DESCRIPTION)
GARCOMPILER = SOS12U2
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LDAPSDKLIBDIR = /opt/csw/lib
LDAPSDKINCDIR = /opt/csw/include/dirsrv
LDAPSDKSSL = Y
LDAPPR = Y
NSPRINCDIR = /opt/csw/include/nspr
NSPRLIBDIR = /opt/csw/lib
NSSLIBDIR = /opt/csw/lib

EXTRA_CONFIGURE_ENV = LDAPSDKDIR=$(prefix)
EXTRA_CONFIGURE_ENV += LDAPSDKLIBDIR=$(LDAPSDKLIBDIR)
EXTRA_CONFIGURE_ENV += LDAPSDKINCDIR=$(LDAPSDKINCDIR)
EXTRA_CONFIGURE_ENV += LDAPSDKSSL=$(LDAPSDKSSL)
EXTRA_CONFIGURE_ENV += LDAPPR=$(LDAPPR)
EXTRA_CONFIGURE_ENV += NSPRINCDIR=$(NSPRINCDIR)
EXTRA_CONFIGURE_ENV += NSPRLIBDIR=$(NSPRLIBDIR)
EXTRA_CONFIGURE_ENV += NSSLIBDIR=$(NSSLIBDIR)

CONFIGURE_ARGS =

RUNTIME_DEP_PKGS_CSWpm-mozldap += CSWlibprldap60
RUNTIME_DEP_PKGS_CSWpm-mozldap += CSWlibplc4
RUNTIME_DEP_PKGS_CSWpm-mozldap += CSWlibldap60
RUNTIME_DEP_PKGS_CSWpm-mozldap += CSWlibnss3
RUNTIME_DEP_PKGS_CSWpm-mozldap += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWpm-mozldap += CSWlibssldap60

include gar/category.mk

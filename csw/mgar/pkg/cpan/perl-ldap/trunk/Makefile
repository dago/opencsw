NAME = perl-ldap
VERSION = 0.4001
CATEGORIES = cpan
AUTHOR = GBARR

DESCRIPTION = Lightweight Directory Access Protocol
define BLURB
  Net::LDAP is a collection of modules that implements a LDAP services API for
  Perl programs. The module may be used to search directories or perform
  maintenance functions such as adding, deleting or modifying entries.
endef

DISTFILES  = COPYING
DISTFILES += CSWpm-ldap.releasenotes

PACKAGES = CSWpm-ldap
CATALOGNAME = pm_ldap
SPKG_DESC_CSWpm-ldap = $(DESCRIPTION)
ARCHALL = 1
OBSOLETES_CSWpm-ldap = CSWpmldap
CATALOGNAME_CSWpmldap = pm_ldap2

# Harmless /usr/local references
CHECKPKG_OVERRIDES_CSWpm-ldap += file-with-bad-content

RUNTIME_DEP_PKGS = CSWpmxmlsax CSWpmauthensasl CSWpmiosocketssl CSWpmuri CSWpmconvertasn1 CSWpmmimebase64

# Module version numbers defeat Sort::Versions
#MANUAL_UPDATE = 1

include gar/category.mk

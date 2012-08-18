NAME = perl-ldap
VERSION = 0.44
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MARSCHAP

DESCRIPTION = Lightweight Directory Access Protocol
define BLURB
  Net::LDAP is a collection of modules that implements a LDAP services API for
  Perl programs. The module may be used to search directories or perform
  maintenance functions such as adding, deleting or modifying entries.
endef

DISTFILES += COPYING
DISTFILES += CSWpm-ldap.releasenotes

PACKAGES = CSWpm-ldap
CATALOGNAME = pm_ldap
SPKG_DESC_CSWpm-ldap = $(DESCRIPTION)
ARCHALL = 1

# Name change
OBSOLETED_BY_CSWpm-ldap = CSWpmldap
CATALOGNAME_CSWpmldap = pm_ldap_stub

# Harmless /usr/local references
CHECKPKG_OVERRIDES_CSWpm-ldap += file-with-bad-content

RUNTIME_DEP_PKGS  = CSWpm-xml-sax
RUNTIME_DEP_PKGS += CSWpm-authen-sasl
RUNTIME_DEP_PKGS += CSWpm-io-socket-ssl
RUNTIME_DEP_PKGS += CSWpm-uri
RUNTIME_DEP_PKGS += CSWpmconvertasn1
RUNTIME_DEP_PKGS += CSWpm-mime-base64

# Module version numbers defeat Sort::Versions
#MANUAL_UPDATE = 1

include gar/category.mk

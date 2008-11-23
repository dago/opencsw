GARNAME = perl-ldap
GARVERSION = 0.34
CATEGORIES = cpan
AUTHOR = GBARR

DESCRIPTION = Lightweight Directory Access Protocol
define BLURB
  Net::LDAP is a collection of modules that implements a LDAP services API for
  Perl programs. The module may be used to search directories or perform
  maintenance functions such as adding, deleting or modifying entries.
endef

DISTFILES += CSWpmldap.gspec CSWpmldap.depend

DEPENDS += cpan/Convert-ASN1 cpan/IO-Socket-SSL
DEPENDS += cpan/Authen-SASL cpan/XML-SAX

# Module version numbers defeat Sort::Versions
MANUAL_UPDATE = 1

include gar/category.mk

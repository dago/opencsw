GARNAME = perl-ldap
GARVERSION = 0.39
CATEGORIES = cpan
AUTHOR = GBARR

DESCRIPTION = Lightweight Directory Access Protocol
define BLURB
  Net::LDAP is a collection of modules that implements a LDAP services API for
  Perl programs. The module may be used to search directories or perform
  maintenance functions such as adding, deleting or modifying entries.
endef

DISTFILES = COPYING

PACKAGES = CSWpmldap
CATALOGNAME = pm_ldap
ARCHALL = 1

REQUIRED_PKGS = CSWpmxmlsax CSWpmauthensasl CSWpmiosocketssl CSWpmuri CSWpmconvertasn1 CSWpmmimebase64

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DEPENDS += cpan/Convert-ASN1 cpan/IO-Socket-SSL
DEPENDS += cpan/Authen-SASL cpan/XML-SAX

# Module version numbers defeat Sort::Versions
#MANUAL_UPDATE = 1

include gar/category.mk

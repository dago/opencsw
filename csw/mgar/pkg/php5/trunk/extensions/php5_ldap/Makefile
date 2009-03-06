PHP5EXT_NAME = ldap

PACKAGES += CSWphp5ldap

CATALOGNAME_CSWphp5ldap = php5_ldap
SPKG_DESC_CSWphp5ldap = ldap Extention for PHP5
REQUIRED_PKGS_CSWphp5ldap = CSWphp5 CSWoldaprt CSWsasl

CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)

PKGFILES_CSWphp5ldap = .*/lib/php/extensions/.*/ldap.*

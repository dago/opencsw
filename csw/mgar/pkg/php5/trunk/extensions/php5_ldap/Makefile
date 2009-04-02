PHP5EXT_NAME = ldap

PACKAGES += CSWphp5ldap

CATALOGNAME_CSWphp5ldap = php5_ldap
SPKG_DESC_CSWphp5ldap = ldap Extention for PHP5
REQUIRED_PKGS_CSWphp5ldap = CSWphp5 CSWoldaprt CSWsasl

CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)

PKGFILES_CSWphp5ldap = .*/lib/php/extensions/.*/ldap.*


define CSWphp5ldap_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling ldap extension"

perl -i -plne 's|;extension=ldap.so|extension=ldap.so|' ${PHP_INI}

exit 0
endef

define CSWphp5ldap_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ldap extension"

perl -i -plne 's|extension=ldap.so|;extension=ldap.so|' ${PHP_INI}

exit 0
endef


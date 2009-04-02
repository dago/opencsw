PHP5EXT_NAME = snmp

PACKAGES += CSWphp5snmp

CATALOGNAME_CSWphp5snmp = php5_snmp
SPKG_DESC_CSWphp5snmp = snmp Extention for PHP5
REQUIRED_PKGS_CSWphp5snmp = CSWphp5 CSWnetsnmp CSWosslrt CSWtcpwrap

CONFIGURE_ARGS += --with-snmp=shared,$(prefix)

PKGFILES_CSWphp5snmp = .*/lib/php/extensions/.*/snmp.*

define CSWphp5snmp_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling snmp extension"

perl -i -plne 's|;extension=snmp.so|extension=snmp.so|' ${PHP_INI}

exit 0
endef

define CSWphp5snmp_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling snmp extension"

perl -i -plne 's|extension=snmp.so|;extension=snmp.so|' ${PHP_INI}

exit 0
endef


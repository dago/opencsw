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

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"snmp\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=snmp.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=snmp.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=snmp.so|extension=snmp.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=snmp.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"snmp\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5snmp_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling snmp extension"

perl -i -plne 's|extension=snmp.so|;extension=snmp.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"snmp\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

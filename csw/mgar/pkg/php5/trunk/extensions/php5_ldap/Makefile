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

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "ldap"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=ldap.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=ldap.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=ldap.so|extension=ldap.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=ldap.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "ldap"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5ldap_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ldap extension"

perl -i -plne 's|extension=ldap.so|;extension=ldap.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "ldap"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

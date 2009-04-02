PHP5EXT_NAME = openssl

PACKAGES += CSWphp5openssl

CATALOGNAME_CSWphp5openssl = php5_openssl
SPKG_DESC_CSWphp5openssl = openssl Extention for PHP5
REQUIRED_PKGS_CSWphp5openssl = CSWphp5 CSWosslrt CSWkrb5lib

CONFIGURE_ARGS += --with-openssl=shared,$(prefix)

PKGFILES_CSWphp5openssl = .*/lib/php/extensions/.*/openssl.*

define CSWphp5openssl_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling openssl extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"openssl\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=openssl.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=openssl.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=openssl.so|extension=openssl.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=openssl.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"openssl\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5openssl_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling openssl extension"

perl -i -plne 's|extension=openssl.so|;extension=openssl.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"openssl\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = mcrypt

PACKAGES += CSWphp5mcrypt

CATALOGNAME_CSWphp5mcrypt = php5_mcrypt
SPKG_DESC_CSWphp5mcrypt = mcrypt Extention for PHP5
REQUIRED_PKGS_CSWphp5mcrypt = CSWphp5 CSWlibmcrypt CSWlibtoolrt

CONFIGURE_ARGS += --with-mcrypt=shared,$(prefix)

PKGFILES_CSWphp5mcrypt = .*/lib/php/extensions/.*/mcrypt.*

define CSWphp5mcrypt_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mcrypt extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "mcrypt"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=mcrypt.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=mcrypt.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=mcrypt.so|extension=mcrypt.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=mcrypt.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "mcrypt"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5mcrypt_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mcrypt extension"

perl -i -plne 's|extension=mcrypt.so|;extension=mcrypt.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "mcrypt"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

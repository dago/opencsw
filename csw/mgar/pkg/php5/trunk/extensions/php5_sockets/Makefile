PHP5EXT_NAME = sockets

PACKAGES += CSWphp5sockets

CATALOGNAME_CSWphp5sockets = php5_sockets
SPKG_DESC_CSWphp5sockets = sockets Extention for PHP5
REQUIRED_PKGS_CSWphp5sockets = CSWphp5

CONFIGURE_ARGS += --enable-sockets=shared

PKGFILES_CSWphp5sockets = .*/lib/php/extensions/.*/sockets.*

define CSWphp5sockets_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sockets extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "sockets"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=sockets.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=sockets.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=sockets.so|extension=sockets.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=sockets.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "sockets"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5sockets_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sockets extension"

perl -i -plne 's|extension=sockets.so|;extension=sockets.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "sockets"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = posix

PACKAGES += CSWphp5posix

CATALOGNAME_CSWphp5posix = php5_posix
SPKG_DESC_CSWphp5posix = posix Extention for PHP5
REQUIRED_PKGS_CSWphp5posix = CSWphp5

CONFIGURE_ARGS += --enable-posix=shared

PKGFILES_CSWphp5posix = .*/lib/php/extensions/.*/posix.*

define CSWphp5posix_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling posix extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "posix"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=posix.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=posix.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=posix.so|extension=posix.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=posix.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "posix"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5posix_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling posix extension"

perl -i -plne 's|extension=posix.so|;extension=posix.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "posix"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

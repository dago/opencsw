PHP5EXT_NAME = shmop

PACKAGES += CSWphp5shmop

CATALOGNAME_CSWphp5shmop = php5_shmop
SPKG_DESC_CSWphp5shmop = shmop Extention for PHP5
REQUIRED_PKGS_CSWphp5shmop = CSWphp5

CONFIGURE_ARGS += --enable-shmop=shared

PKGFILES_CSWphp5shmop = .*/lib/php/extensions/.*/shmop.*

define CSWphp5shmop_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling shmop extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"shmop\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=shmop.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=shmop.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=shmop.so|extension=shmop.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=shmop.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"shmop\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5shmop_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling shmop extension"

perl -i -plne 's|extension=shmop.so|;extension=shmop.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"shmop\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

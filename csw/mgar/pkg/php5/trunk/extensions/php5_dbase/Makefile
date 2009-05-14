PHP5EXT_NAME = dbase

PACKAGES += CSWphp5dbase

CATALOGNAME_CSWphp5dbase = php5_dbase
SPKG_DESC_CSWphp5dbase = dbase Extention for PHP5
REQUIRED_PKGS_CSWphp5dbase = CSWphp5

CONFIGURE_ARGS += --enable-dbase=shared

PKGFILES_CSWphp5dbase = .*/lib/php/extensions/.*/dbase.*

define CSWphp5dbase_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling dbase extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "dbase"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=dbase.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=dbase.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=dbase.so|extension=dbase.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=dbase.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "dbase"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5dbase_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling dbase extension"

perl -i -plne 's|extension=dbase.so|;extension=dbase.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "dbase"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = pdoodbc

PACKAGES += CSWphp5pdoodbc

CATALOGNAME_CSWphp5pdoodbc = php5_pdoodbc
SPKG_DESC_CSWphp5pdoodbc = ODBC PHP Data Object Abstraction Extention for PHP5
REQUIRED_PKGS_CSWphp5pdoodbc = CSWphp5 CSWunixodbc CSWphp5pdo

CONFIGURE_ARGS += --with-pdo-odbc=shared,unixODBC,$(prefix)

PKGFILES_CSWphp5pdoodbc = .*/lib/php/extensions/.*/pdo_odbc.*

define CSWphp5pdoodbc_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdo_odbc extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "pdo_odbc"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pdo_odbc.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pdo_odbc.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pdo_odbc.so|extension=pdo_odbc.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pdo_odbc.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "pdo_odbc"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pdoodbc_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdo_odbc extension"

perl -i -plne 's|extension=pdo_odbc.so|;extension=pdo_odbc.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "pdo_odbc"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

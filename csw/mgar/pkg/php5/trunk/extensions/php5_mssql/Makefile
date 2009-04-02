PHP5EXT_NAME = mssql

PACKAGES += CSWphp5mssql

CATALOGNAME_CSWphp5mssql = php5_mssql
SPKG_DESC_CSWphp5mssql = mssql Extention for PHP5
REQUIRED_PKGS_CSWphp5mssql = CSWphp5 CSWfreetds

CONFIGURE_ARGS += --with-mssql=shared,$(prefix)

PKGFILES_CSWphp5mssql = .*/lib/php/extensions/.*/mssql.*

define CSWphp5mssql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mssql extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"mssql\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=mssql.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=mssql.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=mssql.so|extension=mssql.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=mssql.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"mssql\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5mssql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mssql extension"

perl -i -plne 's|extension=mssql.so|;extension=mssql.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"mssql\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

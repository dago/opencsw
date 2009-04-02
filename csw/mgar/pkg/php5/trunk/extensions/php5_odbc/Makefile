PHP5EXT_NAME = odbc

PACKAGES += CSWphp5odbc

CATALOGNAME_CSWphp5odbc = php5_odbc
SPKG_DESC_CSWphp5odbc = odbc Extention for PHP5
REQUIRED_PKGS_CSWphp5odbc = CSWphp5 CSWunixodbc

PATCHFILES += odbc.diff

CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)

PKGFILES_CSWphp5odbc = .*/lib/php/extensions/.*/odbc.*

define CSWphp5odbc_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling odbc extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"odbc\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=odbc.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=odbc.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=odbc.so|extension=odbc.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=odbc.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"odbc\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5odbc_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling odbc extension"

perl -i -plne 's|extension=odbc.so|;extension=odbc.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"odbc\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

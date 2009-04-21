PHP5EXT_NAME = pdomysql

PACKAGES += CSWphp5pdomysql

CATALOGNAME_CSWphp5pdomysql = php5_pdomysql
SPKG_DESC_CSWphp5pdomysql = A MySQL specific database access abstraction module for PHP applications
REQUIRED_PKGS_CSWphp5pdomysql = CSWphp5 CSWmysql5rt CSWzlib CSWphp5pdo

CONFIGURE_ARGS += --with-pdo-mysql=shared,$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

PKGFILES_CSWphp5pdomysql = .*/lib/php/extensions/.*/pdo_mysql.*

define CSWphp5pdomysql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdo_mysql extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "pdo_mysql"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pdo_mysql.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pdo_mysql.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pdo_mysql.so|extension=pdo_mysql.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pdo_mysql.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "pdo_mysql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pdomysql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdo_mysql extension"

perl -i -plne 's|extension=pdo_mysql.so|;extension=pdo_mysql.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "pdo_mysql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

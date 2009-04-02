PHP5EXT_NAME = mysql

PACKAGES += CSWphp5mysql

CATALOGNAME_CSWphp5mysql = php5_mysql
SPKG_DESC_CSWphp5mysql = mysql Extention for PHP5
REQUIRED_PKGS_CSWphp5mysql = CSWphp5 CSWmysql5rt

CONFIGURE_ARGS += --with-mysql=shared,$(prefix)

PKGFILES_CSWphp5mysql = .*/lib/php/extensions/.*/mysql\.so
PKGFILES_CSWphp5mysql += .*/lib/php/extensions/.*/mysql\.a

define CSWphp5mysql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mysql extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "mysql"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=mysql.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=mysql.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=mysql.so|extension=mysql.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=mysql.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "mysql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5mysql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mysql extension"

perl -i -plne 's|extension=mysql.so|;extension=mysql.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "mysql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

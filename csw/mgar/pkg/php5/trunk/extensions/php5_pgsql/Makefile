PHP5EXT_NAME = pgsql

PACKAGES += CSWphp5pgsql

CATALOGNAME_CSWphp5pgsql = php5_pgsql
SPKG_DESC_CSWphp5pgsql = pgsql Extention for PHP5
REQUIRED_PKGS_CSWphp5pgsql = CSWphp5 CSWlibpq

PATCHFILES += pgsql.diff

CONFIGURE_ARGS += --with-pgsql=shared,$(prefix)/postgresql

PKGFILES_CSWphp5pgsql = .*/lib/php/extensions/.*/pgsql.*

define CSWphp5pgsql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pgsql extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "pgsql"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pgsql.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pgsql.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pgsql.so|extension=pgsql.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pgsql.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "pgsql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pgsql_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pgsql extension"

perl -i -plne 's|extension=pgsql.so|;extension=pgsql.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "pgsql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

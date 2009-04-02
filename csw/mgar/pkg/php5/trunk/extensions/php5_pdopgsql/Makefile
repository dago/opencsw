PHP5EXT_NAME = pdopgsql

PACKAGES += CSWphp5pdopgsql

CATALOGNAME_CSWphp5pdopgsql = php5_pdopgsql
SPKG_DESC_CSWphp5pdopgsql = pdopgsql Extention for PHP5
REQUIRED_PKGS_CSWphp5pdopgsql = CSWphp5 CSWlibpq CSWphp5pdo

PATCHFILES += pdopgsql.diff

CONFIGURE_ARGS += --with-pdo-pgsql=shared,$(prefix)/postgresql

PKGFILES_CSWphp5pdopgsql = .*/lib/php/extensions/.*/pdo_pgsql.*

define CSWphp5pdopgsql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdopgsql extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "pdopgsql"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pdopgsql.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pdopgsql.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pdopgsql.so|extension=pdopgsql.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pdopgsql.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "pdopgsql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pdopgsql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdopgsql extension"

perl -i -plne 's|extension=pdopgsql.so|;extension=pdopgsql.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "pdopgsql"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

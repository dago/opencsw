PHP5EXT_NAME = pdosqlite

PACKAGES += CSWphp5pdosqlite

CATALOGNAME_CSWphp5pdosqlite = php5_pdosqlite
SPKG_DESC_CSWphp5pdosqlite = pdosqlite Extention for PHP5
REQUIRED_PKGS_CSWphp5pdosqlite = CSWphp5 CSWphp5pdo

CONFIGURE_ARGS += --with-pdo-sqlite=shared

PKGFILES_CSWphp5pdosqlite = .*/lib/php/extensions/.*/pdo_sqlite.*

define CSWphp5pdosqlite_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdosqlite extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "pdosqlite"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pdosqlite.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pdosqlite.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pdosqlite.so|extension=pdosqlite.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pdosqlite.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "pdosqlite"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pdosqlite_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdosqlite extension"

perl -i -plne 's|extension=pdosqlite.so|;extension=pdosqlite.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "pdosqlite"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

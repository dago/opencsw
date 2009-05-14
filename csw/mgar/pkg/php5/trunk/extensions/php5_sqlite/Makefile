PHP5EXT_NAME = sqlite

PACKAGES += CSWphp5sqlite

CATALOGNAME_CSWphp5sqlite = php5_sqlite
SPKG_DESC_CSWphp5sqlite = sqlite Extention for PHP5
REQUIRED_PKGS_CSWphp5sqlite = CSWphp5 CSWsqlite

CONFIGURE_ARGS += --with-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --enable-sqlite-utf8

PKGFILES_CSWphp5sqlite = .*/lib/php/extensions/.*/sqlite.*

define CSWphp5sqlite_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sqlite extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "sqlite"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=sqlite.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=sqlite.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=sqlite.so|extension=sqlite.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=sqlite.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "sqlite"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5sqlite_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sqlite extension"

perl -i -plne 's|extension=sqlite.so|;extension=sqlite.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "sqlite"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = pdoodbc

PACKAGES += CSWphp5pdoodbc

CATALOGNAME_CSWphp5pdoodbc = php5_pdoodbc
SPKG_DESC_CSWphp5pdoodbc = pdoodbc Extention for PHP5
REQUIRED_PKGS_CSWphp5pdoodbc = CSWphp5 CSWunixodbc 

CONFIGURE_ARGS += --with-pdo-odbc=shared,unixODBC,$(prefix)

PKGFILES_CSWphp5pdoodbc = .*/lib/php/extensions/.*/pdo_odbc.*

define CSWphp5pdoodbc_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdo_odbc extension"

perl -i -plne 's|;extension=pdo_odbc.so|extension=pdo_odbc.so|' ${PHP_INI}

exit 0
endef

define CSWphp5pdoodbc_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdo_odbc extension"

perl -i -plne 's|extension=pdo_odbc.so|;extension=pdo_odbc.so|' ${PHP_INI}

exit 0
endef


PHP5EXT_NAME = pdomysql

PACKAGES += CSWphp5pdomysql

CATALOGNAME_CSWphp5pdomysql = php5_pdomysql
SPKG_DESC_CSWphp5pdomysql = pdomysql Extention for PHP5
REQUIRED_PKGS_CSWphp5pdomysql = CSWphp5 CSWmysql5rt CSWzlib 

CONFIGURE_ARGS += --with-pdo-mysql=shared,$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

PKGFILES_CSWphp5pdomysql = .*/lib/php/extensions/.*/pdo_mysql.*

define CSWphp5pdomysql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdo_mysql extension"

perl -i -plne 's|;extension=pdo_mysql.so|extension=pdo_mysql.so|' ${PHP_INI}

exit 0
endef

define CSWphp5pdomysql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdo_mysql extension"

perl -i -plne 's|extension=pdo_mysql.so|;extension=pdo_mysql.so|' ${PHP_INI}

exit 0
endef


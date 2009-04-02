PHP5EXT_NAME = pdopgsql

PACKAGES += CSWphp5pdopgsql

CATALOGNAME_CSWphp5pdopgsql = php5_pdopgsql
SPKG_DESC_CSWphp5pdopgsql = pdopgsql Extention for PHP5
REQUIRED_PKGS_CSWphp5pdopgsql = CSWphp5 CSWlibpq 

PATCHFILES += pdopgsql.diff

CONFIGURE_ARGS += --with-pdo-pgsql=shared,$(prefix)/postgresql

PKGFILES_CSWphp5pdopgsql = .*/lib/php/extensions/.*/pdo_pgsql.*

define CSWphp5pdopgsql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdo_pgsql extension"

perl -i -plne 's|;extension=pdo_pgsql.so|extension=pdo_pgsql.so|' ${PHP_INI}

exit 0
endef

define CSWphp5pdopgsql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdo_pgsql extension"

perl -i -plne 's|extension=pdo_pgsql.so|;extension=pdo_pgsql.so|' ${PHP_INI}

exit 0
endef


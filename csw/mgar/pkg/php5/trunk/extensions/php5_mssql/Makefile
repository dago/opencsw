PHP5EXT_NAME = mssql

PACKAGES += CSWphp5mssql

CATALOGNAME_CSWphp5mssql = php5_mssql
SPKG_DESC_CSWphp5mssql = mssql Extention for PHP5
REQUIRED_PKGS_CSWphp5mssql = CSWphp5 CSWfreetds

CONFIGURE_ARGS += --with-mssql=shared,$(prefix)

PKGFILES_CSWphp5mssql = .*/lib/php/extensions/.*/mssql.*

define CSWphp5mssql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mssql extension"

perl -i -plne 's|;extension=mssql.so|extension=mssql.so|' ${PHP_INI}

exit 0
endef

define CSWphp5mssql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mssql extension"

perl -i -plne 's|extension=mssql.so|;extension=mssql.so|' ${PHP_INI}

exit 0
endef


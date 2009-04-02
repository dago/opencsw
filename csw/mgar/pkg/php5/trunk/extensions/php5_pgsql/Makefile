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

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pgsql extension"

perl -i -plne 's|;extension=pgsql.so|extension=pgsql.so|' ${PHP_INI}

exit 0
endef

define CSWphp5pgsql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pgsql extension"

perl -i -plne 's|extension=pgsql.so|;extension=pgsql.so|' ${PHP_INI}

exit 0
endef


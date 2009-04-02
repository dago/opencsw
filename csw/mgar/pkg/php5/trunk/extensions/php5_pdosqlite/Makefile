PHP5EXT_NAME = pdosqlite

PACKAGES += CSWphp5pdosqlite

CATALOGNAME_CSWphp5pdosqlite = php5_pdosqlite
SPKG_DESC_CSWphp5pdosqlite = pdosqlite Extention for PHP5
REQUIRED_PKGS_CSWphp5pdosqlite = CSWphp5 

CONFIGURE_ARGS += --with-pdo-sqlite=shared

PKGFILES_CSWphp5pdosqlite = .*/lib/php/extensions/.*/pdo_sqlite.*

define CSWphp5pdosqlite_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdo_sqlite extension"

perl -i -plne 's|;extension=pdo_sqlite.so|extension=pdo_sqlite.so|' ${PHP_INI}

exit 0
endef

define CSWphp5pdosqlite_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdo_sqlite extension"

perl -i -plne 's|extension=pdo_sqlite.so|;extension=pdo_sqlite.so|' ${PHP_INI}

exit 0
endef


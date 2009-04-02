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

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sqlite extension"

perl -i -plne 's|;extension=sqlite.so|extension=sqlite.so|' ${PHP_INI}

exit 0
endef

define CSWphp5sqlite_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sqlite extension"

perl -i -plne 's|extension=sqlite.so|;extension=sqlite.so|' ${PHP_INI}

exit 0
endef


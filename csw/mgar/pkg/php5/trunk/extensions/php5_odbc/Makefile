PHP5EXT_NAME = odbc

PACKAGES += CSWphp5odbc

CATALOGNAME_CSWphp5odbc = php5_odbc
SPKG_DESC_CSWphp5odbc = odbc Extention for PHP5
REQUIRED_PKGS_CSWphp5odbc = CSWphp5 CSWunixodbc

PATCHFILES += odbc.diff

CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)

PKGFILES_CSWphp5odbc = .*/lib/php/extensions/.*/odbc.*

define CSWphp5odbc_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling odbc extension"

perl -i -plne 's|;extension=odbc.so|extension=odbc.so|' ${PHP_INI}

exit 0
endef

define CSWphp5odbc_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling odbc extension"

perl -i -plne 's|extension=odbc.so|;extension=odbc.so|' ${PHP_INI}

exit 0
endef


PHP5EXT_NAME = dbase

PACKAGES += CSWphp5dbase

CATALOGNAME_CSWphp5dbase = php5_dbase
SPKG_DESC_CSWphp5dbase = dbase Extention for PHP5
REQUIRED_PKGS_CSWphp5dbase = CSWphp5

CONFIGURE_ARGS += --enable-dbase=shared

PKGFILES_CSWphp5dbase = .*/lib/php/extensions/.*/dbase.*

define CSWphp5dbase_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling dbase extension"

perl -i -plne 's|;extension=dbase.so|extension=dbase.so|' ${PHP_INI}

exit 0
endef

define CSWphp5dbase_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling dbase extension"

perl -i -plne 's|extension=dbase.so|;extension=dbase.so|' ${PHP_INI}

exit 0
endef


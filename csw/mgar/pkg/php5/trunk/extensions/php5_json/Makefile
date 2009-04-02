PHP5EXT_NAME = json

PACKAGES += CSWphp5json

CATALOGNAME_CSWphp5json = php5_json
SPKG_DESC_CSWphp5json = json Extention for PHP5
REQUIRED_PKGS_CSWphp5json = CSWphp5

CONFIGURE_ARGS += --enable-json=shared

PKGFILES_CSWphp5json = .*/lib/php/extensions/.*/json.*

define CSWphp5json_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling json extension"

perl -i -plne 's|;extension=json.so|extension=json.so|' ${PHP_INI}

exit 0
endef

define CSWphp5json_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling json extension"

perl -i -plne 's|extension=json.so|;extension=json.so|' ${PHP_INI}

exit 0
endef


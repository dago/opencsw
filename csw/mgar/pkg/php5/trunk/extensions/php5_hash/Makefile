PHP5EXT_NAME = hash

PACKAGES += CSWphp5hash

CATALOGNAME_CSWphp5hash = php5_hash
SPKG_DESC_CSWphp5hash = hash Extention for PHP5
REQUIRED_PKGS_CSWphp5hash = CSWphp5

CONFIGURE_ARGS += --enable-hash=shared

PKGFILES_CSWphp5hash = .*/lib/php/extensions/.*/hash.*

define CSWphp5hash_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling hash extension"

perl -i -plne 's|;extension=hash.so|extension=hash.so|' ${PHP_INI}

exit 0
endef

define CSWphp5hash_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling hash extension"

perl -i -plne 's|extension=hash.so|;extension=hash.so|' ${PHP_INI}

exit 0
endef


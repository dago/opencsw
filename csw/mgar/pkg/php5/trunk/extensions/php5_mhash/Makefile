PHP5EXT_NAME = mhash

PACKAGES += CSWphp5mhash

CATALOGNAME_CSWphp5mhash = php5_mhash
SPKG_DESC_CSWphp5mhash = mhash Extention for PHP5
REQUIRED_PKGS_CSWphp5mhash = CSWphp5 CSWlibmhash

CONFIGURE_ARGS += --with-mhash=shared,$(prefix)

PKGFILES_CSWphp5mhash = .*/lib/php/extensions/.*/mhash.*

define CSWphp5mhash_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mhash extension"

perl -i -plne 's|;extension=mhash.so|extension=mhash.so|' ${PHP_INI}

exit 0
endef

define CSWphp5mhash_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mhash extension"

perl -i -plne 's|extension=mhash.so|;extension=mhash.so|' ${PHP_INI}

exit 0
endef


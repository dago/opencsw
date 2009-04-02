PHP5EXT_NAME = gmp

PACKAGES += CSWphp5gmp

CATALOGNAME_CSWphp5gmp = php5_gmp
SPKG_DESC_CSWphp5gmp = gmp Extention for PHP5
REQUIRED_PKGS_CSWphp5gmp = CSWphp5 CSWlibgmp

CONFIGURE_ARGS += --with-gmp=shared,$(prefix)

PKGFILES_CSWphp5gmp = .*/lib/php/extensions/.*/gmp.*

define CSWphp5gmp_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling gmp extension"

perl -i -plne 's|;extension=gmp.so|extension=gmp.so|' ${PHP_INI}

exit 0
endef

define CSWphp5gmp_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling gmp extension"

perl -i -plne 's|extension=gmp.so|;extension=gmp.so|' ${PHP_INI}

exit 0
endef


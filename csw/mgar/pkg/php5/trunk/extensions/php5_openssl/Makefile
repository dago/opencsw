PHP5EXT_NAME = openssl

PACKAGES += CSWphp5openssl

CATALOGNAME_CSWphp5openssl = php5_openssl
SPKG_DESC_CSWphp5openssl = openssl Extention for PHP5
REQUIRED_PKGS_CSWphp5openssl = CSWphp5 CSWosslrt CSWkrb5lib

CONFIGURE_ARGS += --with-openssl=shared,$(prefix)

PKGFILES_CSWphp5openssl = .*/lib/php/extensions/.*/openssl.*

define CSWphp5openssl_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling openssl extension"

perl -i -plne 's|;extension=openssl.so|extension=openssl.so|' ${PHP_INI}

exit 0
endef

define CSWphp5openssl_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling openssl extension"

perl -i -plne 's|extension=openssl.so|;extension=openssl.so|' ${PHP_INI}

exit 0
endef


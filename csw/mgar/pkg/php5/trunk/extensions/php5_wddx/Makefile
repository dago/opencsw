PHP5EXT_NAME = wddx

PACKAGES += CSWphp5wddx

CATALOGNAME_CSWphp5wddx = php5_wddx
SPKG_DESC_CSWphp5wddx = wddx Extention for PHP5
REQUIRED_PKGS_CSWphp5wddx = CSWphp5

CONFIGURE_ARGS += --enable-wddx=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)

PKGFILES_CSWphp5wddx = .*/lib/php/extensions/.*/wddx.*

define CSWphp5wddx_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling wddx extension"

perl -i -plne 's|;extension=wddx.so|extension=wddx.so|' ${PHP_INI}

exit 0
endef

define CSWphp5wddx_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling wddx extension"

perl -i -plne 's|extension=wddx.so|;extension=wddx.so|' ${PHP_INI}

exit 0
endef


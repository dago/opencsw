PHP5EXT_NAME = zip

PACKAGES += CSWphp5zip

CATALOGNAME_CSWphp5zip = php5_zip
SPKG_DESC_CSWphp5zip = zip Extention for PHP5
REQUIRED_PKGS_CSWphp5zip = CSWphp5 CSWzlib

CONFIGURE_ARGS += --enable-zip=shared
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

PKGFILES_CSWphp5zip = .*/lib/php/extensions/.*/zip.*

define CSWphp5zip_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling zip extension"

perl -i -plne 's|;extension=zip.so|extension=zip.so|' ${PHP_INI}

exit 0
endef

define CSWphp5zip_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling zip extension"

perl -i -plne 's|extension=zip.so|;extension=zip.so|' ${PHP_INI}

exit 0
endef


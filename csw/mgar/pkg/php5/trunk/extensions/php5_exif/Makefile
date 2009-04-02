PHP5EXT_NAME = exif

PACKAGES += CSWphp5exif

CATALOGNAME_CSWphp5exif = php5_exif
SPKG_DESC_CSWphp5exif = exif Extention for PHP5
REQUIRED_PKGS_CSWphp5exif = CSWphp5

CONFIGURE_ARGS += --enable-exif=shared

CPPFLAGS="-I../ext/mbstring"
export CPPFLAGS

PKGFILES_CSWphp5exif = .*/lib/php/extensions/.*/exif.*

define CSWphp5exif_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling exif extension"

perl -i -plne 's|;extension=exif.so|extension=exif.so|' ${PHP_INI}

exit 0
endef

define CSWphp5exif_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling exif extension"

perl -i -plne 's|extension=exif.so|;extension=exif.so|' ${PHP_INI}

exit 0
endef


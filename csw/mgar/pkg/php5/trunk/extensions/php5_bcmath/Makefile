PHP5EXT_NAME = bcmath

PACKAGES += CSWphp5bcmath

CATALOGNAME_CSWphp5bcmath = php5_bcmath
SPKG_DESC_CSWphp5bcmath = bcmath Extention for PHP5
REQUIRED_PKGS_CSWphp5bcmath = CSWphp5

CONFIGURE_ARGS += --enable-bcmath=shared

PKGFILES_CSWphp5bcmath = .*/lib/php/extensions/.*/bcmath.*

define CSWphp5bcmath_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling bcmath extension"

perl -i -plne 's|;extension=bcmath.so|extension=bcmath.so|' ${PHP_INI}

exit 0
endef

define CSWphp5bcmath_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling bcmath extension"

perl -i -plne 's|extension=bcmath.so|;extension=bcmath.so|' ${PHP_INI}

exit 0
endef


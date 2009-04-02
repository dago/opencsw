PHP5EXT_NAME = posix

PACKAGES += CSWphp5posix

CATALOGNAME_CSWphp5posix = php5_posix
SPKG_DESC_CSWphp5posix = posix Extention for PHP5
REQUIRED_PKGS_CSWphp5posix = CSWphp5

CONFIGURE_ARGS += --enable-posix=shared

PKGFILES_CSWphp5posix = .*/lib/php/extensions/.*/posix.*

define CSWphp5posix_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling posix extension"

perl -i -plne 's|;extension=posix.so|extension=posix.so|' ${PHP_INI}

exit 0
endef

define CSWphp5posix_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling posix extension"

perl -i -plne 's|extension=posix.so|;extension=posix.so|' ${PHP_INI}

exit 0
endef


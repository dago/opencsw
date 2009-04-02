PHP5EXT_NAME = sockets

PACKAGES += CSWphp5sockets

CATALOGNAME_CSWphp5sockets = php5_sockets
SPKG_DESC_CSWphp5sockets = sockets Extention for PHP5
REQUIRED_PKGS_CSWphp5sockets = CSWphp5

CONFIGURE_ARGS += --enable-sockets=shared

PKGFILES_CSWphp5sockets = .*/lib/php/extensions/.*/sockets.*

define CSWphp5sockets_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sockets extension"

perl -i -plne 's|;extension=sockets.so|extension=sockets.so|' ${PHP_INI}

exit 0
endef

define CSWphp5sockets_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sockets extension"

perl -i -plne 's|extension=sockets.so|;extension=sockets.so|' ${PHP_INI}

exit 0
endef


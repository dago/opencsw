PHP5EXT_NAME = mcrypt

PACKAGES += CSWphp5mcrypt

CATALOGNAME_CSWphp5mcrypt = php5_mcrypt
SPKG_DESC_CSWphp5mcrypt = mcrypt Extention for PHP5
REQUIRED_PKGS_CSWphp5mcrypt = CSWphp5 CSWlibmcrypt CSWlibtoolrt

CONFIGURE_ARGS += --with-mcrypt=shared,$(prefix)

PKGFILES_CSWphp5mcrypt = .*/lib/php/extensions/.*/mcrypt.*

define CSWphp5mcrypt_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mcrypt extension"

perl -i -plne 's|;extension=mcrypt.so|extension=mcrypt.so|' ${PHP_INI}

exit 0
endef

define CSWphp5mcrypt_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mcrypt extension"

perl -i -plne 's|extension=mcrypt.so|;extension=mcrypt.so|' ${PHP_INI}

exit 0
endef


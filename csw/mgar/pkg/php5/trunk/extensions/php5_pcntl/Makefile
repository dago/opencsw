PHP5EXT_NAME = pcntl

PACKAGES += CSWphp5pcntl

CATALOGNAME_CSWphp5pcntl = php5_pcntl
SPKG_DESC_CSWphp5pcntl = pcntl Extention for PHP5
REQUIRED_PKGS_CSWphp5pcntl = CSWphp5

CONFIGURE_ARGS += --enable-pcntl=shared

PKGFILES_CSWphp5pcntl = .*/lib/php/extensions/.*/pcntl.*

define CSWphp5pcntl_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pcntl extension"

perl -i -plne 's|;extension=pcntl.so|extension=pcntl.so|' ${PHP_INI}

exit 0
endef

define CSWphp5pcntl_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pcntl extension"

perl -i -plne 's|extension=pcntl.so|;extension=pcntl.so|' ${PHP_INI}

exit 0
endef


PHP5EXT_NAME = shmop

PACKAGES += CSWphp5shmop

CATALOGNAME_CSWphp5shmop = php5_shmop
SPKG_DESC_CSWphp5shmop = shmop Extention for PHP5
REQUIRED_PKGS_CSWphp5shmop = CSWphp5

CONFIGURE_ARGS += --enable-shmop=shared

PKGFILES_CSWphp5shmop = .*/lib/php/extensions/.*/shmop.*

define CSWphp5shmop_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling shmop extension"

perl -i -plne 's|;extension=shmop.so|extension=shmop.so|' ${PHP_INI}

exit 0
endef

define CSWphp5shmop_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling shmop extension"

perl -i -plne 's|extension=shmop.so|;extension=shmop.so|' ${PHP_INI}

exit 0
endef


PHP5EXT_NAME = sysvsem

PACKAGES += CSWphp5sysvsem

CATALOGNAME_CSWphp5sysvsem = php5_sysvsem
SPKG_DESC_CSWphp5sysvsem = sysvsem Extention for PHP5
REQUIRED_PKGS_CSWphp5sysvsem = CSWphp5

CONFIGURE_ARGS += --enable-sysvsem=shared

PKGFILES_CSWphp5sysvsem = .*/lib/php/extensions/.*/sysvsem.*

define CSWphp5sysvsem_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sysvsem extension"

perl -i -plne 's|;extension=sysvsem.so|extension=sysvsem.so|' ${PHP_INI}

exit 0
endef

define CSWphp5sysvsem_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sysvsem extension"

perl -i -plne 's|extension=sysvsem.so|;extension=sysvsem.so|' ${PHP_INI}

exit 0
endef


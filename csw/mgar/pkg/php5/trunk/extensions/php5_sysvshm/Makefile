PHP5EXT_NAME = sysvshm

PACKAGES += CSWphp5sysvshm

CATALOGNAME_CSWphp5sysvshm = php5_sysvshm
SPKG_DESC_CSWphp5sysvshm = sysvshm Extention for PHP5
REQUIRED_PKGS_CSWphp5sysvshm = CSWphp5

CONFIGURE_ARGS += --enable-sysvshm=shared

PKGFILES_CSWphp5sysvshm = .*/lib/php/extensions/.*/sysvshm.*

define CSWphp5sysvshm_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sysvshm extension"

perl -i -plne 's|;extension=sysvshm.so|extension=sysvshm.so|' ${PHP_INI}

exit 0
endef

define CSWphp5sysvshm_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sysvshm extension"

perl -i -plne 's|extension=sysvshm.so|;extension=sysvshm.so|' ${PHP_INI}

exit 0
endef


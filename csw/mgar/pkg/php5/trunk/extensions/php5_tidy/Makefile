PHP5EXT_NAME = tidy

PACKAGES += CSWphp5tidy

CATALOGNAME_CSWphp5tidy = php5_tidy
SPKG_DESC_CSWphp5tidy = tidy Extention for PHP5
REQUIRED_PKGS_CSWphp5tidy = CSWphp5 CSWhtmltidy

CONFIGURE_ARGS += --with-tidy=shared,$(prefix)

PKGFILES_CSWphp5tidy = .*/lib/php/extensions/.*/tidy.*

define CSWphp5tidy_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling tidy extension"

perl -i -plne 's|;extension=tidy.so|extension=tidy.so|' ${PHP_INI}

exit 0
endef

define CSWphp5tidy_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling tidy extension"

perl -i -plne 's|extension=tidy.so|;extension=tidy.so|' ${PHP_INI}

exit 0
endef


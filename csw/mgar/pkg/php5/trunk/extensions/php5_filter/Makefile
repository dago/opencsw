PHP5EXT_NAME = filter

PACKAGES += CSWphp5filter

CATALOGNAME_CSWphp5filter = php5_filter
SPKG_DESC_CSWphp5filter = filter Extention for PHP5
REQUIRED_PKGS_CSWphp5filter = CSWphp5 CSWpcrert

CONFIGURE_ARGS += --enable-filter=shared
CONFIGURE_ARGS += --with-pcre-dir=$(prefix)

PKGFILES_CSWphp5filter = .*/lib/php/extensions/.*/filter.*

define CSWphp5filter_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling filter extension"

perl -i -plne 's|;extension=filter.so|extension=filter.so|' ${PHP_INI}

exit 0
endef

define CSWphp5filter_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling filter extension"

perl -i -plne 's|extension=filter.so|;extension=filter.so|' ${PHP_INI}

exit 0
endef


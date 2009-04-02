PHP5EXT_NAME = calendar

PACKAGES += CSWphp5calendar

CATALOGNAME_CSWphp5calendar = php5_calendar
SPKG_DESC_CSWphp5calendar = calendar Extention for PHP5
REQUIRED_PKGS_CSWphp5calendar = CSWphp5

CONFIGURE_ARGS += --enable-calendar=shared

PKGFILES_CSWphp5calendar = .*/lib/php/extensions/.*/calendar.*

define CSWphp5calendar_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling calendar extension"

perl -i -plne 's|;extension=calendar.so|extension=calendar.so|' ${PHP_INI}

exit 0
endef

define CSWphp5calendar_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling calendar extension"

perl -i -plne 's|extension=calendar.so|;extension=calendar.so|' ${PHP_INI}

exit 0
endef


PHP5EXT_NAME = session

PACKAGES += CSWphp5session

CATALOGNAME_CSWphp5session = php5_session
SPKG_DESC_CSWphp5session = session Extention for PHP5
REQUIRED_PKGS_CSWphp5session = CSWphp5 CSWlibmm

CONFIGURE_ARGS += --enable-session=shared

PKGFILES_CSWphp5session = .*/lib/php/extensions/.*/session.*

define CSWphp5session_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling session extension"

perl -i -plne 's|;extension=session.so|extension=session.so|' ${PHP_INI}

exit 0
endef

define CSWphp5session_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling session extension"

perl -i -plne 's|extension=session.so|;extension=session.so|' ${PHP_INI}

exit 0
endef


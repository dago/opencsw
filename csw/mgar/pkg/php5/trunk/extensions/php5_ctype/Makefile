PHP5EXT_NAME = ctype

PACKAGES += CSWphp5ctype

CATALOGNAME_CSWphp5ctype = php5_ctype
SPKG_DESC_CSWphp5ctype = ctype Extention for PHP5
REQUIRED_PKGS_CSWphp5ctype = CSWphp5

CONFIGURE_ARGS += --enable-ctype=shared

PKGFILES_CSWphp5ctype = .*/lib/php/extensions/.*/ctype.*

define CSWphp5ctype_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling ctype extension"

perl -i -plne 's|;extension=ctype.so|extension=ctype.so|' ${PHP_INI}

exit 0
endef

define CSWphp5ctype_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ctype extension"

perl -i -plne 's|extension=ctype.so|;extension=ctype.so|' ${PHP_INI}

exit 0
endef


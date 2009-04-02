PHP5EXT_NAME = mbstring

PACKAGES += CSWphp5mbstring

CATALOGNAME_CSWphp5mbstring = php5_mbstring
SPKG_DESC_CSWphp5mbstring = mbstring Extention for PHP5
REQUIRED_PKGS_CSWphp5mbstring = CSWphp5


CONFIGURE_ARGS += --enable-mbstring=shared
CONFIGURE_ARGS += --enable-mbregex=shared

PKGFILES_CSWphp5mbstring = .*/lib/php/extensions/.*/mbstring.*

define CSWphp5mbstring_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mbstring extension"

perl -i -plne 's|;extension=mbstring.so|extension=mbstring.so|' ${PHP_INI}

exit 0
endef

define CSWphp5mbstring_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mbstring extension"

perl -i -plne 's|extension=mbstring.so|;extension=mbstring.so|' ${PHP_INI}

exit 0
endef


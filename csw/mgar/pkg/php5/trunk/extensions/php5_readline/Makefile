PHP5EXT_NAME = readline

PACKAGES += CSWphp5readline

CATALOGNAME_CSWphp5readline = php5_readline
SPKG_DESC_CSWphp5readline = readline Extention for PHP5
REQUIRED_PKGS_CSWphp5readline = CSWphp5

CONFIGURE_ARGS += --with-libedit=no
CONFIGURE_ARGS += --with-readline=shared,/opt/csw

PKGFILES_CSWphp5readline = .*/lib/php/extensions/.*/readline.*

define CSWphp5readline_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling readline extension"

perl -i -plne 's|;extension=readline.so|extension=readline.so|' ${PHP_INI}

exit 0
endef

define CSWphp5readline_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling readline extension"

perl -i -plne 's|extension=readline.so|;extension=readline.so|' ${PHP_INI}

exit 0
endef


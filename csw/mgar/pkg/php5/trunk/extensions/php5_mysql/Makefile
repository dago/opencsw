PHP5EXT_NAME = mysql

PACKAGES += CSWphp5mysql

CATALOGNAME_CSWphp5mysql = php5_mysql
SPKG_DESC_CSWphp5mysql = mysql Extention for PHP5
REQUIRED_PKGS_CSWphp5mysql = CSWphp5 CSWmysql5rt

CONFIGURE_ARGS += --with-mysql=shared,$(prefix)

PKGFILES_CSWphp5mysql = .*/lib/php/extensions/.*/mysql\.so
PKGFILES_CSWphp5mysql += .*/lib/php/extensions/.*/mysql\.a

define CSWphp5mysql_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mysql extension"

perl -i -plne 's|;extension=mysql.so|extension=mysql.so|' ${PHP_INI}

exit 0
endef

define CSWphp5mysql_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mysql extension"

perl -i -plne 's|extension=mysql.so|;extension=mysql.so|' ${PHP_INI}

exit 0
endef


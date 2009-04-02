PHP5EXT_NAME = mysqli

PACKAGES += CSWphp5mysqli

CATALOGNAME_CSWphp5mysqli = php5_mysqli
SPKG_DESC_CSWphp5mysqli = mysqli Extention for PHP5
REQUIRED_PKGS_CSWphp5mysqli = CSWphp5 CSWmysql5rt CSWzlib

CONFIGURE_ARGS += --with-mysqli=shared,$(bindir)/mysql_config

PKGFILES_CSWphp5mysqli = .*/lib/php/extensions/.*/mysqli.*

define CSWphp5mysqli_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mysqli extension"

perl -i -plne 's|;extension=mysqli.so|extension=mysqli.so|' ${PHP_INI}

exit 0
endef

define CSWphp5mysqli_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mysqli extension"

perl -i -plne 's|extension=mysqli.so|;extension=mysqli.so|' ${PHP_INI}

exit 0
endef


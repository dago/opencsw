PHP5EXT_NAME = ftp

PACKAGES += CSWphp5ftp

CATALOGNAME_CSWphp5ftp = php5_ftp
SPKG_DESC_CSWphp5ftp = ftp Extention for PHP5
REQUIRED_PKGS_CSWphp5ftp = CSWphp5 CSWosslrt

CONFIGURE_ARGS += --enable-ftp=shared

PKGFILES_CSWphp5ftp = .*/lib/php/extensions/.*/ftp.*

define CSWphp5ftp_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling ftp extension"

perl -i -plne 's|;extension=ftp.so|extension=ftp.so|' ${PHP_INI}

exit 0
endef

define CSWphp5ftp_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ftp extension"

perl -i -plne 's|extension=ftp.so|;extension=ftp.so|' ${PHP_INI}

exit 0
endef


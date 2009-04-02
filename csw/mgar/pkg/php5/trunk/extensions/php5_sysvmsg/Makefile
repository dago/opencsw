PHP5EXT_NAME = sysvmsg

PACKAGES += CSWphp5sysvmsg

CATALOGNAME_CSWphp5sysvmsg = php5_sysvmsg
SPKG_DESC_CSWphp5sysvmsg = sysvmsg Extention for PHP5
REQUIRED_PKGS_CSWphp5sysvmsg = CSWphp5

CONFIGURE_ARGS += --enable-sysvsem=shared

PKGFILES_CSWphp5sysvmsg = .*/lib/php/extensions/.*/sysvmsg.*

define CSWphp5sysvmsg_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sysvmsg extension"

perl -i -plne 's|;extension=sysvmsg.so|extension=sysvmsg.so|' ${PHP_INI}

exit 0
endef

define CSWphp5sysvmsg_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sysvmsg extension"

perl -i -plne 's|extension=sysvmsg.so|;extension=sysvmsg.so|' ${PHP_INI}

exit 0
endef


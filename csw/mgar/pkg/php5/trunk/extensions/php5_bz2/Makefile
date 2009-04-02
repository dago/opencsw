PHP5EXT_NAME = bz2

PACKAGES += CSWphp5bz2

CATALOGNAME_CSWphp5bz2 = php5_bz2
SPKG_DESC_CSWphp5bz2 = bz2 Extention for PHP5
REQUIRED_PKGS_CSWphp5bz2 = CSWphp5 CSWbzip2

CONFIGURE_ARGS += --with-bz2=shared,$(prefix)

PKGFILES_CSWphp5bz2 = .*/lib/php/extensions/.*/bz2.*

define CSWphp5bz2_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling bz2 extension"

perl -i -plne 's|;extension=bz2.so|extension=bz2.so|' ${PHP_INI}

exit 0
endef

define CSWphp5bz2_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling bz2 extension"

perl -i -plne 's|extension=bz2.so|;extension=bz2.so|' ${PHP_INI}

exit 0
endef


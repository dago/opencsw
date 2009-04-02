PHP5EXT_NAME = soap

PACKAGES += CSWphp5soap

CATALOGNAME_CSWphp5soap = php5_soap
SPKG_DESC_CSWphp5soap = soap Extention for PHP5
REQUIRED_PKGS_CSWphp5soap = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CONFIGURE_ARGS += --enable-soap=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)

PKGFILES_CSWphp5soap = .*/lib/php/extensions/.*/soap.*

define CSWphp5soap_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling soap extension"

perl -i -plne 's|;extension=soap.so|extension=soap.so|' ${PHP_INI}

exit 0
endef

define CSWphp5soap_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling soap extension"

perl -i -plne 's|extension=soap.so|;extension=soap.so|' ${PHP_INI}

exit 0
endef


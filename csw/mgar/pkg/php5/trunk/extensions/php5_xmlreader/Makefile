PHP5EXT_NAME = xmlreader

PACKAGES += CSWphp5xmlreader

CATALOGNAME_CSWphp5xmlreader = php5_xmlreader
SPKG_DESC_CSWphp5xmlreader = xmlreader Extention for PHP5
REQUIRED_PKGS_CSWphp5xmlreader = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CONFIGURE_ARGS += --enable-xmlreader=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)

PKGFILES_CSWphp5xmlreader = .*/lib/php/extensions/.*/xmlreader.*

define CSWphp5xmlreader_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling xmlreader extension"

perl -i -plne 's|;extension=xmlreader.so|extension=xmlreader.so|' ${PHP_INI}

exit 0
endef

define CSWphp5xmlreader_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling xmlreader extension"

perl -i -plne 's|extension=xmlreader.so|;extension=xmlreader.so|' ${PHP_INI}

exit 0
endef


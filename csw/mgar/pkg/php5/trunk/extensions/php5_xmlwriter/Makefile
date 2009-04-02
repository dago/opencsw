PHP5EXT_NAME = xmlwriter

PACKAGES += CSWphp5xmlwriter

CATALOGNAME_CSWphp5xmlwriter = php5_xmlwriter
SPKG_DESC_CSWphp5xmlwriter = xmlwriter Extention for PHP5
REQUIRED_PKGS_CSWphp5xmlwriter = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CONFIGURE_ARGS += --enable-xmlwriter=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)

PKGFILES_CSWphp5xmlwriter = .*/lib/php/extensions/.*/xmlwriter.*

define CSWphp5xmlwriter_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling xmlwriter extension"

perl -i -plne 's|;extension=xmlwriter.so|extension=xmlwriter.so|' ${PHP_INI}

exit 0
endef

define CSWphp5xmlwriter_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling xmlwriter extension"

perl -i -plne 's|extension=xmlwriter.so|;extension=xmlwriter.so|' ${PHP_INI}

exit 0
endef


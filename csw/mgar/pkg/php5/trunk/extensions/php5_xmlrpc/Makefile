PHP5EXT_NAME = xmlrpc

PACKAGES += CSWphp5xmlrpc

CATALOGNAME_CSWphp5xmlrpc = php5_xmlrpc
SPKG_DESC_CSWphp5xmlrpc = xmlrpc Extention for PHP5
REQUIRED_PKGS_CSWphp5xmlrpc = CSWphp5 CSWiconv CSWlibxml2 CSWzlib CSWexpat

CONFIGURE_ARGS += --with-xmlrpc=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)

PKGFILES_CSWphp5xmlrpc = .*/lib/php/extensions/.*/xmlrpc.*

define CSWphp5xmlrpc_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling xmlrpc extension"

perl -i -plne 's|;extension=xmlrpc.so|extension=xmlrpc.so|' ${PHP_INI}

exit 0
endef

define CSWphp5xmlrpc_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling xmlrpc extension"

perl -i -plne 's|extension=xmlrpc.so|;extension=xmlrpc.so|' ${PHP_INI}

exit 0
endef


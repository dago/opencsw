PHP5EXT_NAME = dom

PACKAGES += CSWphp5dom

CATALOGNAME_CSWphp5dom = php5_dom
SPKG_DESC_CSWphp5dom = dom Extention for PHP5
REQUIRED_PKGS_CSWphp5dom = CSWphp5 CSWiconv CSWlibxml2 CSWzlib

CONFIGURE_ARGS += --enable-dom=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)

PKGFILES_CSWphp5dom = .*/lib/php/extensions/.*/dom.*

define CSWphp5dom_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling dom extension"

perl -i -plne 's|;extension=dom.so|extension=dom.so|' ${PHP_INI}

exit 0
endef

define CSWphp5dom_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling dom extension"

perl -i -plne 's|extension=dom.so|;extension=dom.so|' ${PHP_INI}

exit 0
endef


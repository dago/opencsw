PHP5EXT_NAME = simplexml

## build this static, php can not run without it.
## it is more efficient to have this built into the php binary

CONFIGURE_ARGS += --enable-simplexml
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)

define CSWphp5simplexml_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling simplexml extension"

perl -i -plne 's|;extension=simplexml.so|extension=simplexml.so|' ${PHP_INI}

exit 0
endef

define CSWphp5simplexml_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling simplexml extension"

perl -i -plne 's|extension=simplexml.so|;extension=simplexml.so|' ${PHP_INI}

exit 0
endef


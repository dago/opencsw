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

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "simplexml"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=simplexml.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=simplexml.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=simplexml.so|extension=simplexml.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=simplexml.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "simplexml"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5simplexml_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling simplexml extension"

perl -i -plne 's|extension=simplexml.so|;extension=simplexml.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "simplexml"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

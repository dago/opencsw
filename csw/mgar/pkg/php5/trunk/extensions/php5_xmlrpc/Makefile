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

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "xmlrpc"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=xmlrpc.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=xmlrpc.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=xmlrpc.so|extension=xmlrpc.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=xmlrpc.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "xmlrpc"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5xmlrpc_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling xmlrpc extension"

perl -i -plne 's|extension=xmlrpc.so|;extension=xmlrpc.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "xmlrpc"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

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

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling xmlreader extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "xmlreader"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=xmlreader.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=xmlreader.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=xmlreader.so|extension=xmlreader.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=xmlreader.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "xmlreader"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5xmlreader_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling xmlreader extension"

perl -i -plne 's|extension=xmlreader.so|;extension=xmlreader.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "xmlreader"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

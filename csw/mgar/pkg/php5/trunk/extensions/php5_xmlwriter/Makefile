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

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling xmlwriter extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "xmlwriter"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=xmlwriter.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=xmlwriter.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=xmlwriter.so|extension=xmlwriter.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=xmlwriter.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "xmlwriter"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5xmlwriter_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling xmlwriter extension"

perl -i -plne 's|extension=xmlwriter.so|;extension=xmlwriter.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "xmlwriter"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

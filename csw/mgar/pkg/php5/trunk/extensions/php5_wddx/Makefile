PHP5EXT_NAME = wddx

PACKAGES += CSWphp5wddx

CATALOGNAME_CSWphp5wddx = php5_wddx
SPKG_DESC_CSWphp5wddx = wddx Extention for PHP5
REQUIRED_PKGS_CSWphp5wddx = CSWphp5

CONFIGURE_ARGS += --enable-wddx=shared
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --with-libexpat-dir=$(prefix)

PKGFILES_CSWphp5wddx = .*/lib/php/extensions/.*/wddx.*

define CSWphp5wddx_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling wddx extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "wddx"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=wddx.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=wddx.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=wddx.so|extension=wddx.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=wddx.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "wddx"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5wddx_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling wddx extension"

perl -i -plne 's|extension=wddx.so|;extension=wddx.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "wddx"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

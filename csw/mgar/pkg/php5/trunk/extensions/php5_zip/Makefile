PHP5EXT_NAME = zip

PACKAGES += CSWphp5zip

CATALOGNAME_CSWphp5zip = php5_zip
SPKG_DESC_CSWphp5zip = zip Extention for PHP5
REQUIRED_PKGS_CSWphp5zip = CSWphp5 CSWzlib

CONFIGURE_ARGS += --enable-zip=shared
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

PKGFILES_CSWphp5zip = .*/lib/php/extensions/.*/zip.*

define CSWphp5zip_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling zip extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "zip"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=zip.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=zip.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=zip.so|extension=zip.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=zip.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "zip"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5zip_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling zip extension"

perl -i -plne 's|extension=zip.so|;extension=zip.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "zip"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

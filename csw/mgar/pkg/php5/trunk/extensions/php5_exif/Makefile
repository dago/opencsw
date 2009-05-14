PHP5EXT_NAME = exif

PACKAGES += CSWphp5exif

CATALOGNAME_CSWphp5exif = php5_exif
SPKG_DESC_CSWphp5exif = exif Extention for PHP5
REQUIRED_PKGS_CSWphp5exif = CSWphp5

CONFIGURE_ARGS += --enable-exif=shared

CPPFLAGS="-I../ext/mbstring"
export CPPFLAGS

PKGFILES_CSWphp5exif = .*/lib/php/extensions/.*/exif.*

define CSWphp5exif_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling exif extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "exif"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=exif.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=exif.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=exif.so|extension=exif.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=exif.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "exif"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5exif_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling exif extension"

perl -i -plne 's|extension=exif.so|;extension=exif.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "exif"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

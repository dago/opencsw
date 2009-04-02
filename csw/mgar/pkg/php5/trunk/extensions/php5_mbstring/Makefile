PHP5EXT_NAME = mbstring

PACKAGES += CSWphp5mbstring

CATALOGNAME_CSWphp5mbstring = php5_mbstring
SPKG_DESC_CSWphp5mbstring = mbstring Extention for PHP5
REQUIRED_PKGS_CSWphp5mbstring = CSWphp5


CONFIGURE_ARGS += --enable-mbstring=shared
CONFIGURE_ARGS += --enable-mbregex=shared

PKGFILES_CSWphp5mbstring = .*/lib/php/extensions/.*/mbstring.*

define CSWphp5mbstring_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mbstring extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"mbstring\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=mbstring.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=mbstring.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=mbstring.so|extension=mbstring.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=mbstring.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"mbstring\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5mbstring_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mbstring extension"

perl -i -plne 's|extension=mbstring.so|;extension=mbstring.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"mbstring\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = json

PACKAGES += CSWphp5json

CATALOGNAME_CSWphp5json = php5_json
SPKG_DESC_CSWphp5json = json Extention for PHP5
REQUIRED_PKGS_CSWphp5json = CSWphp5

CONFIGURE_ARGS += --enable-json=shared

PKGFILES_CSWphp5json = .*/lib/php/extensions/.*/json.*

define CSWphp5json_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling json extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"json\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=json.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=json.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=json.so|extension=json.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=json.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"json\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5json_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling json extension"

perl -i -plne 's|extension=json.so|;extension=json.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"json\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = mhash

PACKAGES += CSWphp5mhash

CATALOGNAME_CSWphp5mhash = php5_mhash
SPKG_DESC_CSWphp5mhash = mhash Extention for PHP5
REQUIRED_PKGS_CSWphp5mhash = CSWphp5 CSWlibmhash

CONFIGURE_ARGS += --with-mhash=shared,$(prefix)

PKGFILES_CSWphp5mhash = .*/lib/php/extensions/.*/mhash.*

define CSWphp5mhash_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mhash extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"mhash\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=mhash.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=mhash.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=mhash.so|extension=mhash.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=mhash.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"mhash\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5mhash_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mhash extension"

perl -i -plne 's|extension=mhash.so|;extension=mhash.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"mhash\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

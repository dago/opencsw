PHP5EXT_NAME = calendar

PACKAGES += CSWphp5calendar

CATALOGNAME_CSWphp5calendar = php5_calendar
SPKG_DESC_CSWphp5calendar = calendar Extention for PHP5
REQUIRED_PKGS_CSWphp5calendar = CSWphp5

CONFIGURE_ARGS += --enable-calendar=shared

PKGFILES_CSWphp5calendar = .*/lib/php/extensions/.*/calendar.*

define CSWphp5calendar_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling calendar extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "calendar"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=calendar.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=calendar.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=calendar.so|extension=calendar.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=calendar.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "calendar"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5calendar_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling calendar extension"

perl -i -plne 's|extension=calendar.so|;extension=calendar.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "calendar"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

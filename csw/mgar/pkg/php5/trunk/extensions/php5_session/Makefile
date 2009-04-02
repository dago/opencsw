PHP5EXT_NAME = session

PACKAGES += CSWphp5session

CATALOGNAME_CSWphp5session = php5_session
SPKG_DESC_CSWphp5session = session Extention for PHP5
REQUIRED_PKGS_CSWphp5session = CSWphp5 CSWlibmm

CONFIGURE_ARGS += --enable-session=shared

PKGFILES_CSWphp5session = .*/lib/php/extensions/.*/session.*

define CSWphp5session_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling session extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "session"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=session.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=session.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=session.so|extension=session.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=session.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "session"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5session_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling session extension"

perl -i -plne 's|extension=session.so|;extension=session.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "session"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

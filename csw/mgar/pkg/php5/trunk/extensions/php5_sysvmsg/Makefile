PHP5EXT_NAME = sysvmsg

PACKAGES += CSWphp5sysvmsg

CATALOGNAME_CSWphp5sysvmsg = php5_sysvmsg
SPKG_DESC_CSWphp5sysvmsg = sysvmsg Extention for PHP5
REQUIRED_PKGS_CSWphp5sysvmsg = CSWphp5

CONFIGURE_ARGS += --enable-sysvsem=shared

PKGFILES_CSWphp5sysvmsg = .*/lib/php/extensions/.*/sysvmsg.*

define CSWphp5sysvmsg_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sysvmsg extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"sysvmsg\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=sysvmsg.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=sysvmsg.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=sysvmsg.so|extension=sysvmsg.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=sysvmsg.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"sysvmsg\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5sysvmsg_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sysvmsg extension"

perl -i -plne 's|extension=sysvmsg.so|;extension=sysvmsg.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"sysvmsg\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

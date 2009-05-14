PHP5EXT_NAME = readline

PACKAGES += CSWphp5readline

CATALOGNAME_CSWphp5readline = php5_readline
SPKG_DESC_CSWphp5readline = readline Extention for PHP5
REQUIRED_PKGS_CSWphp5readline = CSWphp5 CSWreadline CSWncurses

CONFIGURE_ARGS += --with-libedit=no
CONFIGURE_ARGS += --with-readline=shared,/opt/csw

PKGFILES_CSWphp5readline = .*/lib/php/extensions/.*/readline.*

define CSWphp5readline_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling readline extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "readline"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=readline.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=readline.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=readline.so|extension=readline.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=readline.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "readline"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5readline_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling readline extension"

perl -i -plne 's|extension=readline.so|;extension=readline.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "readline"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = ncurses

PACKAGES += CSWphp5ncurses

CATALOGNAME_CSWphp5ncurses = php5_ncurses
SPKG_DESC_CSWphp5ncurses = ncurses Extention for PHP5
REQUIRED_PKGS_CSWphp5ncurses = CSWphp5 CSWncurses

CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)

PKGFILES_CSWphp5ncurses = .*/lib/php/extensions/.*/ncurses.*

define CSWphp5ncurses_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling ncurses extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"ncurses\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=ncurses.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=ncurses.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=ncurses.so|extension=ncurses.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=ncurses.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"ncurses\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5ncurses_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ncurses extension"

perl -i -plne 's|extension=ncurses.so|;extension=ncurses.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"ncurses\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

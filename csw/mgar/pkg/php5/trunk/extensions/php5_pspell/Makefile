PHP5EXT_NAME = pspell

PACKAGES += CSWphp5pspell

CATALOGNAME_CSWphp5pspell = php5_pspell
SPKG_DESC_CSWphp5pspell = pspell Extention for PHP5
REQUIRED_PKGS_CSWphp5pspell = CSWphp5 CSWaspell

CONFIGURE_ARGS += --with-pspell=shared,$(prefix)

PKGFILES_CSWphp5pspell = .*/lib/php/extensions/.*/pspell.*

define CSWphp5pspell_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pspell extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"pspell\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pspell.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pspell.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pspell.so|extension=pspell.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pspell.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"pspell\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pspell_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pspell extension"

perl -i -plne 's|extension=pspell.so|;extension=pspell.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"pspell\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

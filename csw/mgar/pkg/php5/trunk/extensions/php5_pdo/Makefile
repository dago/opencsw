PHP5EXT_NAME = pdo

PACKAGES += CSWphp5pdo

CATALOGNAME_CSWphp5pdo = php5_pdo
SPKG_DESC_CSWphp5pdo = pdo Extention for PHP5
REQUIRED_PKGS_CSWphp5pdo = CSWphp5 

PKGFILES_CSWphp5pdo  = .*/lib/php/extensions/.*/pdo\.so*
PKGFILES_CSWphp5pdo += .*/lib/php/extensions/.*/pdo\.a*

define CSWphp5pdo_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pdo extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "pdo"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pdo.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pdo.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pdo.so|extension=pdo.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pdo.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "pdo"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pdo_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pdo extension"

perl -i -plne 's|extension=pdo.so|;extension=pdo.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "pdo"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = sysvsem

PACKAGES += CSWphp5sysvsem

CATALOGNAME_CSWphp5sysvsem = php5_sysvsem
SPKG_DESC_CSWphp5sysvsem = sysvsem Extention for PHP5
REQUIRED_PKGS_CSWphp5sysvsem = CSWphp5

CONFIGURE_ARGS += --enable-sysvsem=shared

PKGFILES_CSWphp5sysvsem = .*/lib/php/extensions/.*/sysvsem.*

define CSWphp5sysvsem_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sysvsem extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "sysvsem"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=sysvsem.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=sysvsem.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=sysvsem.so|extension=sysvsem.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=sysvsem.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "sysvsem"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5sysvsem_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sysvsem extension"

perl -i -plne 's|extension=sysvsem.so|;extension=sysvsem.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "sysvsem"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

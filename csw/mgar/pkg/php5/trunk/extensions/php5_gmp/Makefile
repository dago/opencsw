PHP5EXT_NAME = gmp

PACKAGES += CSWphp5gmp

CATALOGNAME_CSWphp5gmp = php5_gmp
SPKG_DESC_CSWphp5gmp = gmp Extention for PHP5
REQUIRED_PKGS_CSWphp5gmp = CSWphp5 CSWlibgmp

CONFIGURE_ARGS += --with-gmp=shared,$(prefix)

PKGFILES_CSWphp5gmp = .*/lib/php/extensions/.*/gmp.*

define CSWphp5gmp_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling gmp extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "gmp"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=gmp.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=gmp.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=gmp.so|extension=gmp.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=gmp.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "gmp"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5gmp_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling gmp extension"

perl -i -plne 's|extension=gmp.so|;extension=gmp.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "gmp"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

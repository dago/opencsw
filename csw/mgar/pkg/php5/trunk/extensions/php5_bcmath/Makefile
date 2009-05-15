PHP5EXT_NAME = bcmath

PACKAGES += CSWphp5bcmath

CATALOGNAME_CSWphp5bcmath = php5_bcmath
SPKG_DESC_CSWphp5bcmath = bcmath Extention for PHP5
REQUIRED_PKGS_CSWphp5bcmath = CSWphp5

CONFIGURE_ARGS += --enable-bcmath=shared

PKGFILES_CSWphp5bcmath = .*/lib/php/extensions/.*/bcmath.*

define CSWphp5bcmath_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling bcmath extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "bcmath"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=bcmath.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=bcmath.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=bcmath.so|extension=bcmath.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=bcmath.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "bcmath"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5bcmath_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling bcmath extension"

perl -i -plne 's|extension=bcmath.so|;extension=bcmath.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "bcmath"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

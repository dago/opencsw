PHP5EXT_NAME = mysqli

PACKAGES += CSWphp5mysqli

CATALOGNAME_CSWphp5mysqli = php5_mysqli
SPKG_DESC_CSWphp5mysqli = mysqli Extention for PHP5
REQUIRED_PKGS_CSWphp5mysqli = CSWphp5 CSWmysql5rt CSWzlib

CONFIGURE_ARGS += --with-mysqli=shared,$(bindir)/mysql_config

PKGFILES_CSWphp5mysqli = .*/lib/php/extensions/.*/mysqli.*

define CSWphp5mysqli_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mysqli extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "mysqli"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=mysqli.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=mysqli.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=mysqli.so|extension=mysqli.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=mysqli.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "mysqli"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5mysqli_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mysqli extension"

perl -i -plne 's|extension=mysqli.so|;extension=mysqli.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "mysqli"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

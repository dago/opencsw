PHP5EXT_NAME = pcntl

PACKAGES += CSWphp5pcntl

CATALOGNAME_CSWphp5pcntl = php5_pcntl
SPKG_DESC_CSWphp5pcntl = pcntl Extention for PHP5
REQUIRED_PKGS_CSWphp5pcntl = CSWphp5

CONFIGURE_ARGS += --enable-pcntl=shared

PKGFILES_CSWphp5pcntl = .*/lib/php/extensions/.*/pcntl.*

define CSWphp5pcntl_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pcntl extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "pcntl"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=pcntl.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=pcntl.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=pcntl.so|extension=pcntl.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=pcntl.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "pcntl"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5pcntl_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pcntl extension"

perl -i -plne 's|extension=pcntl.so|;extension=pcntl.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "pcntl"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

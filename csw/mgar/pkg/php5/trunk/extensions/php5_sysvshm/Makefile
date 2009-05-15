PHP5EXT_NAME = sysvshm

PACKAGES += CSWphp5sysvshm

CATALOGNAME_CSWphp5sysvshm = php5_sysvshm
SPKG_DESC_CSWphp5sysvshm = sysvshm Extention for PHP5
REQUIRED_PKGS_CSWphp5sysvshm = CSWphp5

CONFIGURE_ARGS += --enable-sysvshm=shared

PKGFILES_CSWphp5sysvshm = .*/lib/php/extensions/.*/sysvshm.*

define CSWphp5sysvshm_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling sysvshm extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "sysvshm"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=sysvshm.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=sysvshm.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=sysvshm.so|extension=sysvshm.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=sysvshm.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "sysvshm"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5sysvshm_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling sysvshm extension"

perl -i -plne 's|extension=sysvshm.so|;extension=sysvshm.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "sysvshm"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

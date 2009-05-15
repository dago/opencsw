PHP5EXT_NAME = ctype

PACKAGES += CSWphp5ctype

CATALOGNAME_CSWphp5ctype = php5_ctype
SPKG_DESC_CSWphp5ctype = ctype Extention for PHP5
REQUIRED_PKGS_CSWphp5ctype = CSWphp5

CONFIGURE_ARGS += --enable-ctype=shared

PKGFILES_CSWphp5ctype = .*/lib/php/extensions/.*/ctype.*

define CSWphp5ctype_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling ctype extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "ctype"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=ctype.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=ctype.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=ctype.so|extension=ctype.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=ctype.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "ctype"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5ctype_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ctype extension"

perl -i -plne 's|extension=ctype.so|;extension=ctype.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "ctype"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

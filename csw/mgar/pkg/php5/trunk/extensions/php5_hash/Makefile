PHP5EXT_NAME = hash

PACKAGES += CSWphp5hash

CATALOGNAME_CSWphp5hash = php5_hash
SPKG_DESC_CSWphp5hash = hash Extention for PHP5
REQUIRED_PKGS_CSWphp5hash = CSWphp5

CONFIGURE_ARGS += --enable-hash=shared

PKGFILES_CSWphp5hash = .*/lib/php/extensions/.*/hash.*

define CSWphp5hash_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling hash extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "hash"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=hash.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=hash.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=hash.so|extension=hash.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=hash.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "hash"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5hash_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling hash extension"

perl -i -plne 's|extension=hash.so|;extension=hash.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "hash"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

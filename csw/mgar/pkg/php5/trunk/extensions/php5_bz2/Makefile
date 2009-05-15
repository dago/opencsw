PHP5EXT_NAME = bz2

PACKAGES += CSWphp5bz2

CATALOGNAME_CSWphp5bz2 = php5_bz2
SPKG_DESC_CSWphp5bz2 = bz2 Extention for PHP5
REQUIRED_PKGS_CSWphp5bz2 = CSWphp5 CSWbzip2

CONFIGURE_ARGS += --with-bz2=shared,$(prefix)

PKGFILES_CSWphp5bz2 = .*/lib/php/extensions/.*/bz2.*

define CSWphp5bz2_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling bz2 extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "bz2"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=bz2.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=bz2.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=bz2.so|extension=bz2.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=bz2.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "bz2"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5bz2_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling bz2 extension"

perl -i -plne 's|extension=bz2.so|;extension=bz2.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "bz2"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

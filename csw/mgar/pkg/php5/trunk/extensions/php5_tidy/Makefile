PHP5EXT_NAME = tidy

PACKAGES += CSWphp5tidy

CATALOGNAME_CSWphp5tidy = php5_tidy
SPKG_DESC_CSWphp5tidy = tidy Extention for PHP5
REQUIRED_PKGS_CSWphp5tidy = CSWphp5 CSWhtmltidy

CONFIGURE_ARGS += --with-tidy=shared,$(prefix)

PKGFILES_CSWphp5tidy = .*/lib/php/extensions/.*/tidy.*

define CSWphp5tidy_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling tidy extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "tidy"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=tidy.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=tidy.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=tidy.so|extension=tidy.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=tidy.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "tidy"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5tidy_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling tidy extension"

perl -i -plne 's|extension=tidy.so|;extension=tidy.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "tidy"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

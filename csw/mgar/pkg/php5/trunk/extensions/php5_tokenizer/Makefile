PHP5EXT_NAME = tokenizer

PACKAGES += CSWphp5tokenizer

CATALOGNAME_CSWphp5tokenizer = php5_tokenizer
SPKG_DESC_CSWphp5tokenizer = tokenizer Extention for PHP5
REQUIRED_PKGS_CSWphp5tokenizer = CSWphp5

CONFIGURE_ARGS += --enable-tokenizer=shared

PKGFILES_CSWphp5tokenizer = .*/lib/php/extensions/.*/tokenizer.*

define CSWphp5tokenizer_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling tokenizer extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"tokenizer\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=tokenizer.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=tokenizer.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=tokenizer.so|extension=tokenizer.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=tokenizer.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"tokenizer\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5tokenizer_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling tokenizer extension"

perl -i -plne 's|extension=tokenizer.so|;extension=tokenizer.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"tokenizer\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

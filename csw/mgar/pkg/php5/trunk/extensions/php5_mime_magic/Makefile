PHP5EXT_NAME = mime_magic

PACKAGES += CSWphp5mimemagic

CATALOGNAME_CSWphp5mimemagic = php5_mime_magic
SPKG_DESC_CSWphp5mimemagic = mime magic Extention for PHP5
REQUIRED_PKGS_CSWphp5mimemagic = CSWphp5

CONFIGURE_ARGS += --with-mime-magic=shared

PKGFILES_CSWphp5mimemagic = .*/lib/php/extensions/.*/mime_magic.*

define CSWphp5mime_magic_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mime_magic extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension \"mime_magic\"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=mime_magic.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=mime_magic.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=mime_magic.so|extension=mime_magic.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=mime_magic.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension \"mime_magic\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5mime_magic_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mime_magic extension"

perl -i -plne 's|extension=mime_magic.so|;extension=mime_magic.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension \"mime_magic\"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

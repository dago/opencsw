PHP5EXT_NAME = gettext

PACKAGES += CSWphp5gettext

CATALOGNAME_CSWphp5gettext = php5_gettext
SPKG_DESC_CSWphp5gettext = gettext Extention for PHP5
REQUIRED_PKGS_CSWphp5gettext = CSWphp5 CSWggettextrt

CONFIGURE_ARGS += --with-gettext=shared,$(prefix)

PKGFILES_CSWphp5gettext = .*/lib/php/extensions/.*/gettext.*

define CSWphp5gettext_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling gettext extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "gettext"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=gettext.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=gettext.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=gettext.so|extension=gettext.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=gettext.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "gettext"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5gettext_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling gettext extension"

perl -i -plne 's|extension=gettext.so|;extension=gettext.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "gettext"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

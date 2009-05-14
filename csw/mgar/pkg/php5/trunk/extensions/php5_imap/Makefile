PHP5EXT_NAME = imap

PACKAGES += CSWphp5imap

CATALOGNAME_CSWphp5imap = php5_imap
SPKG_DESC_CSWphp5imap = imap Extention for PHP5
REQUIRED_PKGS_CSWphp5imap = CSWphp5 CSWimaprt CSWkrb5lib CSWosslrt

CONFIGURE_ARGS += --with-imap=shared,$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)

PKGFILES_CSWphp5imap = .*/lib/php/extensions/.*/imap.*

define CSWphp5imap_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling imap extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "imap"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=imap.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=imap.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=imap.so|extension=imap.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=imap.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "imap"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5imap_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling imap extension"

perl -i -plne 's|extension=imap.so|;extension=imap.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "imap"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

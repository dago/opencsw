PHP5EXT_NAME = ftp

PACKAGES += CSWphp5ftp

CATALOGNAME_CSWphp5ftp = php5_ftp
SPKG_DESC_CSWphp5ftp = ftp Extention for PHP5
REQUIRED_PKGS_CSWphp5ftp = CSWphp5 CSWosslrt

CONFIGURE_ARGS += --enable-ftp=shared

PKGFILES_CSWphp5ftp = .*/lib/php/extensions/.*/ftp.*

define CSWphp5ftp_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling ftp extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "ftp"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=ftp.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=ftp.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=ftp.so|extension=ftp.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=ftp.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "ftp"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5ftp_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ftp extension"

perl -i -plne 's|extension=ftp.so|;extension=ftp.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "ftp"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

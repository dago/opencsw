PHP5EXT_NAME = curl

PACKAGES += CSWphp5curl

CATALOGNAME_CSWphp5curl = php5_curl
SPKG_DESC_CSWphp5curl = curl Extention for PHP5
REQUIRED_PKGS_CSWphp5curl  = CSWphp5 CSWcurlrt CSWlibidn 
REQUIRED_PKGS_CSWphp5curl += CSWoldaprt CSWosslrt CSWzlib

CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --with-curlwrappers

PKGFILES_CSWphp5curl = .*/lib/php/extensions/.*/curl.*

define CSWphp5curl_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling curl extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "curl"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=curl.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=curl.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=curl.so|extension=curl.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=curl.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "curl"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5curl_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling curl extension"

perl -i -plne 's|extension=curl.so|;extension=curl.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "curl"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

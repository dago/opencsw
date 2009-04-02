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

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling curl extension"

perl -i -plne 's|;extension=curl.so|extension=curl.so|' ${PHP_INI}

exit 0
endef

define CSWphp5curl_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling curl extension"

perl -i -plne 's|extension=curl.so|;extension=curl.so|' ${PHP_INI}

exit 0
endef


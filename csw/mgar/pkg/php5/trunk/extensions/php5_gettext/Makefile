PHP5EXT_NAME = gettext

PACKAGES += CSWphp5gettext

CATALOGNAME_CSWphp5gettext = php5_gettext
SPKG_DESC_CSWphp5gettext = gettext Extention for PHP5
REQUIRED_PKGS_CSWphp5gettext = CSWphp5 CSWggettextrt

CONFIGURE_ARGS += --with-gettext=shared,$(prefix)

PKGFILES_CSWphp5gettext = .*/lib/php/extensions/.*/gettext.*

define CSWphp5gettext_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling gettext extension"

perl -i -plne 's|;extension=gettext.so|extension=gettext.so|' ${PHP_INI}

exit 0
endef

define CSWphp5gettext_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling gettext extension"

perl -i -plne 's|extension=gettext.so|;extension=gettext.so|' ${PHP_INI}

exit 0
endef


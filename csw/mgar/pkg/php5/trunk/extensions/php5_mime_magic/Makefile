PHP5EXT_NAME = mime_magic

PACKAGES += CSWphp5mimemagic

CATALOGNAME_CSWphp5mimemagic = php5_mime_magic
SPKG_DESC_CSWphp5mimemagic = mime magic Extention for PHP5
REQUIRED_PKGS_CSWphp5mimemagic = CSWphp5

CONFIGURE_ARGS += --with-mime-magic=shared

PKGFILES_CSWphp5mimemagic = .*/lib/php/extensions/.*/mime_magic.*

define CSWphp5mimemagic_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling mime_magic extension"

perl -i -plne 's|;extension=mime_magic.so|extension=mime_magic.so|' ${PHP_INI}

exit 0
endef

define CSWphp5mimemagic_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling mime_magic extension"

perl -i -plne 's|extension=mime_magic.so|;extension=mime_magic.so|' ${PHP_INI}

exit 0
endef


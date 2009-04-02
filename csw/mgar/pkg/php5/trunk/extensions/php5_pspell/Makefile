PHP5EXT_NAME = pspell

PACKAGES += CSWphp5pspell

CATALOGNAME_CSWphp5pspell = php5_pspell
SPKG_DESC_CSWphp5pspell = pspell Extention for PHP5
REQUIRED_PKGS_CSWphp5pspell = CSWphp5 CSWaspell

CONFIGURE_ARGS += --with-pspell=shared,$(prefix)

PKGFILES_CSWphp5pspell = .*/lib/php/extensions/.*/pspell.*

define CSWphp5pspell_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling pspell extension"

perl -i -plne 's|;extension=pspell.so|extension=pspell.so|' ${PHP_INI}

exit 0
endef

define CSWphp5pspell_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling pspell extension"

perl -i -plne 's|extension=pspell.so|;extension=pspell.so|' ${PHP_INI}

exit 0
endef


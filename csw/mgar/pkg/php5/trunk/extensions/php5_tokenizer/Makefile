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

perl -i -plne 's|;extension=tokenizer.so|extension=tokenizer.so|' ${PHP_INI}

exit 0
endef

define CSWphp5tokenizer_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling tokenizer extension"

perl -i -plne 's|extension=tokenizer.so|;extension=tokenizer.so|' ${PHP_INI}

exit 0
endef


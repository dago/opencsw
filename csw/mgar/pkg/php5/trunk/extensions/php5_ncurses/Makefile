PHP5EXT_NAME = ncurses

PACKAGES += CSWphp5ncurses

CATALOGNAME_CSWphp5ncurses = php5_ncurses
SPKG_DESC_CSWphp5ncurses = ncurses Extention for PHP5
REQUIRED_PKGS_CSWphp5ncurses = CSWphp5 CSWncurses

CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)

PKGFILES_CSWphp5ncurses = .*/lib/php/extensions/.*/ncurses.*

define CSWphp5ncurses_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling ncurses extension"

perl -i -plne 's|;extension=ncurses.so|extension=ncurses.so|' ${PHP_INI}

exit 0
endef

define CSWphp5ncurses_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling ncurses extension"

perl -i -plne 's|extension=ncurses.so|;extension=ncurses.so|' ${PHP_INI}

exit 0
endef


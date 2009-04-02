PHP5EXT_NAME = gd

PACKAGES += CSWphp5gd

CATALOGNAME_CSWphp5gd = php5_gd
SPKG_DESC_CSWphp5gd = gd Extention for PHP5
REQUIRED_PKGS_CSWphp5gd  = CSWphp5 CSWftype2 CSWgd CSWjpeg
REQUIRED_PKGS_CSWphp5gd += CSWpng CSWt1lib CSWxpm CSWzlib


CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-xpm-dir=$(prefix)
CONFIGURE_ARGS += --with-ttf=$(prefix)
CONFIGURE_ARGS += --with-freetype-dir=$(prefix)
CONFIGURE_ARGS += --with-t1lib=$(prefix)
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-gd-jis-conv

PKGFILES_CSWphp5gd  = .*/lib/php/extensions/.*/gd.*

define CSWphp5gd_postinstall
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling gd extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "gd"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=gd.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=gd.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=gd.so|extension=gd.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=gd.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "gd"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5gd_preremove
#!/bin/sh

PHP_INI=/opt/csw/php5/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling gd extension"

perl -i -plne 's|extension=gd.so|;extension=gd.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "gd"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

PHP5EXT_NAME = iconv

PACKAGES += CSWphp5iconv

CATALOGNAME_CSWphp5iconv = php5_iconv
SPKG_DESC_CSWphp5iconv = iconv Extention for PHP5
REQUIRED_PKGS_CSWphp5iconv = CSWphp5 CSWiconv

CONFIGURE_ARGS += --with-iconv=shared
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)

EXTRA_CFLAGS   += -I/opt/csw/include
EXTRA_LDFLAGS += -L$(libdir) -R$(libdir)
LIBS = -lrt -lintl 

#PATCHFILES += iconv.diff

PKGFILES_CSWphp5iconv = .*/lib/php/extensions/.*/iconv.*
PKGFILES_CSWphp5iconv = .*/include/php/ext/iconv.*

define CSWphp5iconv_postinstall
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Post Install <===]"
echo "   ===> Enabling iconv extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "iconv"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=iconv.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=iconv.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=iconv.so|extension=iconv.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=iconv.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "iconv"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5iconv_preremove
#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling iconv extension"

perl -i -plne 's|extension=iconv.so|;extension=iconv.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "iconv"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

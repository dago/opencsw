PHP5EXT_NAME = dba

PACKAGES += CSWphp5dba

CATALOGNAME_CSWphp5dba = php5_dba
SPKG_DESC_CSWphp5dba = dba Extention for PHP5
REQUIRED_PKGS_CSWphp5dba = CSWphp5 CSWbdb44 CSWgdbm

CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --with-ndbm
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb44


PKGFILES_CSWphp5dba = .*/lib/php/extensions/.*/dba\.so

define CSWphp5dba_postinstall
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Post Install <===]"
echo "   ===> Enabling dba extension"

if grep 'CSW Extensions' $${PHP_INI} >/dev/null 2>&1; then
    /bin/true
else
    cat << _EOF_
******************************************************************************
* WARNING: Could not enable Extension "dba"
* You will need to enable it by hand as follows:
*
* open $${PHP_INI} in your favorite text editor
* Add the following line to the file, save, and restart your web server
* extension=dba.so
******************************************************************************
_EOF_
exit 0
fi

if grep 'extension=dba.so' $${PHP_INI} >/dev/null 2>&1; then
    perl -i -plne 's|;extension=dba.so|extension=dba.so|' $${PHP_INI}
else
        perl -i -pe 's|.*CSW Extensions|; CSW Extensions\nextension=dba.so|' $${PHP_INI}
        fi

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Enabled Extension "dba"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the install
******************************************************************************
_EOF_


exit 0
endef

define CSWphp5dba_preremove
#!/bin/sh

PHP_INI=/opt/csw/lib/php.ini

echo "[===> Running Pre Remove <===]"
echo "   ===> Disabling dba extension"

perl -i -plne 's|extension=dba.so|;extension=dba.so|' $${PHP_INI}

cat << _EOF_
******************************************************************************
* NOTICE: Successfully Disabled Extension "dba"
* in $${PHP_INI}
*
* You will need to restart your web server to finish the removal
******************************************************************************
_EOF_

exit 0
endef

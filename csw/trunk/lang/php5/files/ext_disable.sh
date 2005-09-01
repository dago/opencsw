#!/bin/sh

CSW_PREFIX=${PKG_INSTALL_ROOT}/opt/csw
PHP_INI=$CSW_PREFIX/php5/lib/php.ini

PKG_INSTALL_ROOT=${PKG_INSTALL_ROOT:-'/'}

PHPEXT=`echo $PKGINST | sed -e 's,CSWphp5,,' -e 's,\..*,,'`
PHPEXT=${PHPEXT:-${PKGINST}}

# Bail if php.ini does not exist
if [ ! -f $PHP_INI ]; then
    cat << END
Cannot locate $PHP_INI -- Please disable $PHPEXT.so manually
in the appropriate php.ini file.

END

    exit 0
fi

/usr/bin/perl -i.bak -plne "s,^(extension=$PHPEXT.so),;\$1," $PHP_INI

echo "PHP extension $PHPEXT.so is disabled in $PHP_INI."

exit 0


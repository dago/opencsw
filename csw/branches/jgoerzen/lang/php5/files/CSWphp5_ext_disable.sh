#!/bin/sh

CSW_PREFIX=/opt/csw
if [ -n "$PKG_INSTALL_ROOT" ]; then
    CSW_PREFIX=${PKG_INSTALL_ROOT}${CSW_PREFIX}
fi

PHP_INI=$CSW_PREFIX/php5/lib/php.ini
PHP_BIN=$CSW_PREFIX/php5/bin
PHP_EXTMGR=$PHP_BIN/phpext

PHPEXT=`echo $PKGINST | sed -e 's,CSWphp5,,' -e 's,\..*,,'`
PHPEXT=${PHPEXT:-${PKGINST}}

# Bail if php.ini does not exist
if [ ! -f $PHP_INI ]; then
    cat << END
Cannot locate $PHP_INI -- Please disable $PHPEXT.so manually
in the appropriate php.ini file using $PHP_EXTMGR

END

    exit 0
fi

$PHP_EXTMGR -i $PHP_INI -d $PHPEXT
if [ $? -ne 0 ]; then
    cat << END
Failed to disable $PHPEXT support -- please examine
$PHP_INI and disable the extension manually.
END
else
    echo "PHP extension $PHPEXT.so is disabled in $PHP_INI."
fi

exit 0


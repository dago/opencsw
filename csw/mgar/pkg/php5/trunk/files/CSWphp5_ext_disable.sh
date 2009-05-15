#!/bin/sh

PHP_INI=${PKG_INSTALL_ROOT}_PHPINIFILE_
PHP_LIB=${PKG_INSTALL_ROOT}_PHPLIBDIR_
PHP_BIN=${PKG_INSTALL_ROOT}_PHPBINDIR_
PHP_EXTMGR=$PHP_BIN/phpext

if [ -z "$PHPEXT" ]; then
    PHPEXT=`echo $PKGINST | sed -e 's,CSWphp5,,' -e 's,\..*,,'`
    PHPEXT=${PHPEXT:-${PKGINST}}
fi

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


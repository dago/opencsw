
# PHP Extensions
XLIST  = bz2
XLIST += curl
XLIST += dba
XLIST += gd
XLIST += gettext
XLIST += gmp
XLIST += imap
XLIST += ldap
XLIST += mcrypt
XLIST += mhash
XLIST += mssql
XLIST += mysql
XLIST += pdomysql
XLIST += mysqli
XLIST += odbc
XLIST += openssl
XLIST += pdoodbc
XLIST += pgsql
XLIST += pdopgsql
XLIST += pspell
XLIST += readline
XLIST += snmp
XLIST += sqlite
XLIST += pdosqlite
XLIST += wddx
XLIST += xsl

DISTFILES += $(foreach N,$(XLIST),$(call admfiles,CSWphp5$(N),prototype depend))


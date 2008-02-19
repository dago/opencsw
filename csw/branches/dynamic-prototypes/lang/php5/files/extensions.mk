
# PHP Extensions
XLIST  = bz2
XLIST += curl
XLIST += dba
XLIST += ftp
XLIST += gd
XLIST += gettext
XLIST += gmp
XLIST += imap
XLIST += ldap
XLIST += mcrypt
XLIST += mhash
XLIST += mssql
XLIST += mysql
XLIST += mysqli
XLIST += odbc
XLIST += pdomysql
XLIST += pdoodbc
XLIST += pdopgsql
XLIST += pdosqlite
XLIST += pgsql
XLIST += pspell
XLIST += readline
XLIST += snmp
XLIST += sqlite
XLIST += wddx
XLIST += xsl

DISTFILES += $(foreach N,$(XLIST),$(call admfiles,CSWphp5$(N),prototype))


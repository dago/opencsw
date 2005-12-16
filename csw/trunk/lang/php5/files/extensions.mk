
# PHP Extensions
XLIST  = bz2
XLIST += curl
XLIST += dba
XLIST += gd
XLIST += gettext
XLIST += gmp
XLIST += ldap
XLIST += mssql
XLIST += mysql
XLIST += pdomysql
XLIST += mysqli
XLIST += odbc
XLIST += pdoodbc
XLIST += pgsql
XLIST += pdopgsql
XLIST += pspell
XLIST += readline
XLIST += snmp
XLIST += sqlite
XLIST += pdosqlite
XLIST += xsl

DISTFILES += $(foreach N,$(XLIST),$(call admfiles,CSWphp5$(N),prototype depend))



# This is all commented out for now, because half of these packages
# aren't in the build system yet...
ifdef ENABLE_DEPENDENCY_BUILD
DEPENDS += lib/openssl
DEPENDS += lib/expat
DEPENDS += lib/zlib
DEPENDS += lib/iconv
DEPENDS += lib/berkeleydb44
DEPENDS += lib/gdbm
DEPENDS += lib/gd
DEPENDS += lib/jpeg
DEPENDS += lib/png
DEPENDS += lib/freetype
DEPENDS += lib/gmp
DEPENDS += lib/unixodbc
DEPENDS += lib/readline
DEPENDS += lib/netsnmp
DEPENDS += lib/sqlite3
DEPENDS += lib/libxslt
DEPENDS += lib/mcrypt
DEPENDS += devel/gettext
DEPENDS += utils/bzip
DEPENDS += net/curl
DEPENDS += server/openldap
DEPENDS += server/mysql5
DEPENDS += server/postgresql
endif


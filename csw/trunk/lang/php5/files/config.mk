
# Details for the pgsql extension 
ifeq ($(shell /bin/uname -p),sparc)
pg_config = $(prefix)/postgresql/bin/sparcv8
else
pg_config = $(prefix)/postgresql/bin
endif

# Configuration
CONFIGURE_ARGS += --prefix=$(prefix)/php5
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-discard-path
#CONFIGURE_ARGS += --enable-debug
CONFIGURE_ARGS += --disable-static

# Features
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --enable-dom=shared
CONFIGURE_ARGS += --with-openssl=shared,$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-zlib=shared,$(prefix)
CONFIGURE_ARGS += --enable-bcmath=shared
CONFIGURE_ARGS += --with-bz2=shared,$(prefix)
CONFIGURE_ARGS += --enable-calendar=shared
CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --with-iconv=shared,$(prefix)
CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --with-ndbm
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb43
CONFIGURE_ARGS += --with-inifile
CONFIGURE_ARGS += --enable-ftp=shared
CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --with-xpm-dir=$(prefix)
CONFIGURE_ARGS += --with-freetype-dir=$(prefix)
CONFIGURE_ARGS += --with-t1lib=$(prefix)
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-gd-jis-conv
CONFIGURE_ARGS += --enable-exif=shared
CONFIGURE_ARGS += --with-gettext=shared,$(prefix)
CONFIGURE_ARGS += --with-gmp=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)
CONFIGURE_ARGS += --enable-mbstring=shared
CONFIGURE_ARGS += --enable-pdo=shared
CONFIGURE_ARGS += --with-mssql=shared,$(prefix)
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)/mysql4
CONFIGURE_ARGS += --with-pdo-mysql=shared,$(prefix)/mysql4
CONFIGURE_ARGS += --with-mysqli=shared
CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)
CONFIGURE_ARGS += --with-pdo-odbc=shared,unixODBC,$(prefix)
CONFIGURE_ARGS += --with-pgsql=shared,$(pg_config)
CONFIGURE_ARGS += --with-pdo-pgsql=shared,$(pg_config)
CONFIGURE_ARGS += --with-pspell=shared,$(prefix)
CONFIGURE_ARGS += --with-readline=shared,$(prefix)
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --enable-shmop=shared
#CONFIGURE_ARGS += --enable-simplexml=shared
CONFIGURE_ARGS += --with-snmp=shared,$(prefix)
CONFIGURE_ARGS += --enable-soap=shared
CONFIGURE_ARGS += --enable-sockets=shared
CONFIGURE_ARGS += --with-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --with-pdo-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --enable-sqlite-utf8
CONFIGURE_ARGS += --enable-sysvmsg=shared
CONFIGURE_ARGS += --enable-sysvsem=shared
CONFIGURE_ARGS += --enable-sysvshm=shared
CONFIGURE_ARGS += --enable-xml
CONFIGURE_ARGS += --with-expat-dir=$(prefix)
CONFIGURE_ARGS += --with-xsl=shared,$(prefix)
CONFIGURE_ARGS += --enable-wddx=shared
CONFIGURE_ARGS += --enable-xmlreader=shared

# Previously distributed extensions moved to PECL
#CONFIGURE_ARGS += --enable-dio=shared
#CONFIGURE_ARGS += --with-fam=shared
#CONFIGURE_ARGS += --enable-yp=shared

# Need a fix for ncurses.h use of stdbool.h
#CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)


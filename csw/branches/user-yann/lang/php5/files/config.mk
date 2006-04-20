
# Can't do direct downloads of PHP from php.net
#MASTER_SITES = http://www.php.net/downloads.php
SPKG_SOURCEURL = http://www.php.net/downloads.php
DISTFILES     += $(GARNAME)-$(GARVERSION).tar.bz2

# Disable Tests (report submitted to PHP QA)
ENABLE_TEST = 0

# PostgreSQL
ifeq ($(shell /bin/uname -p),sparc)
pg_config = $(prefix)/postgresql/bin/sparcv8
else
pg_config = $(prefix)/postgresql/bin
endif

# MySQL 5
PATH := $(PATH):$(prefix)/mysql5/bin
export PATH

# BerkeleyDB
EXTRA_LIB += $(prefix)/bdb43/lib
EXTRA_INC += $(prefix)/bdb43/lib

# IMAP C Client
MASTER_SITES += ftp://ftp.cac.washington.edu/imap/
DISTFILES    += c-client.tar.Z
IMAPVERSION   = imap-2004f

# SAPI Common Configuration
CONFIGURE_ARGS += --prefix=$(prefix)/php5
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-discard-path
#CONFIGURE_ARGS += --enable-debug
CONFIGURE_ARGS += --disable-static

# Features
CONFIGURE_ARGS += --with-imap=../$(IMAPVERSION)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)/ssl
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
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)/mysql5
CONFIGURE_ARGS += --with-pdo-mysql=shared,$(prefix)/mysql5
CONFIGURE_ARGS += --with-mysqli=shared,$(prefix)/mysql5/bin/mysql_config
CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)
CONFIGURE_ARGS += --with-pdo-odbc=shared,unixODBC,$(prefix)
CONFIGURE_ARGS += --with-pgsql=shared,$(pg_config)
CONFIGURE_ARGS += --with-pdo-pgsql=shared,$(pg_config)
CONFIGURE_ARGS += --with-pspell=shared,$(prefix)
CONFIGURE_ARGS += --with-readline=shared,$(prefix)
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --enable-shmop=shared
#CONFIGURE_ARGS += --enable-simplexml=shared
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
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
CONFIGURE_ARGS += --enable-pcntl=shared
CONFIGURE_ARGS += --enable-fastcgi
CONFIGURE_ARGS += --with-mcrypt=shared,$(prefix)
CONFIGURE_ARGS += --with-mhash=shared,$(prefix)

# Previously distributed extensions moved to PECL
#CONFIGURE_ARGS += --enable-dio=shared
#CONFIGURE_ARGS += --with-fam=shared
#CONFIGURE_ARGS += --enable-yp=shared

# Need a fix for ncurses.h use of stdbool.h
#CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)


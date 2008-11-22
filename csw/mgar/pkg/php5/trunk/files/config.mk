
MASTER_SITES   = http://us.php.net/distributions/
SPKG_SOURCEURL = http://www.php.net/downloads.php
DISTFILES     += $(GARNAME)-$(GARVERSION).tar.bz2

# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1

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
EXTRA_LIB += $(prefix)/bdb44/lib
EXTRA_INC += $(prefix)/bdb44/lib

# IMAP C Client
#MASTER_SITES += ftp://ftp.cac.washington.edu/imap/
#DISTFILES    += c-client.tar.Z
#IMAPVERSION   = imap-2004f

# SAPI Common Configuration
CONFIGURE_ARGS += --prefix=$(prefix)/php5

#CONFIGURE_ARGS += --enable-discard-path
#CONFIGURE_ARGS += --enable-debug
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/php5/bin
CONFIGURE_ARGS += --enable-memory-limit

# Features
CONFIGURE_ARGS += --with-imap=shared,$(prefix)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)/ssl
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --enable-dom
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --enable-bcmath
CONFIGURE_ARGS += --with-bz2=shared,$(prefix)
CONFIGURE_ARGS += --enable-calendar
CONFIGURE_ARGS += --enable-dbx
CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)
CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --with-ndbm
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb44
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
CONFIGURE_ARGS += --enable-exif
CONFIGURE_ARGS += --with-gettext=shared,$(prefix)
CONFIGURE_ARGS += --with-gmp=shared,$(prefix)
ifeq ($(usesunldap),1)
CONFIGURE_ARGS += --with-ldap=shared,/usr
else
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)
endif
CONFIGURE_ARGS += --enable-mbstring
CONFIGURE_ARGS += --enable-mbstr-enc-trans
CONFIGURE_ARGS += --enable-mbregex
CONFIGURE_ARGS += --enable-pdo
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
CONFIGURE_ARGS += --enable-shmop
CONFIGURE_ARGS += --enable-simplexml
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
CONFIGURE_ARGS += --with-snmp=shared,$(prefix)
CONFIGURE_ARGS += --enable-soap
CONFIGURE_ARGS += --enable-magic-quotes
CONFIGURE_ARGS += --enable-sockets
CONFIGURE_ARGS += --with-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --with-pdo-sqlite=shared,$(prefix)
CONFIGURE_ARGS += --enable-sqlite-utf8
CONFIGURE_ARGS += --enable-sysvmsg
CONFIGURE_ARGS += --enable-sysvsem
CONFIGURE_ARGS += --enable-sysvshm
CONFIGURE_ARGS += --enable-track-vars
CONFIGURE_ARGS += --enable-trans-sid
CONFIGURE_ARGS += --enable-xml
CONFIGURE_ARGS += --with-expat-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-xsl=shared,$(prefix)
CONFIGURE_ARGS += --enable-wddx=shared
CONFIGURE_ARGS += --enable-xmlreader
CONFIGURE_ARGS += --with-xmlrpc
CONFIGURE_ARGS += --with-mcrypt=shared,$(prefix)
CONFIGURE_ARGS += --with-mhash=shared,$(prefix)
CONFIGURE_ARGS += --with-mime-magic
CONFIGURE_ARGS += --enable-json
CONFIGURE_ARGS += --enable-filter=shared
CONFIGURE_ARGS += --enable-zip
#CONFIGURE_ARGS += --with-tidy=shared

# Stuff from CSQamp
CONFIGURE_ARGS += --enable-spl
CONFIGURE_ARGS += --with-pcre-regex
CONFIGURE_ARGS += --enable-session
CONFIGURE_ARGS += --with-pear

# Previously distributed extensions moved to PECL
#CONFIGURE_ARGS += --enable-dio=shared
#CONFIGURE_ARGS += --with-fam=shared
#CONFIGURE_ARGS += --enable-yp=shared

# Need a fix for ncurses.h use of stdbool.h
#CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)


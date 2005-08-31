GARNAME = php
GARVERSION = 5.0.4
CATEGORIES = lang

DESCRIPTION = A high-level scripting language.
define BLURB
  PHP is a widely-used Open Source general-purpose scripting language that is
  especially suited for Web development and can be embedded into HTML. Its
  syntax draws upon C, Java, and Perl, and is easy to learn. PHP runs on many
  different platforms and can be used as a standalone executable or as a
  module under a variety of Web servers. It has excellent support for
  databases, XML, LDAP, IMAP, Java, various Internet protocols, and general
  data manipulation, and is extensible via its powerful API. It is actively
  developed and supported by a talented and energetic international team.
  Numerous Open Source and commercial PHP-based application packages are
  available.
endef

# Can't do direct downloads of PHP

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWap2modphp5.gspec

# Fix up configure script
PATCHFILES += config.diff

#DEPENDS += server/apache2 server/mysql4

# Configuration
CONFIGURE_ARGS  = --prefix=$(prefix)/php5
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-discard-path
CONFIGURE_ARGS += --enable-debug
CONFIGURE_ARGS += --disable-static

# Features
CONFIGURE_ARGS += --with-libxml-dir=$(prefix)
CONFIGURE_ARGS += --enable-dom=shared
CONFIGURE_ARGS += --with-openssl=shared,$(prefix)/ssl
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
CONFIGURE_ARGS += --with-db3=$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb43
CONFIGURE_ARGS += --with-inifile
CONFIGURE_ARGS += --enable-dio=shared
CONFIGURE_ARGS += --with-fam=shared
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
#CONFIGURE_ARGS += --with-imap=$(WORKSRC)/imap
#CONFIGURE_ARGS += --with-kerberos=$(prefix)
#CONFIGURE_ARGS += --with-imap-ssl=$(prefix)/ssl
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)
CONFIGURE_ARGS += --with-mbstring=shared
#CONFIGURE_ARGS += --with-mcve=shared,$(prefix)
#CONFIGURE_ARGS += --with-openssl-dir=$(prefix)/ssl
CONFIGURE_ARGS += --with-mssql=shared,$(prefix)
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)/mysql4
CONFIGURE_ARGS += --with-mysqli=shared
CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)
CONFIGURE_ARGS += --with-pgsql=shared,$(prefix)/postgresql
CONFIGURE_ARGS += --with-pspell=shared,$(prefix)
CONFIGURE_ARGS += --with-readline=shared,$(prefix)
CONFIGURE_ARGS += --with-mm=$(prefix)
CONFIGURE_ARGS += --enable-shmop=shared
CONFIGURE_ARGS += --enable-simplexml=shared
CONFIGURE_ARGS += --enable-snmp=shared,$(prefix)
CONFIGURE_ARGS += --enable-soap=shared
CONFIGURE_ARGS += --enable-sockets=shared
CONFIGURE_ARGS += --with-sqlite=shared
CONFIGURE_ARGS += --enable-sysvmsg=shared
CONFIGURE_ARGS += --enable-sysvsem=shared
CONFIGURE_ARGS += --enable-sysvshm=shared
CONFIGURE_ARGS += --enable-xml=shared
CONFIGURE_ARGS += --with-expat-dir=$(prefix)
CONFIGURE_ARGS += --with-xsl=shared,$(prefix)
CONFIGURE_ARGS += --enable-yp=shared

# Need a fix for ncurses.h use of stdbool.h
#CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)

ENABLE_TEST = 0

include ../category.mk

INSTALL_ENV += INSTALL_ROOT=$(DESTDIR)

EXTRA_LIB = $(prefix)/bdb43/lib
EXTRA_INC = $(prefix)/bdb43/include

# This is required so that we don't try to regen the
# sqlite parser.
pre-build:
	@touch $(WORKSRC)/ext/sqlite/libsqlite/src/parse.c
	@$(MAKECOOKIE)

post-install:
	@cp -f $(WORKSRC)/php.ini-recommended $(DESTDIR)$(sysconfdir)/php.ini


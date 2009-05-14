GARNAME    = php
GARVERSION = 4.4.9
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

MASTER_SITES   = http://us.php.net/distributions/
SPKG_SOURCEURL = http://www.php.net/downloads.php
DISTFILES     += $(GARNAME)-$(GARVERSION).tar.bz2

INSTALL_ENV   += INSTALL_ROOT=$(DESTDIR)
PHP4ROOT       = $(DESTDIR)$(prefix)/php4

STRIP_DIRS    += $(PHP4ROOT)/lib/php/extensions/*/
STRIP_DIRS    += $(PHP4ROOT)/bin

PACKAGES = CSWphp4 
CATALOGNAME_CSWphp4   = php4
SPKG_DESC_CSWphp4     = A High-Level Scripting Languages
REQUIRED_PKGS_CSWphp4 = 

PATCHFILES  = pgsql.diff

EXTRA_LIB += $(prefix)/bdb44/lib
EXTRA_INC += $(prefix)/bdb44/include
EXTRA_CFLAGS = -I$(prefix)/include/ncursesw
CONFIGURE_ARGS += --prefix=$(prefix)/php4
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-exec-dir=$(prefix)/php4/bin

CONFIGURE_ARGS += --enable-bcmath=shared
CONFIGURE_ARGS += --enable-calendar=shared
CONFIGURE_ARGS += --enable-cgi
CONFIGURE_ARGS += --enable-cli
CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --with-curlwrappers
CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --enable-exif
CONFIGURE_ARGS += --enable-fastcgi
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-mbregex=shared
CONFIGURE_ARGS += --enable-mbstring=shared
CONFIGURE_ARGS += --enable-sockets
CONFIGURE_ARGS += --with-bz2=shared,$(prefix)
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb44
CONFIGURE_ARGS += --with-dom-exslt=$(prefix)
CONFIGURE_ARGS += --with-dom-xslt=$(prefix)
CONFIGURE_ARGS += --with-dom=shared,$(prefix)
CONFIGURE_ARGS += --with-expat-dir=$(prefix)
CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-gettext=shared,$(prefix)
CONFIGURE_ARGS += --with-gmp=shared,$(prefix)
CONFIGURE_ARGS += --with-iconv=shared
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)
CONFIGURE_ARGS += --with-imap=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=$(prefix)
CONFIGURE_ARGS += --with-mcal=shared,$(prefix)
CONFIGURE_ARGS += --with-mssql=shared,$(prefix)
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)
CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)
CONFIGURE_ARGS += --with-openssl=shared,$(prefix)
CONFIGURE_ARGS += --with-pgsql=shared,$(prefix)/postgresql
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-unixODBC=shared,$(prefix)
CONFIGURE_ARGS += --with-xmlrpc=shared,$(prefix)
CONFIGURE_ARGS += --with-zlib=shared


# Disable Tests (report submitted to PHP QA)
SKIPTEST = 1
ENABLE_CHECK = 0

# System Rules/Configuration
include gar/category.mk

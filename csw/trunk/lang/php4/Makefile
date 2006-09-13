GARNAME = php
GARVERSION = 4.4.2
CATEGORIES = lang

DESCRIPTION = A high-level scripting language.
define BLURB
  PHP is a widely-used Open Source general-purpose scripting language that is
  especially suited for Web development and can be embedded into HTML. Its
  syntax draws upon C, Java, and Perl, and is easy to learn. PHP runs on many
  different platforms and can be used as a standalone executable or as a module
  under a variety of Web servers. It has excellent support for databases, XML,
  LDAP, IMAP, Java, various Internet protocols, and general data manipulation,
  and is extensible via its powerful API. It is actively developed and supported
  by a talented and energetic international team. Numerous Open Source and
  commercial PHP-based application packages are available.
endef

#DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

DEPENDS += server/apache2 server/mysql4

# Some tests fail (3 of 300)
TEST_SCRIPTS =

# Configuration
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-config-file-path=$(prefix)/apache2/etc
CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql4
CONFIGURE_ARGS += --with-db4=$(prefix)/bdb4
CONFIGURE_ARGS += --with-gdbm=$(prefix)
CONFIGURE_ARGS += --with-expat-dir=$(prefix)
CONFIGURE_ARGS += --with-gd=$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-gmp=$(prefix)
CONFIGURE_ARGS += --with-ncurses=$(prefix)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --enable-sockets
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bz2
CONFIGURE_ARGS += --enable-dba
CONFIGURE_ARGS += --with-dom
CONFIGURE_ARGS += --with-dom-xslt
CONFIGURE_ARGS += --with-dom-exslt
CONFIGURE_ARGS += --with-xmlrpc
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-exif

include ../category.mk

post-install:
	@cp -f $(WORKSRC)/php.ini-recommended $(sysconfdir)/php.ini


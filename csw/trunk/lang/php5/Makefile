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

#DEPENDS += server/apache2 server/mysql4

# Configuration
CONFIGURE_ARGS  = --prefix=$(prefix)/php5
CONFIGURE_ARGS += --with-apxs2=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --enable-force-cgi-redirect
CONFIGURE_ARGS += --enable-discard-path
CONFIGURE_ARGS += --enable-debug
CONFIGURE_ARGS += --disable-static

# Features
CONFIGURE_ARGS += --enable-bcmath
CONFIGURE_ARGS += --with-bz2=shared
CONFIGURE_ARGS += --enable-calendar
CONFIGURE_ARGS += --with-curl=shared,$(prefix)
CONFIGURE_ARGS += --enable-dba=shared
CONFIGURE_ARGS += --with-db4=shared,$(prefix)/bdb4
CONFIGURE_ARGS += --with-gdbm=shared,$(prefix)
CONFIGURE_ARGS += --with-inifile
CONFIGURE_ARGS += --with-flatfile
CONFIGURE_ARGS += --enable-dio
CONFIGURE_ARGS += --with-fam=shared
CONFIGURE_ARGS += --enable-ftp
CONFIGURE_ARGS += --with-gd=shared,$(prefix)
CONFIGURE_ARGS += --with-jpeg-dir=$(prefix)
CONFIGURE_ARGS += --with-png-dir=$(prefix)
CONFIGURE_ARGS += --with-freetype-dir=$(prefix)
CONFIGURE_ARGS += --enable-gd-native-ttf
CONFIGURE_ARGS += --enable-gd-jis-conv
CONFIGURE_ARGS += --with-gettext=shared,$(prefix)
CONFIGURE_ARGS += --with-gmp=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap=shared,$(prefix)
CONFIGURE_ARGS += --with-ldap-sasl=shared,$(prefix)
CONFIGURE_ARGS += --with-ncurses=shared,$(prefix)
CONFIGURE_ARGS += --with-mysql=shared,$(prefix)/mysql4
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
CONFIGURE_ARGS += --with-pgsql=shared,$(prefix)
CONFIGURE_ARGS += --with-readline=shared,$(prefix)
CONFIGURE_ARGS += --enable-shmop
CONFIGURE_ARGS += --enable-soap
CONFIGURE_ARGS += --enable-sockets
CONFIGURE_ARGS += --enable-sysvmsg
CONFIGURE_ARGS += --enable-sysvsem
CONFIGURE_ARGS += --enable-sysvshm
CONFIGURE_ARGS += --with-expat-dir=$(prefix)
CONFIGURE_ARGS += --with-xsl=shared,$(prefix)
CONFIGURE_ARGS += --enable-yp

include ../category.mk

EXTRA_LIB = $(prefix)/bdb43/lib
EXTRA_INC = $(prefix)/bdb43/include

#post-install:
#	@cp -f $(WORKSRC)/php.ini-recommended $(sysconfdir)/php.ini


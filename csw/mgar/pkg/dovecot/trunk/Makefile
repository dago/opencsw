GARNAME = dovecot
GARVERSION = 1.1.8
CATEGORIES = server

DESCRIPTION = Secure IMAP server
define BLURB
  Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like systems,
  written with security primarily in mind. Dovecot is an excellent choice for
  both small and large installations. It's fast, simple to set up, requires no
  special administration and it uses very little memory.
endef

MASTER_SITES = http://dovecot.org/releases/1.1/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWdovecot,)

REQUIRED_PKGS = CSWosslrt CSWmysql5rt 

PREREQUISITE_PKGS  = CSWmysql5devel CSWmysql5rt
PREREQUISITE_PKGS += CSWoldaprt CSWoldapdevel

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# See http://www.mail-archive.com/dovecot@dovecot.org/msg15562.html
PATCHFILES = patch-unsetenv.diff

# TODO
# * Consider LDAP issues: http://opencsw.org/bugtrack/view.php?id=2760
# * --enable-header-install & split packages (dovecot, dovecotdevel)
# * Build and package Dovecot Sieve plugin http://wiki.dovecot.org/LDA/Sieve
# * ...

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-sqlite
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-ssldir=$(DESTDIR)/ssl

EXTRA_LIB = /opt/csw/mysql5/lib/mysql
EXTRA_INC = /opt/csw/mysql5/include/mysql

include gar/category.mk

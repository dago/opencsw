GARNAME = dovecot
GARVERSION = 1.1.11
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
DISTFILES += $(call admfiles,CSWdovecotdevel,)

SPKG_SOURCEURL = http://dovecot.org/

SPKG_DESC_CSWdovecot      = Secure IMAP server
SPKG_DESC_CSWdovecotdevel = Dovecot secure IMAP server header files

REQUIRED_PKGS_CSWdovecot      = CSWosslrt CSWmysql5rt CSWoldaprt
REQUIRED_PKGS_CSWdovecotdevel = CSWdovecot

PREREQUISITE_PKGS  = CSWossldevel CSWosslrt
PREREQUISITE_PKGS += CSWmysql5devel CSWmysql5rt
PREREQUISITE_PKGS += CSWoldaprt CSWoldapdevel

PKGFILES_CSWdovecotdevel = $(PKGFILES_DEVEL)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# Work around non-existing unsetenv() on Solaris 8
# See http://www.mail-archive.com/dovecot@dovecot.org/msg15562.html
PATCHFILES = patch-unsetenv.diff

TEST_SCRIPTS	=

# TODO
# * Consider LDAP issues: http://opencsw.org/bugtrack/view.php?id=2760
# * Build and package Dovecot Sieve plugin http://wiki.dovecot.org/LDA/Sieve
# * ...

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pop3d
CONFIGURE_ARGS += --with-lda
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-sqlite
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-ssldir=$(DESTDIR)/ssl
CONFIGURE_ARGS += --enable-header-install
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(GARNAME)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw/$(GARNAME)

EXTRA_LIB = /opt/csw/mysql5/lib/mysql
EXTRA_INC = /opt/csw/mysql5/include/mysql

include gar/category.mk

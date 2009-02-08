# TODO
# * postinstall: Create dovecot user(s) or advise user to do so
# * Create default config so that service can startup right away?
# * Build and package Dovecot Sieve plugin http://wiki.dovecot.org/LDA/Sieve

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
SPKG_SOURCEURL = http://dovecot.org/

PACKAGES = CSWdovecot CSWdovecotdevel
CATALOGNAME_CSWdovecotdevel = dovecot_devel

SPKG_DESC_CSWdovecot      = Secure IMAP server
SPKG_DESC_CSWdovecotdevel = Dovecot secure IMAP server header files

REQUIRED_PKGS_CSWdovecot      = CSWosslrt CSWmysql5rt CSWoldaprt
REQUIRED_PKGS_CSWdovecot      = CSWsasl CSWsqlite3 CSWzlib CSWlibnet
REQUIRED_PKGS_CSWdovecot      = CSWcswclassutils
REQUIRED_PKGS_CSWdovecotdevel = CSWdovecot

PREREQUISITE_PKGS  = CSWossldevel CSWosslrt
PREREQUISITE_PKGS += CSWmysql5devel CSWmysql5rt
PREREQUISITE_PKGS += CSWoldaprt CSWoldapdevel
PREREQUISITE_PKGS += CSWsasl 
PREREQUISITE_PKGS += CSWsqlite3 CSWsqlite3dev

PKGFILES_CSWdovecotdevel = $(PKGFILES_DEVEL)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# No test suite for Dovecot available
TEST_SCRIPTS	=

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pop3d
CONFIGURE_ARGS += --with-lda
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-sqlite
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-ssldir=/opt/csw/ssl
CONFIGURE_ARGS += --enable-header-install
CONFIGURE_ARGS += --localstatedir=/var/opt/csw
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw/$(GARNAME)

EXTRA_LIB = /opt/csw/mysql5/lib/mysql
EXTRA_INC = /opt/csw/mysql5/include/mysql

include gar/category.mk

# init script / SMF integration
SPKG_CLASSES_CSWdovecot = none cswinitsmf
PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswdovecot$$$$/ { $$$$2 = "cswinitsmf" } { print }'

post-install-modulated: DOCS = NEWS AUTHORS COPYING.LGPL COPYING.MIT
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 755 $(FILEDIR)/CSWdovecot.cswdovecot  \
		$(DESTDIR)/etc/opt/csw/init.d/cswdovecot
	@$(MAKECOOKIE)

# TODO
# - SSL certs to /etc/opt/csw/ssl?
# - /var/run/dovecot instead of /var/opt/csw/run?
NAME = dovecot
VERSION = 2.0.15
CATEGORIES = server

DESCRIPTION = Secure IMAP server
define BLURB
  Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like systems,
  written with security primarily in mind. Dovecot is an excellent choice for
  both small and large installations. It's fast, simple to set up, requires no
  special administration and it uses very little memory.
endef

SPKG_SOURCEURL = http://dovecot.org/
MASTER_SITES   = http://dovecot.org/releases/2.0/
DISTFILES      = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX   = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES  = CSWdovecot CSWdovecot-dev

CATALOGNAME_CSWdovecot = dovecot
CATALOGNAME_CSWdovecot-dev = dovecot_dev

SPKG_DESC_CSWdovecot = Secure IMAP server
SPKG_DESC_CSWdovecot-dev = Dovecot secure IMAP server header files

OBSOLETED_BY_CSWdovecot-dev = CSWdovecotdevel
CATALOGNAME_CSWdovecotdevel = dovecot_devel_stub

RUNTIME_DEP_PKGS_CSWdovecot += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibz1
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibpq
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWdovecot += CSWosslrt
RUNTIME_DEP_PKGS_CSWdovecot += CSWoldaprt

PKGFILES_CSWdovecot-dev = $(PKGFILES_DEVEL)

# These directories belong to CSWosslrt
PROTOTYPE_FILTER  = awk '\
	$$$$3 == "/opt/csw/ssl/certs" { next } \
	$$$$3 == "/opt/csw/ssl/private" { next } \
	 { print }'

# No test suite for Dovecot available
TEST_SCRIPTS	=

# Override some paths for configure
sysconfdir=/etc/opt/csw/dovecot
localstatedir=/var/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += MYSQL_LIBS="-L/opt/csw/mysql5/lib -L/opt/csw/lib  -L/opt/csw/mysql5/lib/mysql -lmysqlclient -L/opt/csw/lib -lz -lposix4 -lresolv -lc -lgen -lsocket -lnsl -lm"
CONFIGURE_ARGS += --with-gssapi
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-pgsql
CONFIGURE_ARGS += --with-sqlite
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-ssldir=/opt/csw/ssl
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bzlib

EXTRA_LIB = /opt/csw/postgresql/lib
EXTRA_INC = /opt/csw/include/mysql /opt/csw/postgresql/include

STRIP_DIRS  = $(DESTDIR)$(libexecdir)/dovecot

# cswclassutils integration
INITSMF    = /etc/opt/csw/init.d/cswdovecot
USERGROUP = /etc/opt/csw/pkg/CSWdovecot/cswusergroup
SAMPLECONF = .*/dovecot.pem $(sysconfdir)/dovecot.conf
MIGRATE_FILES = dovecot.conf

include gar/category.mk

pre-install-modulated:
	perl -pi -e 's|/etc/ssl|/opt/csw/ssl|' $(WORKSRC)/doc/mkcert.sh
	perl -pi -e '\
		s| /var/run| /var/opt/csw/run|; \
		s| /etc/ssl| /opt/csw/ssl|; \
		s| /usr/libexec| /opt/csw/libexec|; \
		s| /usr/lib/dovecot| /opt/csw/lib/dovecot|; \
		s| /usr/local| /opt/csw|;' \
		$(WORKSRC)/doc/example-config/dovecot.conf
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: DOCS = NEWS AUTHORS COPYING.LGPL COPYING.MIT
post-install-modulated: CSWDOCS=README.CSW changelog.CSW
post-install-modulated: SSLDIR = $(DESTDIR)/opt/csw/ssl
post-install-modulated:
	perl -pi -e 's/usr\/local/opt\/csw/g' \
		$(DESTDIR)/opt/csw/share/doc/dovecot/wiki/*
	perl -pi -e 's/usr\/share/opt\/csw\/share/g' \
		$(DESTDIR)/opt/csw/share/doc/dovecot/wiki/*
	perl -pi -e 's/usr\/local/opt\/csw/g' \
		$(DESTDIR)/opt/csw/share/doc/dovecot/example-config/conf.d/*

	# Include these in the pkg. dovecot will create them otherwise
	# with root:root ownership, which conflicts with other pkg's
	ginstall -d $(DESTDIR)$(localstatedir)/run 
	ginstall -d $(DESTDIR)$(localstatedir)/lib

	cp $(DESTDIR)/opt/csw/share/doc/dovecot/example-config/dovecot.conf \
		$(DESTDIR)$(sysconfdir)/dovecot.conf

	# Create self-signed sample cert
	ginstall -d $(SSLDIR)/certs
	ginstall -d $(SSLDIR)/private
	( cd $(WORKSRC)/doc; SSLDIR=$(SSLDIR) /bin/sh ./mkcert.sh )
	chmod 400 $(SSLDIR)/private/dovecot.pem

	# Copy documentation (upstream + CSW) and mkcert.sh
	ginstall -d $(DOCDEST)
	cp $(addprefix $(FILEDIR)/,$(CSWDOCS)) $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS))    $(DOCDEST)
	ginstall -m 755 $(WORKSRC)/doc/mkcert.sh $(DOCDEST)
	cp $(WORKSRC)/doc/dovecot-openssl.cnf $(DOCDEST)

	# Copy init script
	ginstall -Dm 755 $(FILEDIR)/cswdovecot  \
		$(DESTDIR)/etc/opt/csw/init.d/cswdovecot

	# Copy cswusergroup
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWdovecot
	ginstall -m 444 $(FILEDIR)/cswusergroup \
		$(DESTDIR)/etc/opt/csw/pkg/CSWdovecot/

	@$(MAKECOOKIE)

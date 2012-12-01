# TODO
# - SSL certs to /etc/opt/csw/ssl?
# - /var/run/dovecot instead of /var/opt/csw/run?
NAME = dovecot
VERSION = 2.1.12
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Secure IMAP server
define BLURB
  Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like systems,
  written with security primarily in mind. Dovecot is an excellent choice for
  both small and large installations. It's fast, simple to set up, requires no
  special administration and it uses very little memory.
endef

SPKG_SOURCEURL = http://dovecot.org/
MASTER_SITES   = http://dov1cot.org/releases/2.0/
DISTFILES      = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX   = $(NAME)-(\d+GARCOMPILER    = SOS12d+(?:\.\d+)*).tar.gz

PACKAGES  = CSWdovecot CSWdovecot-dev

CATALOGNAME_CSWdovecot = dovecot
CATALOGNAME_CSWdovecot-dev = dovecot_dev

SPKG_DESC_CSWdovecot = Secure IMAP server
SPKG_DESC_CSWdovecot-dev = Dovecot secure IMAP server header files

OBSOLETED_BY_CSWdovecot-dev = CSWdovecotdevel
CATALOGNAME_CSWdovecotdevel = dovecot_devel_stub

RUNTIME_DEP_PKGS_CSWdovecot += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibz1
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_gssapi-krb5-2
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibpq5Wdovecot += CSWlibpq
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWdovecot += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWdovecot += CSWlibldap2-4-2

PKGFILES_CSWdovecot-dev = $(PKGFILES_DEVEL)

# These directories belong to CSWosslrt
PROTOTYPE_FILTER  = awk '\
	$$$$3 == "/opt/csw/ssl/certs" { next } \
	$$$$3 == "/opt/csw/ssl/private" { nexREINPLACEMENTS += ul

REINPLACE_MATCH_ul = /usr/local
REINPLACE_WITH_ul = $(prefix)
REINPLACE_FILES_ul += src/plugins/fts/decode2text.sh
REINPLACE_FILES_ul += doc/wiki/LDA.Sendmail.txt
REINPLACE_FILES_ul += doc/wiki/CompilingSource.txt
REINPLACE_FILES_ul += doc/wiki/HowTo.PopBSMTPAndDovecot.txtext } \
	 { print }'

# No test suite for Dovecot available
TEST_SCRIPTS	=

CONFIGURE_ARGS  = $(DIRPATHS"
CONFIGURE_ARGS += --with-gssapi
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-pgsql
CONFIGURE_ARGS += --with-sqlite
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGetc/opt/csw/ssl
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bzlib

EXTRA_INC = /opt/csw/include/mysql /opt/csw/include/postgresqlw/postgresql/include

STRIP_DIRS  = $(DESTDIR)$(libexecdir)/dovecot

# cswclassutils integration
INITSMF    = /etc/opt/csw/init.d/cswdovecot
USERGROUP = /etc/opt/csw/pkg/CSWdovecot/cswusergroup
SAMPLECONF = .*/dovecot.pem $(sysconfdir)/dovecot/dovecot.conf
MIGRATE_FILES = dovecot.conf

# the perl search and replace is missing this.  Need to rework the below perl
# lines.  For now overriding since the file(s) are oi/LDA.Sendmail.txt

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk

pre-install-modulated:
	perl etc/opt/csw/ssl|' $(WORKSRC)/doc/mkcert.sh
	perl -pi -e '\
		s| /var/run| /var/opt/csw/run|; \
		s| /etc/ssl| /etc|; \
		s| /etc/ssl| /opt/csw/ssl|; \
		s| /usr/libex/dovecot|; \
		s| /usr/lib/dovecot| /opt/csw/lib/dovecot/opt/csw/lib/dovecot|; \
		s| /usr/local| /opt/csw|;' \
		$(WORKSRC)/doc/example-config/dovecot.conf
	perl -pi etc -e '\
		s|/etc/ssl|/opt/csw/ssl|; \
		s|/usr/local|/opt/csw|;' \
		$(WORKSRC)/doc/example-config/conf.d/*
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: DOCS = NEWS AUTHORS COPYING.LGPL COPYING.MIT
post-install-modulated: CSWDOCS=README.CSW changelog.CSW
post-install-modulated: etc/opt/csw/ssl
post-install-modulated:

	perl -pi -e '\
		s|/etc/ssl|/etc -e '\
		s|/etc/ssl|/opt/csw/ssl|; \
		s|/usr/local|/opt/csw|; \
		s|/usr/share|/opt/csw/share|;' \
		$(DESTDIR)/opt/csw/share/doc/dovecot/wiki/*

	# Include these in the pkg. dovecot will create them otherwise
	# with root:root ownership, which conflicts with other pkg's
	ginstall -d $(DESTDIR)$(localstatedir)/run 
	ginstall -d $(DESTDIR)$(localstatedir)/lib

	cp $(FILEDIR)/dovecot-minimal.conf \
		$(DESTDIR)$(sysconfdir)/dovecot/dovecot.conf

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
		$(DESTDIR)/etc/opt/csw/pkg/CSWdoveco
# TODO
# - Migrate config from /opt/csw/etc/dovecot to /etc
# - example.conf patch needs tweaking (rejected)
# - SSL certs to /etc/opt/csw/ssl?
# - USERGROUP doesn't work yet, wrong usage?
# - /var/run/dovecot instead of /var/opt/csw/run?
GARNAME = dovecot
GARVERSION = 1.1.20
CATEGORIES = server

DESCRIPTION = Secure IMAP server
define BLURB
  Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like systems,
  written with security primarily in mind. Dovecot is an excellent choice for
  both small and large installations. It's fast, simple to set up, requires no
  special administration and it uses very little memory.
endef

SPKG_SOURCEURL = http://dovecot.org/
MASTER_SITES   = http://dovecot.org/releases/1.1/
DISTFILES      = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX   = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Sieve plugin is packaged via a post-package hook (see package-sieveplugin:)
PACKAGES  = CSWdovecot CSWdovecot-devel CSWdovecot-sieve
NOPACKAGE = CSWdovecot-sieve

CATALOGNAME_CSWdovecot = dovecot
CATALOGNAME_CSWdovecot-devel = dovecot_devel
CATALOGNAME_CSWdovecot-sieve = dovecot_sieve

SPKG_DESC_CSWdovecot = Secure IMAP server
SPKG_DESC_CSWdovecot-devel = Dovecot secure IMAP server header files
SPKG_DESC_CSWdovecot-sieve = Dovecot secure IMAP server sieve plugin

REQUIRED_PKGS_CSWdovecot       = CSWosslrt CSWmysql5rt CSWoldaprt CSWlibpq
REQUIRED_PKGS_CSWdovecot      += CSWsasl CSWsqlite3 CSWzlib CSWlibnet
REQUIRED_PKGS_CSWdovecot      += CSWbzip2 CSWiconv CSWcswclassutils
REQUIRED_PKGS_CSWdovecot      += CSWkrb5lib
REQUIRED_PKGS_CSWdovecot-devel = CSWdovecot
REQUIRED_PKGS_CSWdovecot-sieve = CSWdovecot

PREREQUISITE_PKGS  = CSWossldevel CSWosslrt
PREREQUISITE_PKGS += CSWmysql5devel CSWmysql5rt
PREREQUISITE_PKGS += CSWoldaprt CSWoldapdevel
PREREQUISITE_PKGS += CSWsasl 
PREREQUISITE_PKGS += CSWsqlite3
PREREQUISITE_PKGS += CSWlibpq
PREREQUISITE_PKGS += CSWkrb5lib CSWkrb5libdev

PKGFILES_CSWdovecot-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWdovecot-sieve = .*sieve.*

# These directories belong to CSWosslrt
PROTOTYPE_FILTER  = awk '\
	$$$$3 == "/opt/csw/ssl/certs" { next } \
	$$$$3 == "/opt/csw/ssl/private" { next } \
	 { print }'

# No test suite for Dovecot available
TEST_SCRIPTS	=

# Adjust the comment about file paths in the example conf header
PATCHFILES += patch-exampleconf.diff

# Override some paths for configure
sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pop3d
CONFIGURE_ARGS += --with-gssapi
CONFIGURE_ARGS += --with-lda
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-pgsql
CONFIGURE_ARGS += --with-sqlite
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-ssldir=/opt/csw/ssl
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --with-bzlib
CONFIGURE_ARGS += --enable-header-install

EXTRA_LIB = /opt/csw/mysql5/lib/mysql /opt/csw/postgresql/lib
EXTRA_INC = /opt/csw/mysql5/include/mysql /opt/csw/postgresql/include

STRIP_DIRS  = $(DESTDIR)$(libexecdir)/dovecot

# cswclassutils integration
INITSMF    = $(sysconfdir)/init.d/cswdovecot
USERGROUP  = dovecot:dovecot:Dovecot IMAP Server:/var/opt/csw/run/dovecot/login:/bin/false
SAMPLECONF = .*/dovecot.pem $(sysconfdir)/dovecot.conf

include gar/category.mk

# Adjust file paths in various files. Not a prerequisite to the remaining 
# build process, but i found it easiest to put it here and not clutter 
# post-install even more
pre-install-modulated:
	perl -pi -e 's|/etc/ssl|/opt/csw/ssl|' $(WORKSRC)/doc/mkcert.sh
	perl -pi -e '\
		s| /var/run| /var/opt/csw/run|; \
		s| /etc/ssl| /opt/csw/ssl|; \
		s| /usr/libexec| /opt/csw/libexec|; \
		s| /usr/lib/dovecot| /opt/csw/lib/dovecot|;' \
		$(WORKSRC)/dovecot-example.conf
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: DOCS = NEWS AUTHORS COPYING.LGPL COPYING.MIT
post-install-modulated: CSWDOCS=README.CSW changelog.CSW
post-install-modulated: SSLDIR = $(DESTDIR)/opt/csw/ssl
post-install-modulated: build-and-install-sieveplugin

	# Include these in the pkg. dovecot will create them otherwise
	# with root:root ownership, which conflicts with other pkg's
	ginstall -d $(DESTDIR)$(localstatedir)/run 
	ginstall -d $(DESTDIR)$(localstatedir)/lib

	cp $(DESTDIR)$(sysconfdir)/dovecot-example.conf \
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
	@$(MAKECOOKIE)

post-package: package-sieveplugin
	@$(MAKECOOKIE)

# Extra targets for the Sieve plugin build and packaging process, invoked
# via post-install-modulated and post-package.

SIEVEVERSION = 1.1.8
SIEVEDIST    = dovecot-sieve-$(SIEVEVERSION)
SIEVEURL     = http://www.dovecot.org/releases/sieve/$(SIEVEDIST).tar.gz

build-and-install-sieveplugin: CONFIGURE_ARGS = $(DIRPATHS)
build-and-install-sieveplugin: CONFIGURE_ARGS += --with-dovecot=../$(WORKSRC)
build-and-install-sieveplugin:
	@echo
	@echo [===== NOW BUILDING extra cmusieve plugin =====]
	@echo
	wget -nc $(SIEVEURL)
	gtar xzf $(SIEVEDIST).tar.gz
	(cd $(SIEVEDIST); \
		$(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS); \
		$(BUILD_ENV) gmake $(BUILD_ARGS); \
		$(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) $(INSTALL_ARGS) install; )
	rm -rf $(SIEVEDIST)*
	@$(MAKECOOKIE)

# Sieve plugin needs to be packaged with version != $(GARVERSION)
package-sieveplugin:
	gmake -o post-package \
		NOPACKAGE="CSWdovecot CSWdovecot-devel" SPKG_VERSION=$(SIEVEVERSION) \
		repackage

# TODO:
# * Bump to 1.1.13, http://hg.dovecot.org/dovecot-1.1/rev/a2013dedbad0

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

PACKAGES = CSWdovecot CSWdovecot-devel CSWdovecot-sieve
CATALOGNAME_CSWdovecot = dovecot
CATALOGNAME_CSWdovecotdevel = dovecot_devel
CATALOGNAME_CSWdovecot-sieve = dovecot_sieve

# Sieve plugin is packaged individually (see package-sieveplugin:)
NOPACKAGE = CSWdovecot-sieve

# CSWdovecot is not installed on the build farm and as such its dependent
# packages throw errors when fed to checkpkg
ENABLE_CHECK=0

SPKG_SOURCEURL = http://dovecot.org/
SPKG_DESC_CSWdovecot = Secure IMAP server
SPKG_DESC_CSWdovecotdevel = Dovecot secure IMAP server header files
SPKG_DESC_CSWdovecot-sieve = Dovecot secure IMAP server sieve plugin
SPKG_CLASSES_CSWdovecot = none cswusergroup cswcpsampleconf cswinitsmf

REQUIRED_PKGS_CSWdovecot       = CSWosslrt CSWmysql5rt CSWoldaprt CSWlibpq
REQUIRED_PKGS_CSWdovecot      += CSWsasl CSWsqlite3 CSWzlib CSWlibnet
REQUIRED_PKGS_CSWdovecot      += CSWbzip2 CSWiconv CSWcswclassutils
REQUIRED_PKGS_CSWdovecot      += CSWkrb5lib
REQUIRED_PKGS_CSWdovecotdevel  = CSWdovecot
REQUIRED_PKGS_CSWdovecot-sieve = CSWdovecot

PREREQUISITE_PKGS  = CSWossldevel CSWosslrt
PREREQUISITE_PKGS += CSWmysql5devel CSWmysql5rt
PREREQUISITE_PKGS += CSWoldaprt CSWoldapdevel
PREREQUISITE_PKGS += CSWsasl 
PREREQUISITE_PKGS += CSWsqlite3
PREREQUISITE_PKGS += CSWlibpq
PREREQUISITE_PKGS += CSWkrb5lib CSWkrb5libdev

PKGFILES_CSWdovecotdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWdovecot-sieve = .*sieve.*

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# No test suite for Dovecot available
TEST_SCRIPTS	=

# See http://dovecot.org/list/dovecot/2009-February/037273.html
PATCHFILES = patch-authcrash.diff
# See http://dovecot.org/list/dovecot/2009-March/038201.html
PATCHFILES += patch-enosys.diff
# Adjust the comment about file paths in the example conf header
PATCHFILES += patch-exampleconf.diff

# Override some paths for configure
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

PROTOTYPE_FILTER  = awk '\
	$$$$3 ~ /\/init.d\/cswdovecot$$$$/ { $$$$2 = "cswinitsmf" } \
	$$$$3 ~ /cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
	$$$$3 ~ /dovecot.pem.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
	$$$$3 ~ /dovecot.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
	$$$$3 == "/opt/csw/ssl/certs" { next } \
	$$$$3 == "/opt/csw/ssl/private" { next } \
	 { print }'

include gar/category.mk

# Adjust file paths in various files. Not a prerequisite to the remaining 
# build process, but i found it easiest to put it here and not clutter 
# post-install even more
pre-install-modulated:
	@perl -pi -e 's|/etc/ssl|/opt/csw/ssl|' $(WORKSRC)/doc/mkcert.sh
	@perl -pi -e '\
		s| /var/run| /var/opt/csw/run|; \
		s| /etc/ssl| /opt/csw/ssl|; \
		s| /usr/libexec| /opt/csw/libexec|; \
		s| /usr/lib/dovecot| /opt/csw/lib/dovecot|;' \
		$(WORKSRC)/dovecot-example.conf
	@$(MAKECOOKIE)

# Maybe there is a nicer way to build this via modulations ...
build-and-install-sieveplugin: CONFIGURE_ARGS = $(DIRPATHS)
build-and-install-sieveplugin: CONFIGURE_ARGS += --with-dovecot=../$(WORKSRC)
build-and-install-sieveplugin:
	@echo
	@echo [===== NOW BUILDING extra cmusieve plugin =====]
	@echo
	@wget -nc http://www.dovecot.org/releases/sieve/dovecot-sieve-1.1.6.tar.gz
	@gtar xzf dovecot-sieve-1.1.6.tar.gz
	@(cd dovecot-sieve-1.1.6; \
		$(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS); \
		$(BUILD_ENV) gmake $(BUILD_ARGS); \
		$(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) $(INSTALL_ARGS) install; )
	@rm -rf dovecot-sieve-1.1.6*
	@$(MAKECOOKIE)

# Sieve plugin needs to be packaged with version != $(GARVERSION)
package-sieveplugin:
	@gmake -o post-package \
		NOPACKAGE="CSWdovecot CSWdovecotdevel" SPKG_VERSION=1.1.6 \
		repackage


post-install-modulated: DOCS = NEWS AUTHORS COPYING.LGPL COPYING.MIT
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: SSLDIR = $(DESTDIR)/opt/csw/ssl
post-install-modulated: build-and-install-sieveplugin
	@ginstall -d $(DOCDEST)
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -d $(DESTDIR)$(sysconfdir)/pkg/CSWdovecot
	@ginstall -d $(SSLDIR)/certs
	@ginstall -d $(SSLDIR)/private

	@cp $(DESTDIR)$(sysconfdir)/dovecot-example.conf \
		$(DESTDIR)$(sysconfdir)/dovecot.conf.CSW

	# Create self-signed sample cert
	@( cd $(WORKSRC)/doc; SSLDIR=$(SSLDIR) /bin/sh ./mkcert.sh )
	@mv $(SSLDIR)/certs/dovecot.pem $(SSLDIR)/certs/dovecot.pem.CSW
	@mv $(SSLDIR)/private/dovecot.pem $(SSLDIR)/private/dovecot.pem.CSW
	@chmod 400 $(SSLDIR)/private/dovecot.pem.CSW

	# Copy documentation (upstream + CSW) and mkcert.sh
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@cp $(FILEDIR)/CSWdovecot.changelog.CSW $(DOCDEST)/changelog.CSW
	@cp $(FILEDIR)/CSWdovecot.README.CSW $(DOCDEST)/README.CSW
	@ginstall -m 755 $(WORKSRC)/doc/mkcert.sh $(DOCDEST)
	@cp $(WORKSRC)/doc/dovecot-openssl.cnf $(DOCDEST)

	# Files for cswinitsmf and cswusergroup
	@ginstall -m 755 $(FILEDIR)/CSWdovecot.cswdovecot  \
		$(DESTDIR)/etc/opt/csw/init.d/cswdovecot
	@ginstall -m 644 $(FILEDIR)/CSWdovecot.cswusergroup \
		$(DESTDIR)$(sysconfdir)/pkg/CSWdovecot/cswusergroup
	@$(MAKECOOKIE)

post-package: package-sieveplugin
	@$(MAKECOOKIE)

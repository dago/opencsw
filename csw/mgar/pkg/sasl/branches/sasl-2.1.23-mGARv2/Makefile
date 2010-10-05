GARNAME = sasl
GARVERSION = 2.1.24
FILEVERSION = $(GARVERSION)rc1
CATEGORIES = lib

DESCRIPTION = Simple Authentication and Security Layer
define BLURB
   SASL is the Simple Authentication and Security Layer, a method for adding authentication 
   support to connection-based protocols. To use SASL, a protocol includes a command for 
   identifying and authenticating a user to a server and for optionally negotiating 
   protection of subsequent protocol interactions. If its use is negotiated, a security 
   layer is inserted between the protocol and the connection.
endef

MASTER_SITES = ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/
DISTNAME = cyrus-$(GARNAME)-$(GARVERSION)
DISTFILES = cyrus-$(GARNAME)-$(FILEVERSION).tar.gz
DISTFILES += cswsaslauthd.init saslauthd.init.CSW
DISTFILES += README.sasl README.saslauthd

# PATCHFILES = saslauthd-doc.diff saslauthd-groff.diff ltmain.diff

PACKAGES = CSWsasl CSWsaslauthd CSWsaslgssapi CSWsaslsql

SPKG_SOURCEURL = http://asg.web.cmu.edu/sasl/

CATALOGNAME_CSWsasl = sasl
CATALOGNAME_CSWsaslauthd = saslauthd
CATALOGNAME_CSWsaslgssapi = sasl_gssapi
CATALOGNAME_CSWsaslsql = sasl_sql

RUNTIME_DEP_PKGS_CSWsasl = CSWosslrt CSWbdb47 CSWoldaprt CSWkrb5lib
RUNTIME_DEP_PKGS_CSWsaslauthd = CSWosslrt CSWoldaprt CSWkrb5lib
RUNTIME_DEP_PKGS_CSWsaslgssapi = CSWsasl CSWkrb5lib
RUNTIME_DEP_PKGS_CSWsaslsql = CSWsasl CSWlibpq CSWmysql5rt CSWsqlite

CHECKPKG_OVERRIDES_CSWsaslgssapi += surplus-dependency|CSWsasl
CHECKPKG_OVERRIDES_CSWsaslsql += surplus-dependency|CSWsasl

SPKG_DESC_CSWsasl = Cyrus Simple Authentication and Security Layer
SPKG_DESC_CSWsaslauthd = Cyrus Simple Authentication and Security Layer Authentication Daemon
SPKG_DESC_CSWsaslgssapi = Cyrus Simple Authentication and Security Layer GSSAPI Binding
SPKG_DESC_CSWsaslsql = Cyrus Simple Authentication and Security Layer SQL Binding

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = cyrus-$(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_CFLAGS = -D__EXTENSIONS__

BUILD_ENV = _REENTRANT=1

EXTRA_LIB = $(prefix)/bdb47/lib

EXTRA_INC  = /opt/csw/include/gssapi
EXTRA_INC += /opt/csw/mysql5/include/mysql
EXTRA_INC += /opt/csw/postgresql/include

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

# Do not use LD_OPTIONS as it breaks tests by using the installed libraries
# before the newly built ones.
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)
LD_OPTIONS =

BUILD64 = 1
NOISALIST = 1

NODIRPATHS = --docdir

# SASL configuration
CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --disable-static 
CONFIGURE_ARGS += --enable-sql
CONFIGURE_ARGS += --with-bdb-libdir=/opt/csw/bdb47/lib 
CONFIGURE_ARGS += --with-bdb-incdir=/opt/csw/bdb47/include/ 
CONFIGURE_ARGS += --with-saslauthd=$(localstatedir)/saslauthd 
CONFIGURE_ARGS += --with-ipctype=unix 
CONFIGURE_ARGS += --with-ldap=$(libdir)
# Autoconf tries to find the directory with the shared lib in it. Because of the
# ISA suffix for 64 bit we must specify the exact library location and add
# the include directories manually.
CONFIGURE_ARGS += --with-mysql=$(abspath $(prefix)/mysql5/lib/$(MM_LIBDIR)/mysql)
CONFIGURE_ARGS += --with-pgsql=$(abspath $(prefix)/postgresql/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --with-openssl=$(libdir)
CONFIGURE_ARGS += --with-dbpath=$(sysconfdir)/sasldb2
CONFIGURE_ARGS += --with-plugindir=$(libdir)/sasl2 
CONFIGURE_ARGS += --enable-login

SED=/usr/bin/sed
EGREP=/usr/bin/egrep
max_cmd_line=65535

TEST_TARGET = check

#INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir libdir includedir mandir

PKGFILES_CSWsaslauthd = /etc/opt/csw/init.d/cswsaslauthd.init
PKGFILES_CSWsaslauthd += $(bindir)/testsaslauthd
PKGFILES_CSWsaslauthd += $(sbindir)/saslauthd
PKGFILES_CSWsaslauthd += $(mandir)/.*/saslauthd\.8
PKGFILES_CSWsaslauthd += $(docdir)/saslauthd/LDAP_SASLAUTHD
PKGFILES_CSWsaslauthd += $(docdir)/saslauthd/README.saslauthd
PKGFILES_CSWsaslauthd += /var/opt/csw/saslauthd
PKGFILES_CSWsaslgssapi = $(libdir)/sasl2/libgssapiv2\..*
PKGFILES_CSWsaslsql = $(libdir)/sasl2/libsql\..*

MIGRATECONF = saslauthd.conf sasldb2
PRESERVECONF = saslauthd.conf

INITSMF = /etc/opt/csw/init.d/cswsaslauthd.init

CSWsasl_usergroup = :sasl:::::: 

include gar/category.mk

post-install-modulated: testsaslauthd install-testsaslauthd install-doc
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d/
	ginstall $(WORKDIR)/cswsaslauthd.init $(DESTDIR)/etc/opt/csw/init.d
	@$(MAKECOOKIE)

DOC_FILES = rfc1321.txt \
                rfc1939.txt \
                rfc2104.txt \
                rfc2195.txt \
                rfc2222.txt \
                rfc2243.txt \
                rfc2245.txt \
                rfc2289.txt \
                rfc2444.txt \
                rfc2595.txt \
                rfc2831.txt \
                rfc2945.txt \
                rfc3174.txt \
                testing.txt \
                server-plugin-flow.fig \
                draft-burdis-cat-srp-sasl-xx.txt \
                draft-ietf-sasl-anon-xx.txt \
                draft-ietf-sasl-crammd5-xx.txt \
                draft-ietf-sasl-gssapi-xx.txt \
                draft-ietf-sasl-plain-xx.txt \
                draft-ietf-sasl-rfc2222bis-xx.txt \
                draft-ietf-sasl-rfc2831bis-xx.txt \
                draft-ietf-sasl-saslprep-xx.txt \
                draft-murchison-sasl-login-xx.txt \
                draft-newman-sasl-c-api-xx.txt \
                draft-newman-sasl-passdss-xx.txt \
                programming.html \
                sysadmin.html \
                gssapi.html \
                advanced.html \
                options.html \
                plugprog.html \
                appconvert.html \
                macosx.html \
                windows.html \
                readme.html \
                mechanisms.html \
                upgrading.html \
                index.html \
                components.html \
                install.html \
                TODO \
                ONEWS

testsaslauthd:
	cd $(WORKSRC)/saslauthd && make testsaslauthd

install-testsaslauthd:
	mkdir -p $(DESTDIR)$(bindir)
	cp $(WORKSRC)/saslauthd/testsaslauthd $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)/var/opt/csw/saslauthd

install-doc:
	mkdir -p $(DESTDIR)$(docdir)/sasl
	cp $(WORKDIR)/README.sasl $(DESTDIR)$(docdir)/sasl/README.CSW
	list='$(DOC_FILES)'; for file in $$list; do \
		cp $(WORKSRC)/doc/$$file $(DESTDIR)$(docdir)/sasl; \
	     done
	mkdir -p $(DESTDIR)$(docdir)/saslauthd
	cp $(WORKSRC)/saslauthd/LDAP_SASLAUTHD $(DESTDIR)$(docdir)/saslauthd
	cp $(WORKDIR)/README.saslauthd $(DESTDIR)$(docdir)/saslauthd/README.CSW


GARNAME = sasl
GARVERSION = 2.1.22
CATEGORIES = lib

DESCRIPTION = Simple Authentication and Security Layer
define BLURB
   SASL is the Simple Authentication and Security Layer, a method for adding authentication 
   support to connection-based protocols. To use SASL, a protocol includes a command for 
   identifying and authenticating a user to a server and for optionally negotiating 
   protection of subsequent protocol interactions. If its use is negotiated, a security 
   layer is inserted between the protocol and the connection.
endef

# Source location
MASTER_SITES = ftp://ftp.andrew.cmu.edu/pub/cyrus-mail

# Visitor information
SPKG_SOURCEURL = http://asg.web.cmu.edu/sasl/

WORKSRC = $(WORKDIR)/cyrus-$(GARNAME)-$(GARVERSION)

DISTFILES = cyrus-$(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = cyrus-$(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_ENV = _REENTRANT=1

TEST_TARGET = check

SED=/usr/bin/sed
EGREP=/usr/bin/egrep
max_cmd_line=65535

# SASL libraries and utilities
DISTFILES += $(call admfiles,CSWsasl,$(ADMSTANDARD) $(ADMISCRIPTS))
# SASL authentication server
DISTFILES += $(call admfiles,CSWsaslauthd,$(ADMADDON))
# SASL sql plugin
DISTFILES += $(call admfiles,CSWsaslsql,$(ADMSTANDARD))
# SASL gssapi plugin
DISTFILES += $(call admfiles,CSWsaslgssapi,$(ADMSTANDARD))

# Init files for SASLAUTHD
DISTFILES += cswsaslauthd.init saslauthd.init.CSW

PATCHFILES = saslauthd-doc.diff saslauthd-groff.diff ltmain.diff

#INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir libdir includedir mandir

EXTRA_LIBS += /opt/csw/bdb4/lib
EXTRA_LIBS += /opt/csw/mysql4/lib
EXTRA_LIBS += /opt/csw/postgresql/lib

# SASL configuration
CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --disable-static 
CONFIGURE_ARGS += --enable-sql
CONFIGURE_ARGS += --with-bdb-libdir=/opt/csw/bdb4/lib 
CONFIGURE_ARGS += --with-bdb-incdir=/opt/csw/bdb4/include/ 
CONFIGURE_ARGS += --with-saslauthd=/var/opt/csw/saslauthd 
CONFIGURE_ARGS += --with-ipctype=unix 
CONFIGURE_ARGS += --with-ldap=/opt/csw 
CONFIGURE_ARGS += --with-mysql=/opt/csw/mysql4/ 
CONFIGURE_ARGS += --with-pgsql=/opt/csw/postgresql 
CONFIGURE_ARGS += --with-openssl=/opt/csw 
CONFIGURE_ARGS += --with-dbpath=/opt/csw/etc/sasldb2 
CONFIGURE_ARGS += --with-plugindir=/opt/csw/lib/sasl2 
CONFIGURE_ARGS += --enable-login


all: .DEFAULT
.DEFAULT:
	@true

post-install: testsaslauthd install-testsaslauthd install-doc

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

INSTDIR = $(DESTDIR)/opt/csw


testsaslauthd:
	cd $(WORKSRC)/saslauthd && make testsaslauthd

install-testsaslauthd:
	-mkdir -p $(INSTDIR)/bin
	cp $(WORKSRC)/saslauthd/testsaslauthd $(INSTDIR)/bin

install-doc:
	-mkdir -p $(INSTDIR)/share/doc/sasl
	list='$(DOC_FILES)'; for file in $$list; do \
		cp $(WORKSRC)/doc/$$file $(INSTDIR)/share/doc/sasl; \
	     done
	cp files/README.sasl $(INSTDIR)/share/doc/sasl/README.CSW
	-mkdir -p $(INSTDIR)/share/doc/saslauthd
	cp $(WORKSRC)/saslauthd/LDAP_SASLAUTHD $(INSTDIR)/share/doc/saslauthd
	cp files/README.saslauthd $(INSTDIR)/share/doc/saslauthd/README.CSW


include gar/category.mk

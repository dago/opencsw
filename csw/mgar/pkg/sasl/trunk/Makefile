NAME = sasl
VERSION = 2.1.25
FILEVERSION = $(VERSION)
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Simple Authentication and Security Layer
define BLURB
   SASL is the Simple Authentication and Security Layer, a method for adding authentication 
   support to connection-based protocols. To use SASL, a protocol includes a command for 
   identifying and authenticating a user to a server and for optionally negotiating 
   protection of subsequent protocol interactions. If its use is negotiated, a security 
   layer is inserted between the protocol and the connection.
endef

MASTER_SITES = ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/
DISTNAME = cyrus-$(NAME)-$(VERSION)
DISTFILES = cyrus-$(NAME)-$(FILEVERSION).tar.gz
# This file will be renamed to cswsaslauthd during install
DISTFILES += cswsaslauthd.init
DISTFILES += saslauthd.init.CSW
DISTFILES += saslauthd.conf.CSW
DISTFILES += README.sasl
DISTFILES += README.saslauthd
DISTFILES += changelog.CSW
DISTFILES += CSWsaslauthd.postmsg

EXPANDVARS = CSWsaslauthd.postmsg
POSTMSG = $(docdir)/saslauthd/CSWsaslauthd.postmsg

# For some reason or another, plugins are installed in
# $(prefix)/lib/sasl2, regardless of what --with-plugindir is set
# to. This patch will make the install routine put the plugins to
# the path specified by --with-plugindir
PATCHFILES = 0001-Install-plugin-at-proper-location.patch
# This patch makes libtool honor -R properly, without this
# patch libtool discards -R options passed with LDFLAGS
PATCHFILES += ltmain.diff

VENDOR_URL = http://asg.web.cmu.edu/sasl/

PACKAGES += CSWsasl
SPKG_DESC_CSWsasl = Cyrus Simple Authentication and Security Layer
RUNTIME_DEP_PKGS_CSWsasl = CSWosslrt
RUNTIME_DEP_PKGS_CSWsasl += CSWbdb48
RUNTIME_DEP_PKGS_CSWsasl += CSWlibsasl2-2

PACKAGES += CSWsaslauthd
SPKG_DESC_CSWsaslauthd = Cyrus Simple Authentication and Security Layer Authentication Daemon
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWsasl
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWosslrt
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWoldaprt
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsaslauthd += CSWlibkrb5support0
CHECKPKG_OVERRIDES_CSWsaslauthd += surplus-dependency|CSWsasl
PKGFILES_CSWsaslauthd = $(sysconfdir)/init.d/cswsaslauthd
PKGFILES_CSWsaslauthd += $(sysconfdir)/saslauthd.init.CSW
PKGFILES_CSWsaslauthd += $(sysconfdir)/saslauthd.conf.CSW
PKGFILES_CSWsaslauthd += $(sbindir)/testsaslauthd
PKGFILES_CSWsaslauthd += $(sbindir)/saslauthd
PKGFILES_CSWsaslauthd += $(mandir)/.*/saslauthd\.8
PKGFILES_CSWsaslauthd += $(docdir)/saslauthd/LDAP_SASLAUTHD
PKGFILES_CSWsaslauthd += $(docdir)/saslauthd/README.saslauthd
PKGFILES_CSWsaslauthd += $(docdir)/saslauthd/README.CSW
PKGFILES_CSWsaslauthd += $(docdir)/saslauthd/CSWsaslauthd.postmsg
PKGFILES_CSWsaslauthd += /var/opt/csw/saslauthd

PACKAGES += CSWsaslgssapi
CATALOGNAME_CSWsaslgssapi = sasl_gssapi
SPKG_DESC_CSWsaslgssapi = Cyrus Simple Authentication and Security Layer GSSAPI Binding
RUNTIME_DEP_PKGS_CSWsaslgssapi = CSWsasl CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsaslgssapi += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsaslgssapi += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsaslgssapi += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsaslgssapi += CSWlibkrb5support0
CHECKPKG_OVERRIDES_CSWsaslgssapi += catalogname-does-not-match-pkgname|pkgname=CSWsaslgssapi|catalogname=sasl_gssapi|expected-catalogname=saslgssapi
PKGFILES_CSWsaslgssapi = $(call pkgfiles_lib,sasl2/libgs2.so)
PKGFILES_CSWsaslgssapi += $(call pkgfiles_lib,sasl2/libgssapiv2.so)

PACKAGES += CSWsaslsql
CATALOGNAME_CSWsaslsql = sasl_sql
SPKG_DESC_CSWsaslsql = Cyrus Simple Authentication and Security Layer SQL Binding
RUNTIME_DEP_PKGS_CSWsaslsql = CSWsasl
# 2011-10-24 raos
# libpq 64-bit is not available on Solaris 10 x86.
ifneq ($(MODULATION),isa-amd64)
RUNTIME_DEP_PKGS_CSWsaslsql += CSWlibpq
endif
RUNTIME_DEP_PKGS_CSWsaslsql += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWsaslsql += CSWlibmysqlclient15
CHECKPKG_OVERRIDES_CSWsaslsql += catalogname-does-not-match-pkgname|pkgname=CSWsaslsql|catalogname=sasl_sql|expected-catalogname=saslsql
PKGFILES_CSWsaslsql = $(call pkgfiles_lib,sasl2/libsql.so)

PACKAGES += CSWlibsasl2-2
SPKG_DESC_CSWlibsasl2-2 = Simple authentication and security layer library, libsasl2.so.2
PKGFILES_CSWlibsasl2-2 += $(call pkgfiles_lib,libsasl2.so.2)

PACKAGES += CSWsasl-dev
SPKG_DESC_CSWsasl-dev = Development files for SASL
PKGFILES_CSWsasl-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsasl-dev += CSWlibsasl2-2

PACKAGES += CSWsaslsample
CATALOGNAME_CSWsaslsample = sasl_sample
SPKG_DESC_CSWsaslsample = Cyrus Simple Authentication and Security Layer sample client/server
RUNTIME_DEP_PKGS_CSWsaslsample = CSWsasl
RUNTIME_DEP_PKGS_CSWsaslsample += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWsaslsample += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsaslsample += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWsaslsample += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWsaslsample += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsaslsample += CSWlibkrb5support0
PKGFILES_CSWsaslsample = $(bindir)/sasl-sample-server
PKGFILES_CSWsaslsample += $(bindir)/sasl-sample-client
# The plugins of CSWsasl are needed, else the functionality
# of saslsample is very limited
CHECKPKG_OVERRIDES_CSWsaslsample += surplus-dependency|CSWsasl
CHECKPKG_OVERRIDES_CSWsaslsample += catalogname-does-not-match-pkgname|pkgname=CSWsaslsample|catalogname=sasl_sample|expected-catalogname=saslsample


BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWmysql-dev
BUILD_DEP_PKGS += CSWlibpq
BUILD_DEP_PKGS += CSWoldapdevel 
BUILD_DEP_PKGS += CSWlibsqlite3-dev
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWbdb48devel

EXTRA_CFLAGS = -D__EXTENSIONS__

EXTRA_BUILD_ENV = _REENTRANT=1

EXTRA_INC  = $(includedir)/gssapi
EXTRA_INC += $(includedir)/mysql
EXTRA_INC += $(prefix)/bdb48/include
EXTRA_INC += /opt/csw/postgresql/include

EXTRA_LIB  = $(prefix)/bdb48/lib
EXTRA_LIB += $(prefix)/postgresql/lib

# Do not use LD_OPTIONS as it breaks tests by using the installed libraries
# before the newly built ones.
EXTRA_RUNPATH_ISALIST	= $(EXTRA_RUNPATH_DIRS)

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

NODIRPATHS = --docdir

# SASL configuration
CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --disable-static 
CONFIGURE_ARGS += --enable-sql
CONFIGURE_ARGS += --enable-login
CONFIGURE_ARGS += --enable-plain
CONFIGURE_ARGS += --enable-cram
CONFIGURE_ARGS += --enable-digest
CONFIGURE_ARGS += --enable-scram
CONFIGURE_ARGS += --enable-otp
CONFIGURE_ARGS += --enable-gssapi
CONFIGURE_ARGS += --with-bdb-libdir=$(abspath /opt/csw/bdb48/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --with-bdb-incdir=/opt/csw/bdb48/include/ 
CONFIGURE_ARGS += --with-bdb=db-4.8
CONFIGURE_ARGS += --with-saslauthd=$(localstatedir)/saslauthd 
CONFIGURE_ARGS += --with-ipctype=unix 
CONFIGURE_ARGS += --with-ldap=$(libdir)
# SQLite3 is supported
CONFIGURE_ARGS += --with-sqlite=no
CONFIGURE_ARGS += --with-sqlite3=$(prefix)
# Autoconf tries to find the directory with the shared lib in it. Because of the
# ISA suffix for 64 bit we must specify the exact library location and add
# the include directories manually.
#CONFIGURE_ARGS += --with-mysql=$(libdir)
CONFIGURE_ARGS += --with-mysql=$(libdir)
# 2011-10-24 raos
# libpq 64-bit is not available on Solaris 10 x86.
# Although the configure script figures this out, the build
# breaks complaining that libpq cannot be found for amd64.
ifneq ($(MODULATION),isa-amd64)
CONFIGURE_ARGS += --with-pgsql=$(abspath $(prefix)/postgresql/lib/$(MM_LIBDIR))
endif
CONFIGURE_ARGS += --with-openssl=$(libdir)
CONFIGURE_ARGS += --with-dbpath=$(sysconfdir)/sasldb2
CONFIGURE_ARGS += --with-plugindir=$(libdir)/sasl2 
CONFIGURE_ARGS += --with-configdir=$(libdir)/sasl2 
# This is for 32/64 switching. We do this all by ourselves, do not use SASLs mechanism
# See also the patch 0001-Install-plugin-at-proper-location.patch
CONFIGURE_ARGS += --without-lib-subdir

SED=/usr/bin/sed
EGREP=/usr/bin/egrep
max_cmd_line=65535
SED_USR_LOCAL= sed -e 's|/usr/local|/opt/csw|g'

MIGRATE_FILES_CSWsasl      = "sasldb2"
MIGRATE_FILES_CSWsaslauthd = "saslauthd.conf"
MIGRATE_SOURCE_DIR	   = /opt/csw/etc
MIGRATE_DEST_DIR	   = $(sysconfdir)
PRESERVECONF = /etc/opt/csw/saslauthd.conf /etc/opt/csw/saslauthd.init

INITSMF = /etc/opt/csw/init.d/cswsaslauthd

CSWsasl_usergroup = :sasl:::::: 

include gar/category.mk

# This is for building the sample sasl server/client
# which can be used to test the sasl installation
post-build-modulated:
	test -d $(WORKSRC)/sample && cd $(WORKSRC)/sample && /usr/bin/env -i $(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) 
	@$(MAKECOOKIE)


post-install-modulated: install-doc fix-path-manpages install-sample
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d/
	ginstall $(WORKDIR)/saslauthd.init.CSW $(DESTDIR)$(sysconfdir)
	ginstall $(WORKDIR)/saslauthd.conf.CSW $(DESTDIR)$(sysconfdir)
	ginstall $(WORKDIR)/cswsaslauthd.init $(DESTDIR)$(sysconfdir)/init.d/cswsaslauthd
	ginstall $(WORKDIR)/CSWsaslauthd.postmsg $(DESTDIR)$(docdir)/saslauthd/
	@$(MAKECOOKIE)

# The names 'client' and 'server' are a little generic, so we change
# them to something more meaningfull
install-sample:
	test -d $(DESTDIR)$(bindir) || ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/sample/.libs/client $(DESTDIR)$(bindir)/sasl-sample-client
	ginstall $(WORKSRC)/sample/.libs/server $(DESTDIR)$(bindir)/sasl-sample-server

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

install-doc:
	mkdir -p $(DESTDIR)$(docdir)/sasl
	cp $(WORKDIR)/README.sasl $(DESTDIR)$(docdir)/sasl/README.CSW
	list='$(DOC_FILES)'; for file in $$list; do \
		$(SED_USR_LOCAL) $(WORKSRC)/doc/$$file > $(DESTDIR)$(docdir)/sasl/$$file; \
	     done
	mkdir -p $(DESTDIR)$(docdir)/saslauthd
	$(SED_USR_LOCAL) $(WORKSRC)/saslauthd/LDAP_SASLAUTHD > $(DESTDIR)$(docdir)/saslauthd/LDAP_SASLAUTHD
	cp $(WORKDIR)/README.saslauthd $(DESTDIR)$(docdir)/saslauthd/README.CSW

fix-path-manpages:
	for f in $(DESTDIR)$(mandir)/*/*.? ; do \
		$(SED_USR_LOCAL) $$f > $$f.tmp ; \
		mv $$f.tmp $$f ; \
	done

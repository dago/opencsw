# Source location
MASTER_SITES = http://www.ibiblio.com/pub/mirrors/apache/httpd/

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += config.layout

ifdef ENABLE_DEPENDENCY_BUILD
DEPEND += lib/libiconv
DEPEND += lib/openssl
DEPEND += lib/openldap
DEPEND += lib/berkeleydb44
DEPEND += lib/sqlite3
DEPEND += lib/expat
DEPEND += server/postgres
DEPEND += server/mysql5
endif

# Build Configuration
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --enable-mods-shared=most
CONFIGURE_ARGS += --enable-authn-alias
CONFIGURE_ARGS += --enable-authnz-ldap
CONFIGURE_ARGS += --enable-file-cache
CONFIGURE_ARGS += --enable-cache
CONFIGURE_ARGS += --enable-disk-cache
CONFIGURE_ARGS += --enable-mem-cache
CONFIGURE_ARGS += --enable-bucketeer
CONFIGURE_ARGS += --enable-charset-lite
CONFIGURE_ARGS += --enable-ldap
CONFIGURE_ARGS += --enable-log-forensic
CONFIGURE_ARGS += --enable-mime-magic
CONFIGURE_ARGS += --enable-cern-meta
CONFIGURE_ARGS += --enable-usertrack
CONFIGURE_ARGS += --enable-unique-id
CONFIGURE_ARGS += --enable-version
CONFIGURE_ARGS += --enable-proxy
CONFIGURE_ARGS += --enable-proxy-connect
CONFIGURE_ARGS += --enable-proxy-ftp
CONFIGURE_ARGS += --enable-proxy-http
CONFIGURE_ARGS += --enable-proxy-ajp
CONFIGURE_ARGS += --enable-proxy-balancer
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --enable-cgid
CONFIGURE_ARGS += --enable-dav-lock

CONFIGURE_ARGS += --with-z=$(prefix)
CONFIGURE_ARGS += --with-ssl=$(prefix)

ifdef USE_EXTERNAL_APR
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-config
CONFIGURE_ARGS += --with-apr-util=$(bindir)/apu-config
else
# APR
#CONFIGURE_ARGS += --enable-threads
#CONFIGURE_ARGS += --enable-other-child

# APR-Util
CONFIGURE_ARGS += --with-ldap
#CONFIGURE_ARGS += --with-ldap-lib=$(libdir)
#CONFIGURE_ARGS += --with-ldap-include=$(includedir)
CONFIGURE_ARGS += --with-dbm=db44
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb44
CONFIGURE_ARGS += --with-pgsql=$(prefix)/postgresql
# This requires apr_dbd_mysql.c to work properly, which is not distributed
# with apr-util, apparently.
#CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql5
CONFIGURE_ARGS += --with-sqlite2=no
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)

# Patch APU to absolutely use GNU iconv
PATCHFILES += apu-iconv.diff

# Patches for global sysvsem from steleman
ifeq ($(GAROSREL),5.10)
USE_NONPORTABLE_ATOMICS = 1
endif
ifeq ($(GAROSREL),5.11)
USE_NONPORTABLE_ATOMICS = 1
endif
ifdef USE_NONPORTABLE_ATOMICS
PATCHFILES += configure.apr.diff
PATCHFILES += apr_atomic.c.diff
CONFIGURE_ARGS += --enable-nonportable-atomics
endif

# Required for bdb44
LIBS = -lnsl
export LIBS

endif

# Extra libpath
EXTRA_LIB = $(prefix)/bdb44/lib $(prefix)/postgresql/lib
EXTRA_INC = $(prefix)/bdb44/include $(prefix)/postgresql/include


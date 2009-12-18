# Source location
MASTER_SITES  = http://www.ibiblio.com/pub/mirrors/apache/httpd/

# MySQL support requires apr_dbd_mysql.c, which is not distributed with
# apr-util due to licensing issues.
#MASTER_SITES += http://apache.webthing.com/svn/apache/apr/
#DISTFILES += apr_dbd_mysql.c

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += config.layout

DEPEND += lib/libiconv
DEPEND += lib/openssl
DEPEND += lib/openldap
DEPEND += lib/berkeleydb44
DEPEND += lib/sqlite3
DEPEND += lib/expat
#DEPEND += server/postgres
#DEPEND += server/mysql5

# Build Configuration
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-rule=SSL_EXPERIMENTAL
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

CONFIGURE_ARGS += --enable-suexec
CONFIGURE_ARGS += --with-suexec-caller=nobody
CONFIGURE_ARGS += --with-suexec-docroot=$(prefix)/apache2/share/htdocs
CONFIGURE_ARGS += --with-suexec-userdir=public_html
CONFIGURE_ARGS += --with-suexec-uidmin=100
CONFIGURE_ARGS += --with-suexec-gidmin=100
CONFIGURE_ARGS += --with-suexec-logfile=$(prefix)/apache2/var/log/suexec_log
CONFIGURE_ARGS += --with-suexec-bin=$(prefix)/apache2/sbin/suexec

ifdef USE_EXTERNAL_APR
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-config
CONFIGURE_ARGS += --with-apr-util=$(bindir)/apu-config
else
# APR
#CONFIGURE_ARGS += --enable-lfs
#CONFIGURE_ARGS += --enable-threads
#CONFIGURE_ARGS += --enable-other-child

# APR-Util
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-dbm=db47
#CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb44
#CONFIGURE_ARGS += --with-pgsql=$(prefix)/postgresql
CONFIGURE_ARGS += --without-sqlite2
CONFIGURE_ARGS += --with-sqlite3=$(prefix)
#CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql5
CONFIGURE_ARGS += --enable-dbd-dso
CONFIGURE_ARGS += --without-odbc
CONFIGURE_ARGS += --without-freetds

# Patch APU to absolutely use GNU iconv
PATCHFILES += apu-iconv.diff

# Patch APR to set _FILE_OFFSET_BITS=64
#PATCHFILES += apr-lfs.diff

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
#LIBS = -lnsl
#export LIBS

endif

# Extra libpath
#EXTRA_LIB += $(prefix)/bdb44/lib
#EXTRA_INC += $(prefix)/bdb44/include

#EXTRA_LIB += $(prefix)/postgresql/lib
#EXTRA_INC += $(prefix)/postgresql/include

#EXTRA_LIB += $(prefix)/mysql5/lib
#EXTRA_INC += $(prefix)/mysql5/include


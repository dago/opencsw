# Source location
MASTER_SITES = http://www.ibiblio.com/pub/mirrors/apache/httpd/

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += config.layout

# Patch mod_ssl to build with OpenSSL 0.9.8
#PATCHFILES += openssl.diff

# Patch APU to absolutely use GNU iconv
PATCHFILES += apu-iconv.diff

# http://issues.apache.org/bugzilla/show_bug.cgi?id=37145
#PATCHFILES += 37145_2.0.x.diff

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

# APR-Util
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-ldap-lib=$(libdir)
CONFIGURE_ARGS += --with-ldap-include=$(includedir)
CONFIGURE_ARGS += --with-dbm=db43
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb43
CONFIGURE_ARGS += --with-pgsql=$(prefix)/postgresql
CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql4
CONFIGURE_ARGS += --with-sqlite2=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)

# Extra libpath
EXTRA_LIB = $(prefix)/bdb43/lib
EXTRA_INC = $(prefix)/bdb43/include


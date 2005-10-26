# Source location
MASTER_SITES = http://www.ibiblio.com/pub/mirrors/apache/httpd/

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += config.layout

# Patch mod_ssl to build with OpenSSL 0.9.8
PATCHFILES += openssl.diff

# Patch configure to use SUNWpl5u
PATCHFILES += perl.diff

# Build Configuration
CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS  = --enable-layout=csw
CONFIGURE_ARGS += --enable-mods-shared=all
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb43
CONFIGURE_ARGS += --with-dbm=db43
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --with-ldap-lib=$(libdir)
CONFIGURE_ARGS += --with-ldap-include=$(includedir)
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-iconv=$(prefix)
CONFIGURE_ARGS += --with-z=$(prefix)
CONFIGURE_ARGS += --enable-deflate
CONFIGURE_ARGS += --enable-proxy
CONFIGURE_ARGS += --enable-proxy-connect
CONFIGURE_ARGS += --enable-proxy-http
CONFIGURE_ARGS += --enable-proxy-ftp
CONFIGURE_ARGS += --enable-cgid
CONFIGURE_ARGS += --enable-cgi
CONFIGURE_ARGS += --enable-ldap
CONFIGURE_ARGS += --enable-auth-ldap
CONFIGURE_ARGS += --enable-cache
CONFIGURE_ARGS += --enable-disk-cache
CONFIGURE_ARGS += --enable-mem-cache

EXTRA_LIB = $(prefix)/bdb43/lib
EXTRA_INC = $(prefix)/bdb43/include


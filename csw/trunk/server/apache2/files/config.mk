MASTER_SITES = http://www.ibiblio.com/pub/mirrors/apache/httpd/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += config.layout

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
CONFIGURE_ARGS += --with-perl=/usr/bin/perl
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


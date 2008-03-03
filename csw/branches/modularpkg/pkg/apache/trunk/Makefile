GARNAME = apache
GARVERSION = 1.3.36
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the best
  around in terms of functionality, efficiency, security and speed.
endef

MASTER_SITES = http://www.ibiblio.org/pub/mirrors/apache/httpd/
DISTFILES = $(GARNAME)_$(GARVERSION).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(prefix)
CONFIGURE_ARGS += --with-apr-util=$(prefix)
CONFIGURE_ARGS += --enable-mods-shared=all
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --with-mpm=worker
CONFIGURE_ARGS += --enable-deflate
CONFIGURE_ARGS += --enable-proxy
CONFIGURE_ARGS += --enable-proxy-connect
CONFIGURE_ARGS += --enable-proxy-http
CONFIGURE_ARGS += --enable-proxy-ftp
CONFIGURE_ARGS += --disable-cgid
CONFIGURE_ARGS += --enable-cgi
CONFIGURE_ARGS += --with-ldap
CONFIGURE_ARGS += --enable-ldap
CONFIGURE_ARGS += --enable-auth-ldap
CONFIGURE_ARGS += --enable-cache
CONFIGURE_ARGS += --enable-disk-cache
CONFIGURE_ARGS += --enable-mem-cache
CONFIGURE_ARGS += --disable-ipv6
CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb4
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-expat=$(prefix)

include gar/category.mk

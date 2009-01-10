GARNAME = nginx
GARVERSION = 0.7.30
CATEGORIES = server

DESCRIPTION = HTTP server and mail proxy server
define BLURB
  Nginx (pronounced "engine x") is a free, open-source, high-performance
  HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
endef

MASTER_SITES = http://sysoev.ru/nginx/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnginx,)
DISTFILES += cswnginx.xml svc-cswnginx

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWosslrt CSWpcre  CSWzlib

GARCOMPILER = GNU

#CONFIGURE_ARGS += --with-cpu-opt=pentiumpro
CONFIGURE_ARGS += --prefix=$(prefix)/var/nginx
CONFIGURE_ARGS += --conf-path=$(sysconfdir)/nginx/nginx.conf
CONFIGURE_ARGS += --sbin-path=$(sbindir)/nginx
CONFIGURE_ARGS += --lock-path=$(prefix)/var/run/nginx/nginx.lock
CONFIGURE_ARGS += --pid-path=$(prefix)/var/run/nginx/nginx.pid
CONFIGURE_ARGS += --http-client-body-temp-path=$(prefix)/var/spool/nginx/client
CONFIGURE_ARGS += --http-fastcgi-temp-path=$(prefix)/var/spool/nginx/fastcgi
CONFIGURE_ARGS += --http-proxy-temp-path=$(prefix)/var/spool/nginx/proxy
CONFIGURE_ARGS += --error-log-path=$(prefix)/var/log/nginx/error.log
CONFIGURE_ARGS += --http-log-path=$(prefix)/var/log/nginx/access.log
CONFIGURE_ARGS += --with-cc-opt="-I/opt/csw/include/openssl"
CONFIGURE_ARGS += --with-ld-opt="-L/opt/csw/lib"
CONFIGURE_ARGS += --with-md5=YES
CONFIGURE_ARGS += --with-sha1=YES
CONFIGURE_ARGS += --with-http_ssl_module
CONFIGURE_ARGS += --with-http_realip_module
CONFIGURE_ARGS += --with-http_dav_module
CONFIGURE_ARGS += --with-http_flv_module
CONFIGURE_ARGS += --with-http_stub_status_module

TEST_SCRIPTS =

PROTOTYPE_FILTER = awk '$$$$3 ~ /\/var\/log$$$$/ { $$$$6 = "sys" } { print }'
#PROTOTYPE_FILTER = awk '$$$$3 ~ /\/var\/spool\/nginx\/(client|fastcgi|proxy)$/ { $$$$4 = "700" } { print }'

include gar/category.mk


NGINXDOC = CHANGES CHANGES.ru LICENSE README

post-install:
	cp $(WORKDIR)/svc-cswnginx $(WORKDIR)/cswnginx
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(sharedstatedir)/nginx/contrib
	ginstall -d $(DESTDIR)$(docdir)/nginx
	ginstall -d $(DESTDIR)$(prefix)/sbin
	ginstall -d $(DESTDIR)$(prefix)/var/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/nginx/sites
	ginstall -d $(DESTDIR)$(prefix)/var/log/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/client
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/fastcgi
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/proxy
	cd $(WORKSRC); \
	cp -r contrib/* $(DESTDIR)$(sharedstatedir)/nginx/contrib; \
	cp $(NGINXDOC)  $(DESTDIR)$(docdir)/nginx; \
	$(MAKECOOKIE)

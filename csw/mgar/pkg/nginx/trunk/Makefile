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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWpcre CSWosslrt CSWzlib

CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --conf-path=etc/nginx/nginx.conf
CONFIGURE_ARGS += --sbin-path=sbin/nginx
CONFIGURE_ARGS += --lock-path=var/run/nginx/nginx.lock
CONFIGURE_ARGS += --pid-path=var/run/nginx/nginx.pid
CONFIGURE_ARGS += --http-client-body-temp-path=var/spool/nginx/client
CONFIGURE_ARGS += --http-fastcgi-temp-path=var/spool/nginx/fastcgi
CONFIGURE_ARGS += --http-proxy-temp-path=var/spool/nginx/proxy
CONFIGURE_ARGS += --error-log-path=var/log/nginx/error.log
CONFIGURE_ARGS += --http-log-path=var/log/nginx/access.log
CONFIGURE_ARGS += --with-cc-opt="-I/opt/csw/include/openssl"
CONFIGURE_ARGS += --with-ld-opt="-L/opt/csw/lib"
CONFIGURE_ARGS += --with-md5=YES
CONFIGURE_ARGS += --with-sha1=YES
CONFIGURE_ARGS += --with-http_ssl_module
CONFIGURE_ARGS += --with-http_realip_module
CONFIGURE_ARGS += --with-http_dav_module
CONFIGURE_ARGS += --with-http_flv_module
CONFIGURE_ARGS += --with-http_stub_status_module

include gar/category.mk

# No test suite
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

NGINXDOC=CHANGES CHANGES.ru LICENSE README

install-custom:
	ginstall -d $(DESTDIR)$(prefix)/etc
	ginstall -d $(DESTDIR)$(prefix)/sbin
	ginstall -d $(DESTDIR)$(prefix)/var/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/nginx/html
	ginstall -d $(DESTDIR)$(prefix)/var/nginx/sites
	ginstall -d $(DESTDIR)$(prefix)/var/log/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/client
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/fastcgi
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/proxy
	ginstall -d $(DESTDIR)$(prefix)/share/doc/nginx
	cd $(WORKSRC); \
	cp objs/nginx $(DESTDIR)$(prefix)/sbin; \
	cp html/* $(DESTDIR)$(prefix)/var/nginx/html; \
	cp conf/* $(DESTDIR)$(prefix)/etc; \
	cp conf/fastcgi_params $(DESTDIR)$(prefix)/etc/fastcgi_params.default; \
	cp conf/mime.types     $(DESTDIR)$(prefix)/etc/mime.types.default; \
	cp conf/nginx.conf     $(DESTDIR)$(prefix)/etc/nginx.conf.default; \
	cp $(NGINXDOC) $(DESTDIR)$(prefix)/share/doc/nginx; \
	$(MAKECOOKIE)


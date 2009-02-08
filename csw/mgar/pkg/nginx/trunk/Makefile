GARNAME = nginx
GARVERSION = 0.7.30
CATEGORIES = server

DESCRIPTION = nginx HTTP server and mail proxy server
define BLURB
  Nginx (pronounced "engine x") is a free, open-source, high-performance
  HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
endef

MASTER_SITES = http://sysoev.ru/nginx/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnginx,checkinstall postinstall preremove)
DISTFILES += cswnginx.xml svc-cswnginx

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWosslrt CSWpcrert  CSWzlib

EXTRA_BUILD_ISAS_i386  = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv9

ifeq ($(ISA),pentium_pro)
	NGINXCPU = pentiumpro
else
ifeq ($(ISA),sparcv8)
	NGINXCPU = sparc32
else
ifeq ($(ISA),sparcv9)
	NGINXCPU = sparc64
else
	NGINXCPU = $(ISA)
endif
endif
endif

CFLAGS =

CONFIGURE_ARGS += --with-cpu-opt=$(NGINXCPU)
CONFIGURE_ARGS += --with-cc-opt="-I$(includedir) -I$(includedir)/openssl"
CONFIGURE_ARGS += --with-ld-opt="$(LDFLAGS)"
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
CONFIGURE_ARGS += --with-md5=YES
CONFIGURE_ARGS += --with-sha1=YES
CONFIGURE_ARGS += --with-http_ssl_module
CONFIGURE_ARGS += --with-http_realip_module
CONFIGURE_ARGS += --with-http_dav_module
CONFIGURE_ARGS += --with-http_flv_module
CONFIGURE_ARGS += --with-http_stub_status_module

TEST_SCRIPTS =

PROTOTYPE_FILTER = awk '$$$$3 ~ /\/var\/((log|run)|(svc|(svc\/(manifest|manifest\/site))))$$$$/ { $$$$6 = "sys" } $$$$3 ~ /\/var\/spool\/nginx\/(client|fastcgi|proxy)$$$$/ { $$$$4 = "700" } { print }'

include gar/category.mk

NGINXDOCS = CHANGES CHANGES.ru LICENSE README

post-configure-modulated:
	gsed -i s#/...ISALIST#/'$$ISALIST'# $(WORKSRC)/objs/ngx_auto_config.h
	$(MAKECOOKIE)

post-install-modulated:
	cp $(WORKDIR)/svc-cswnginx $(WORKDIR)/cswnginx
	ginstall -d $(DESTDIR)$(sysconfdir)/nginx/conf.d
	ginstall -d $(DESTDIR)$(sharedstatedir)/nginx/contrib
	ginstall -d $(DESTDIR)$(docdir)/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/log/nginx
	ginstall -d $(DESTDIR)$(prefix)/var/nginx/sites
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/client
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/fastcgi
	ginstall -d $(DESTDIR)$(prefix)/var/spool/nginx/proxy
	mv $(DESTDIR)$(sysconfdir)/nginx/fastcgi_params $(DESTDIR)$(sysconfdir)/nginx/fastcgi_params.CSW
	mv $(DESTDIR)$(sysconfdir)/nginx/mime.types $(DESTDIR)$(sysconfdir)/nginx/mime.types.CSW
	mv $(DESTDIR)$(sysconfdir)/nginx/nginx.conf $(DESTDIR)$(sysconfdir)/nginx/nginx.conf.CSW
	cd $(WORKSRC); \
	cp -r contrib/* $(DESTDIR)$(sharedstatedir)/nginx/contrib; \
	cp $(NGINXDOCS) $(DESTDIR)$(docdir)/nginx
	$(MAKECOOKIE)

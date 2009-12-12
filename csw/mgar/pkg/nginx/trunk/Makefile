GARNAME = nginx
GARVERSION = 0.7.64
CATEGORIES = server

DESCRIPTION = HTTP server and mail proxy server
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

REQUIRED_PKGS = CSWosslrt CSWpcrert CSWzlib

PACKAGING_PLATFORMS  = solaris8-sparc  solaris8-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

#EXTRA_BUILD_ISAS_i386  = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv9

NGINXCPU_pentium_pro = pentiumpro
NGINXCPU_sparcv8 = sparc32
NGINXCPU_sparcv9 = sparc64
NGINXCPU_$(ISA) ?= $(ISA)
NGINXCPU = $(NGINXCPU_$(ISA))

CFLAGS =

sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

CONFIGURE_ARGS += --with-cpu-opt=$(NGINXCPU)
CONFIGURE_ARGS += --with-cc-opt="-I$(includedir) -I$(includedir)/openssl"
CONFIGURE_ARGS += --with-ld-opt="$(LDFLAGS)"
CONFIGURE_ARGS += --lock-path=/var/run/nginx/nginx.lock
CONFIGURE_ARGS += --pid-path=/var/run/nginx/nginx.pid
CONFIGURE_ARGS += --conf-path=$(sysconfdir)/nginx/nginx.conf
CONFIGURE_ARGS += --sbin-path=$(sbindir)/nginx
CONFIGURE_ARGS += --prefix=$(localstatedir)/nginx
CONFIGURE_ARGS += --http-client-body-temp-path=$(localstatedir)/nginx/client
CONFIGURE_ARGS += --http-fastcgi-temp-path=$(localstatedir)/nginx/fastcgi
CONFIGURE_ARGS += --http-proxy-temp-path=$(localstatedir)/nginx/proxy
CONFIGURE_ARGS += --error-log-path=$(localstatedir)/nginx/logs/error.log
CONFIGURE_ARGS += --http-log-path=$(localstatedir)/nginx/logs/access.log
CONFIGURE_ARGS += --with-md5=YES
CONFIGURE_ARGS += --with-sha1=YES
CONFIGURE_ARGS += --with-http_ssl_module
CONFIGURE_ARGS += --with-http_realip_module
CONFIGURE_ARGS += --with-http_dav_module
CONFIGURE_ARGS += --with-http_flv_module
CONFIGURE_ARGS += --with-http_stub_status_module

TEST_SCRIPTS =

#PROTOTYPE_FILTER = awk '$$$$3 ~ /\/var\/((log|run)|(svc|(svc\/(manifest|manifest\/site))))$$$$/ { $$$$6 = "sys" } $$$$3 ~ /\/var\/nginx\/(client|fastcgi|proxy)$$$$/ { $$$$4 = "700" } { print }'

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
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/client
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/fastcgi
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/logs
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/proxy
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/sites
	mv $(DESTDIR)$(sysconfdir)/nginx/fastcgi_params $(DESTDIR)$(sysconfdir)/nginx/fastcgi_params.CSW
	mv $(DESTDIR)$(sysconfdir)/nginx/mime.types $(DESTDIR)$(sysconfdir)/nginx/mime.types.CSW
	mv $(DESTDIR)$(sysconfdir)/nginx/nginx.conf $(DESTDIR)$(sysconfdir)/nginx/nginx.conf.CSW
	cd $(WORKSRC); \
	cp -r contrib/* $(DESTDIR)$(sharedstatedir)/nginx/contrib; \
	cp $(NGINXDOCS) $(DESTDIR)$(docdir)/nginx
	$(MAKECOOKIE)

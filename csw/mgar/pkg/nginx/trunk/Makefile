NAME       = nginx
VERSION    = 1.1.4
CATEGORIES = server

GARCOMPILER = SOS11

DESCRIPTION = HTTP server and mail proxy server
define BLURB
  Nginx (pronounced "engine x") is a free, open-source, high-performance
  HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
endef

MASTER_SITES = http://nginx.org/download/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
DISTFILES   += cswnginx

LICENSE      = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

BUILD_DEP_PKGS = CSWlibz-dev
RUNTIME_DEP_PKGS = CSWosslrt CSWlibpcre0 CSWlibz1 CSWperl

PACKAGING_PLATFORMS  = solaris9-sparc  solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# default sparc arch is set to sparcv8plus because nginx contains
# assembler parts specific to v8plus and v9 arches:
#	.inline ngx_casa,0
#	casa    [%o2] 0x80, %o1, %o0
#	.end
#
#	.inline ngx_casxa,0
#	casxa   [%o2] 0x80, %o1, %o0
#	.end

ISA_DEFAULT_sparc      = sparcv8plus
EXTRA_BUILD_ISAS_i386  = pentium_pro amd64
EXTRA_BUILD_ISAS_sparc = sparcv9

NGINXCPU_i386          = pentium
NGINXCPU_pentium_pro   = pentium3
NGINXCPU_sparcv8plus   = sparc32
NGINXCPU_sparcv9       = sparc64
NGINXCPU_$(ISA)       ?= $(ISA)
NGINXCPU               = $(NGINXCPU_$(ISA))

CFLAGS =

sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

#CONFIGURE_ARGS += --with-debug
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
CONFIGURE_ARGS += --http-scgi-temp-path=$(localstatedir)/nginx/scgi
CONFIGURE_ARGS += --http-uwsgi-temp-path=$(localstatedir)/nginx/uwsgi
CONFIGURE_ARGS += --http-proxy-temp-path=$(localstatedir)/nginx/proxy
CONFIGURE_ARGS += --error-log-path=$(localstatedir)/nginx/logs/error.log
CONFIGURE_ARGS += --http-log-path=$(localstatedir)/nginx/logs/access.log
CONFIGURE_ARGS += --with-ipv6
CONFIGURE_ARGS += --with-http_addition_module
CONFIGURE_ARGS += --with-http_dav_module
CONFIGURE_ARGS += --with-http_flv_module
CONFIGURE_ARGS += --with-http_realip_module
CONFIGURE_ARGS += --with-http_secure_link_module
CONFIGURE_ARGS += --with-http_ssl_module
CONFIGURE_ARGS += --with-http_stub_status_module

TEST_SCRIPTS =

INITSMF      = $(sysconfdir)/init.d/cswnginx
PRESERVECONF = $(sysconfdir)/nginx/fastcgi.conf $(sysconfdir)/nginx/fastcgi_params $(sysconfdir)/nginx/mime.types $(sysconfdir)/nginx/nginx.conf $(sysconfdir)/nginx/scgi_params $(sysconfdir)/nginx/uwsgi_params $(localstatedir)/nginx/html/50x.html $(localstatedir)/nginx/html/index.html

NGINXDOCS    = CHANGES CHANGES.ru LICENSE README


include gar/category.mk

post-configure-modulated:
	gsed -i  s#/...ISALIST#/'$$ISALIST'# $(WORKSRC)/objs/ngx_auto_config.h
	gsed -i 's#  pause#  rep; nop#'      $(WORKSRC)/src/os/unix/ngx_sunpro_amd64.il
	$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(sysconfdir)/nginx/conf.d
	ginstall -d $(DESTDIR)$(sharedstatedir)/nginx/contrib
	ginstall -d $(DESTDIR)$(docdir)/nginx
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/client
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/fastcgi
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/logs
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/proxy
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/scgi
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/sites
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/uwsgi
	cp $(WORKDIR)/cswnginx $(DESTDIR)$(sysconfdir)/init.d/
	cd $(WORKSRC); \
	cp -r contrib/* $(DESTDIR)$(sharedstatedir)/nginx/contrib; \
	cp $(NGINXDOCS) $(DESTDIR)$(docdir)/nginx
	rm -rf $(DESTDIR)/var/run/nginx
	$(MAKECOOKIE)

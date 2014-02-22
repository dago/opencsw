NAME = mod_proxy_html
VERSION = 3.1.2
CATEGORIES = server

DESCRIPTION = Apache 2 output filter to rewrite HTML links
define BLURB
	mod_proxy_html is an output filter to rewrite HTML 
	links in a proxy situation, to ensure that links work 
	for users outside the proxy. It serves the same purpose 
	as Apache's ProxyPassReverse directive does for HTTP 
	headers, and is an essential component of a reverse proxy.
endef

MASTER_SITES = http://apache.webthing.com/NAME = $(NAME)
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = http://apache.webthing.com/mod_proxy_html/

BUILD_DEP_PKGS += CSWapache2-dev
BUILD_DEP_PKGS += CSWlibxml2-dev

PACKAGES += CSWap2-mod-proxy-html
SPKG_DESC_CSWap2-mod-proxy-html = Apache 2 output filter to rewrite HTML links
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWap2-mod-proxy-html += CSWapache2

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(AP2_ROOT)/libexec
AP2_EXTRACONF = $(AP2_ROOT)/etc/extra
AP2_SBIN      = $(AP2_ROOT)/sbin
APXS          = $(AP2_SBIN)/apxsWORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALPRESERVECONF += $(AP2_EXTRACONF)/proxy_html.conf

include gar/category.mk

build-custom:
	cd $(WORKSRC) && $(APXS) -I. -I$(includedir)/libxml2 -c mod_proxy_html.c
	cd $(WORKSRC) && $(APXS) -I. -I$(includedir)/libxml2 -c mod_xml2enc.c
	@$(MAKECOOKIE)

install-custom:
	mkdir -p $(DESTDIR)$(AP2_LIBEXEC)
	cd $(WORKSRC) && $(APXS) -S LIBEXECDIR=$(DESTDIR)$(AP2_LIBEXEC) -i mod_proxy_html.la
	cd $(WORKSRC) && $(APXS) -S LIBEXECDIR=$(DESTDIR)$(AP2_LIBEXEC) -i mod_xml2enc.la
	ginstall -d $(DESTDIR)$(AP2_EXTRACONF)
	ginstall -m 0644 $(WORKSRC)/proxy_html.conf $(DESTDIR)$(AP2_EXTRACONF)/proxy_html.conf
	ginstall -d $(DESTDIR)$(docdir)/ap2_mod_proxy_html
	ginstall -m 0644 $(WORKSRC)/README $(DESTDIR)$(docdir)/ap2_mod_proxy_html/README
	@$(MAKECOOKIE)

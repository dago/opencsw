GARNAME = mod_proxy_html
GARVERSION = 2.5.2
CATEGORIES = server

DESCRIPTION = Apache 2 output filter to rewrite HTML links
define BLURB
	mod_proxy_html is an output filter to rewrite HTML 
	links in a proxy situation, to ensure that links work 
	for users outside the proxy. It serves the same purpose 
	as Apache's ProxyPassReverse directive does for HTTP 
	headers, and is an essential component of a reverse proxy.
endef

MASTER_SITES = http://apache.webthing.com/mod_proxy_html/
DISTFILES  = $(GARNAME)-$(GARVERSION).c
DISTFILES += $(call admfiles,CSWap2modproxyhtml,depend)

PREREQUISITE_PKGS = CSWapache2-devel CSWapache2 CSWlibxml2

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	$(prefix)/apache2/sbin/apxs -c -I$(includedir)/libxml2/ $(WORKSRC)/mod_proxy_html-2.5.2.c
	@$(MAKECOOKIE)

install-custom:
	@-mkdir -p $(DESTDIR)$(prefix)/apache2/libexec
	cp $(WORKSRC)/.libs/mod_proxy_html-2.5.2.so $(DESTDIR)$(prefix)/apache2/libexec
	@$(MAKECOOKIE)

GARNAME = ap2_modgeoip
SPKG_NAME = mod_geoip
GARVERSION = 1.2.5
CATEGORIES = server

DESCRIPTION = Apache 2.x GeoIP module
define BLURB
  mod_geoip2 is an Apache 2.x module for finding the country and city
  that a web request originated from.  It uses the GeoIP library and
  database to perform the lookup.  It is free software, licensed under
  the Apache license.  It requires the C API, version 1.4.3 and above, see:
  http://www.maxmind.com/app/c
endef

MASTER_SITES = http://www.maxmind.com/download/geoip/api/mod_geoip2/
DISTFILES  = $(SPKG_NAME)2_$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWap2modgeoip,depend postinstall preremove)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk
include ../apache2/files/extensionbuild.mk

WORKSRC := $(WORKDIR)/$(SPKG_NAME)2_$(GARVERSION)
SPKG_SOURCEURL = http://www.maxmind.com/app/mod_geoip/

build-custom:
	@( cd $(WORKSRC) ; $(APXS2_BUILD) -L$(libdir) -Wl,"-R $(libdir)" -lGeoIP $(SPKG_NAME).c )
	@$(MAKECOOKIE)

install-custom:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@( cd $(WORKSRC) ; \
		$(APXS2_INSTALL) $(SPKG_NAME).la ; \
		cp Changes README* INSTALL $(DESTDIR)$(docdir)/$(GARNAME) )
	@cp $(FILEDIR)/CSWap2modgeoip.copyright $(DESTDIR)$(docdir)/$(GARNAME)/copyright
	@$(MAKECOOKIE)

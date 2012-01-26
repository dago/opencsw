NAME = geolitedb
VERSION = 110201
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Geolite country database

MASTER_SITES = http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/
DISTFILES  = GeoIP.dat.gz
DISTFILES += COPYING

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://www.maxmind.com/app/geolitecountry

install-custom:
	@echo " ==> Installing $(NAME)"
	@ginstall -d $(DESTDIR)/opt/csw/share/GeoIP
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/geolitedb
	@cp -r $(WORKSRC)/GeoIP.dat $(DESTDIR)/opt/csw/share/GeoIP/
	@$(MAKECOOKIE)

NAME = geolitedb
VERSION = 20120403
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Geolite country database

MASTER_SITES += http://geolite.maxmind.com/download/geoip/database/
MASTER_SITES += http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/
MASTER_SITES += http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/
DISTFILES += GeoIP.dat.gzIPv6ISTFILES += GeoIP.dat.gz
DISTFILES += GeoLiteCity.dat.xz
DISTFILES += GeoLiteCityv6.dat.gz
DISTFILES += COPYING

VENDOR_URL = http://www.maxmind.com/app/geolitecountry

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME)"
	ginstall -d $(DESTDIR)/opt/csw/share/GeoIP
	ginstall $(WORKDIR)/GeoIP.dat $(DESTDIR)/opt/csw/share/GeoIP/GeoIP.dat
	ginstaIPv6.dat $(DESTDIR)/opt/csw/share/GeoIP/GeoIPv6share/GeoIP/GeoIP.dat
	ginstall $(WORKDIR)/GeoLiteCity.dat $(DESTDIR)/opt/csw/share/GeoIP/GeoIPCity.dat
	ginstall $(WORKDIR)/GeoLiteCityv6.dat $(DESTDIR)/opt/csw/share/GeoIP/GeoIPCityv6.dat
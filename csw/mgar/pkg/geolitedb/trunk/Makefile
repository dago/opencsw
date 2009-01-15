GARNAME = geolitedb
GARVERSION = 090102
CATEGORIES = net

DESCRIPTION = geolite country database

MASTER_SITES = http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/
DISTFILES  = GeoIP.dat.gz
DISTFILES += $(call admfiles,CSWgeolitedb)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://www.maxmind.com/app/geolitecountry/

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@ginstall -d $(DESTDIR)/opt/csw/share/GeoIP
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/geolitedb
	@cp -r $(WORKSRC)/GeoIP.dat $(DESTDIR)/opt/csw/share/GeoIP/
	@cp -r $(FILEDIR)/CSWgeolitedb.copyright $(DESTDIR)/opt/csw/share/doc/geolitedb/LICENSE
	@$(MAKECOOKIE)

GARNAME = geolitedb
GARVERSION = 080901
CATEGORIES = net

DESCRIPTION = geolite country database

MASTER_SITES = http://www.maxmind.com/download/geoip/database/
DISTFILES  = GeoIP.dat.gz
DISTFILES += $(call admfiles,CSWgeolitedb)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://www.maxmind.com/download/geoip/database/

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@ginstall -d $(DESTDIR)/opt/csw/share/GeoIP
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/geolitedb
	@cp -r $(WORKSRC)/GeoIP.dat $(DESTDIR)/opt/csw/share/GeoIP/
	@cp -r $(FILEDIR)/CSWgeolitedb.copyright $(DESTDIR)/opt/csw/share/doc/geolitedb/copyright
	@$(MAKECOOKIE)

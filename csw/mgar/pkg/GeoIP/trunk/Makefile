GARNAME = GeoIP
GARVERSION = 1.4.6
CATEGORIES = net

DESCRIPTION = GeoIP C API
define BLURB
  GeoIP C API
endef

MASTER_SITES = http://geolite.maxmind.com/download/geoip/api/c/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWgeoip CSWgeoipdevel
REQUIRED_PKGS_CSWgeoip = CSWgeolitedb CSWzlib
REQUIRED_PKGS_CSWgeoipdevel = CSWgeoip
CATALOGNAME_CSWgeoip = geoip
CATALOGNAME_CSWgeoipdevel = geoip_devel

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure-modulated:
	@echo " ==> Pre-configure for $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   sed 's/-Wall//' Makefile.am > tmp.sed ; \
	   mv tmp.sed Makefile.am ; \
	   sed 's/-Wall//' Makefile.in > tmp.sed ; \
	   mv tmp.sed Makefile.in ; \
	   cd apps ; \
	   sed 's/-Wall//' Makefile.am > tmp.sed ; \
	   mv tmp.sed Makefile.am ; \
	   sed 's/-Wall//' Makefile.in > tmp.sed ; \
	   mv tmp.sed Makefile.in ; \
	   cd ../libGeoIP ; \
	   sed 's/-Wall//' Makefile.am > tmp.sed ; \
	   mv tmp.sed Makefile.am ; \
	   sed 's/-Wall//' Makefile.in > tmp.sed ; \
	   mv tmp.sed Makefile.in ; \
	   cd ../test ; \
	   sed 's/-Wall//' Makefile.am > tmp.sed ; \
	   mv tmp.sed Makefile.am ; \
	   sed 's/-Wall//' Makefile.in > tmp.sed ; \
	   mv tmp.sed Makefile.in )
	@$(MAKECOOKIE)

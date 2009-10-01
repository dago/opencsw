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
REQUIRED_PKGS_CSWgeoip = CSWgeolitedb CSWzlib CSWgcc3corert
REQUIRED_PKGS_CSWgeoipdevel = CSWgeoip
CATALOGNAME_CSWgeoip = geoip
CATALOGNAME_CSWgeoipdevel = geoip_devel
SPKG_DESC_CSWgeoip = $(DESCRIPTION)
SPKG_DESC_CSWgeoipdevel = GeoIP C API development support

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GCC4
TEST_TARGET = check

PKGFILES_CSWgeoipdevel = $(PKGFILES_DEVEL)

EXTRA_MERGE_EXCLUDE_FILES = .*GeoIP.dat$

# Do not exclude static libs (needed for devel package)
MERGE_EXCLUDE_STATICLIBS =

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw

include gar/category.mk

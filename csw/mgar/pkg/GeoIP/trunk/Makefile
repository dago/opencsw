NAME = GeoIP
VERSION = 1.4.6
CATEGORIES = net

DESCRIPTION = GeoIP C API
define BLURB
  GeoIP C API
endef

MASTER_SITES = http://geolite.maxmind.com/download/geoip/api/c/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
VENDOR_URL = http://www.maxmind.com/app/api

PACKAGES                 += CSWgeoip
CATALOGNAME_CSWgeoip      = geoip
SPKG_DESC_CSWgeoip        = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgeoip = CSWgeolitedb CSWzlib CSWgcc4corert

PACKAGES                     += CSWgeoip-dev
CATALOGNAME_CSWgeoip-dev      = geoip_dev
SPKG_DESC_CSWgeoip-dev        = GeoIP C API development support
RUNTIME_DEP_PKGS_CSWgeoip-dev = CSWgeoip

GARCOMPILER = GCC4
TEST_TARGET = check

PKGFILES_CSWgeoip-dev = $(PKGFILES_DEVEL)

EXTRA_MERGE_EXCLUDE_FILES = .*GeoIP.dat$

# Do not exclude static libs (needed for devel package)
MERGE_EXCLUDE_STATICLIBS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw

CHECKPKG_OVERRIDES_CSWgeoip += non-uniform-lib-versions-in-package|sonames=libGeoIP.so.1,libGeoIPUpdate.so.0
CHECKPKG_OVERRIDES_CSWgeoip += surplus-dependency|CSWgeolitedb
CHECKPKG_OVERRIDES_CSWgeoip-dev += discouraged-path-in-pkgmap|/opt/csw/lib/libGeoIP.a
CHECKPKG_OVERRIDES_CSWgeoip-dev += discouraged-path-in-pkgmap|/opt/csw/lib/libGeoIPUpdate.a
# Dev package renamed, remove next time
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/include/GeoIPCity.h|CSWgeoip-dev|CSWgeoipdevel
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/include/GeoIP.h|CSWgeoip-dev|CSWgeoipdevel
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/lib/libGeoIPUpdate.a|CSWgeoip-dev|CSWgeoipdevel
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/include/GeoIPUpdate.h|CSWgeoip-dev|CSWgeoipdevel
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/lib/libGeoIP.a|CSWgeoip-dev|CSWgeoipdevel

include gar/category.mk

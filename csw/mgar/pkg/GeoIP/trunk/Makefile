NAME = GeoIP
VERSION = 1.4.7
CATEGORIES = net

DESCRIPTION = GeoIP C API
define BLURB
  GeoIP C API
endef

MASTER_SITES = http://geolite.maxmind.com/download/geoip/api/c/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
VENDOR_URL = http://www.maxmind.com/app/c

PACKAGES                 += CSWgeoip
CATALOGNAME_CSWgeoip      = geoip
SPKG_DESC_CSWgeoip        = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgeoip = CSWgeolitedb CSWzlib CSWgcc4corert

PACKAGES                     += CSWgeoip-dev
CATALOGNAME_CSWgeoip-dev      = geoip_dev
SPKG_DESC_CSWgeoip-dev        = GeoIP C API development support
RUNTIME_DEP_PKGS_CSWgeoip-dev = CSWgeoip
PKGFILES_CSWgeoip-dev         = $(PKGFILES_DEVEL)

GARCOMPILER = GCC4

#TEST_TARGET = check
TEST_TARGET =

EXTRA_MERGE_EXCLUDE_FILES = .*GeoIP.dat$

# Do not exclude static libs (needed for devel package)
#MERGE_EXCLUDE_STATICLIBS =

BUILD64 = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --disable-static

CHECKPKG_OVERRIDES_CSWgeoip += non-uniform-lib-versions-in-package|sonames=libGeoIP.so.1,libGeoIPUpdate.so.0
CHECKPKG_OVERRIDES_CSWgeoip += surplus-dependency|CSWgeolitedb

# Dev package renamed, remove next time
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/include/GeoIPCity.h|CSWgeoip-dev|CSWgeoipdevel
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/include/GeoIP.h|CSWgeoip-dev|CSWgeoipdevel
CHECKPKG_OVERRIDES_CSWgeoip-dev += file-collision|/opt/csw/include/GeoIPUpdate.h|CSWgeoip-dev|CSWgeoipdevel

include gar/category.mk

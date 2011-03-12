NAME = GeoIP
VERSION = 1.4.6
CATEGORIES = net

DESCRIPTION = GeoIP C API
define BLURB
  GeoIP C API
endef

MASTER_SITES = http://geolite.maxmind.com/download/geoip/api/c/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWgeoip
CATALOGNAME_CSWgeoip = geoip
SPKG_DESC_CSWgeoip = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgeoip = CSWgeolitedb CSWzlib CSWgcc3corert

PACKAGES += CSWgeoip-dev
CATALOGNAME_CSWgeoip-dev = geoip_dev
SPKG_DESC_CSWgeoip-dev = GeoIP C API development support
RUNTIME_DEP_PKGS_CSWgeoip-dev = CSWgeoip

GARCOMPILER = GCC4
TEST_TARGET = check

PKGFILES_CSWgeoip-dev = $(PKGFILES_DEVEL)

EXTRA_MERGE_EXCLUDE_FILES = .*GeoIP.dat$

# Do not exclude static libs (needed for devel package)
MERGE_EXCLUDE_STATICLIBS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw

include gar/category.mk

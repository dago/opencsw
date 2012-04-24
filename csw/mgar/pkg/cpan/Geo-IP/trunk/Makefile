NAME = Geo-IP
VERSION = 1.40
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BORISZ

DESCRIPTION = Maxmind GeoIP native C bindings
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = README

PACKAGES += CSWpm-geo-ip
SPKG_DESC_CSWpm-geo-ip = Maxmind GeoIP native C bindings
RUNTIME_DEP_PKGS_CSWpm-geo-ip += CSWlibgeoip1

# Adjust location of GeoIP database
REINPLACEMENTS += geoip
REINPLACE_MATCH_geoip = /usr/local/share/GeoIP
REINPLACE_WITH_geoip = $(sharedstatedir)/GeoIP
REINPLACE_FILES_geoip += lib/Geo/IP/Record.pod
REINPLACE_FILES_geoip += lib/Geo/IP.pm

include gar/category.mk

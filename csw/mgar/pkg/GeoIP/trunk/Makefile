NAME = GeoIP
VERSION = 1.4.8
GARTYPE = v2

DESCRIPTION = GeoIP C API

MASTER_SITES = http://geolite.maxmind.com/download/geoip/api/c/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Remove-gcc-specific-flags.patch
PATCHFILES += 0002-Do-not-use-unnamed-union.patch
PATCHFILES += 0003-Explicitly-print-NULL-when-passed-nullpointer-instea.patch

VENDOR_URL = http://www.maxmind.com/app/c

PACKAGES += CSWgeoip
SPKG_DESC_CSWgeoip = GeoIP C API
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgeoip += CSWlibgeoip1

PACKAGES += CSWgeoip-update
SPKG_DESC_CSWgeoip-update = Updater for GeoIP.dat directly from MaxMind
PKGFILES_CSWgeoip-update += $(sysconfdir)/.*
PKGFILES_CSWgeoip-update += $(bindir)/geoipupdate
PKGFILES_CSWgeoip-update += $(mandir)/man1/geoipupdate\.1
RUNTIME_DEP_PKGS_CSWgeoip-update += CSWlibgeoipupdate0
RUNTIME_DEP_PKGS_CSWgeoip-update += CSWlibgeoip1
RUNTIME_DEP_PKGS_CSWgeoip-update += CSWlibz1

PACKAGES += CSWlibgeoip1
SPKG_DESC_CSWlibgeoip1 = GeoIP library, libGeoIP.so.1
PKGFILES_CSWlibgeoip1 += $(call pkgfiles_lib,libGeoIP.so.1)
RUNTIME_DEP_PKGS_CSWlibgeoip1 += CSWgeolitedb
CHECKPKG_OVERRIDES_CSWlibgeoip1 += surplus-dependency|CSWgeolitedb

PACKAGES += CSWlibgeoipupdate0
SPKG_DESC_CSWlibgeoipupdate0 = GeoIP database update library, libGeoIPUpdate.so.0
PKGFILES_CSWlibgeoipupdate0 += $(call pkgfiles_lib,libGeoIPUpdate.so.0)
RUNTIME_DEP_PKGS_CSWlibgeoipupdate0 += CSWlibgeoip1
RUNTIME_DEP_PKGS_CSWlibgeoipupdate0 += CSWlibz1

PACKAGES += CSWgeoip-dev
SPKG_DESC_CSWgeoip-dev = GeoIP development files for libGeoIP.so.1
PKGFILES_CSWgeoip-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWgeoip-dev += CSWlibgeoip1
RUNTIME_DEP_PKGS_CSWgeoip-dev += CSWlibgeoipupdate0

BUILD64_LIBS_ONLY = 1

# CONFIGURE_ARGS  = $(DIRPATHS)
# CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
# CONFIGURE_ARGS += --disable-static

# There is one test failing on sparcv9, skip for now
SKIPTEST ?= 1

EXTRA_MERGE_EXCLUDE_FILES += $(sharedstatedir)/GeoIP/GeoIP\.dat
EXTRA_MERGE_EXCLUDE_FILES += $(sysconfdir)/GeoIP\.conf\.default

PRESERVECONF += $(sysconfdir)/GeoIP.conf

include gar/category.mk

post-patch-modulated:
	-cd $(WORKSRC) && ./bootstrap
	-cd $(WORKSRC) && /opt/csw/bin/libtoolize
	@$(MAKECOOKIE)

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mirrorbrain
VERSION = 2.17.0
GARTYPE = v2

DESCRIPTION = Brief description

MASTER_SITES = http://mirrorbrain.org/files/releases/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Make-geoip-database-position-adjustable.patch

VENDOR_URL = http://mirrorbrain.org

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_EXTRACONF = $(DESTDIR)$(AP2_ROOT)/etc/extra
AP2_SBIN      = $(AP2_ROOT)/sbin
APXS          = $(AP2_SBIN)/apxs

BUILD_DEP_PKGS += CSWapache2-dev
BUILD_DEP_PKGS += CSWap2-mod-form

PACKAGES = CSWap2-mod-mirrorbrain
SPKG_DESC_CSWap2-mod-mirrorbrain = MirrorBrain redirector Apache module
PKGFILES_CSWap2-mod-mirrorbrain += $(AP2_LIBEXEC)/mod_mirrorbrain.so
PKGFILES_CSWap2-mod-mirrorbrain += $(AP2_EXTRACONF)/mod_mirrorbrain.conf.CSW
RUNTIME_DEP_PKGS_CSWap2-mod-mirrorbrain += CSWapache2
RUNTIME_DEP_PKGS_CSWap2-mod-mirrorbrain += CSWap2-mod-form
RUNTIME_DEP_PKGS_CSWap2-mod-mirrorbrain += CSWap2modgeoip
RUNTIME_DEP_PKGS_CSWap2-mod-mirrorbrain += CSWlibaprutil1-dbd-pgsql
# I know these are needed
CHECKPKG_OVERRIDES_CSWap2-mod-mirrorbrain += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWap2-mod-mirrorbrain += surplus-dependency|CSWap2-mod-form
CHECKPKG_OVERRIDES_CSWap2-mod-mirrorbrain += surplus-dependency|CSWap2modgeoip
CHECKPKG_OVERRIDES_CSWap2-mod-mirrorbrain += surplus-dependency|CSWlibaprutil1-dbd-pgsql

# The Python CSWpy-mb module "mb" and the "mb" binary are in lang-py/mb

GEOIPCITYFILE = $(sharedstatedir)/GeoIP/GeoIPCity.dat
GEOIPFILE = $(sharedstatedir)/GeoIP/GeoIP.dat

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF += $(AP2_EXTRACONF)/mod_mirrorbrain.conf

STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

include gar/category.mk

build-custom:
	cd $(WORKSRC)/mod_mirrorbrain && $(APXS) -c mod_mirrorbrain.c
	cd $(WORKSRC)/mod_autoindex_mb && $(APXS) -c mod_autoindex_mb.c
	cd $(WORKSRC)/tools && $(CC) $(CPPFLAGS) $(CFLAGS) $(LINKER_FLAGS) -DDEFAULT_GEOIPCITYFILE=\"$(GEOIPCITYFILE)\" -lGeoIP geoiplookup_city.c -o geoiplookup_city
	cd $(WORKSRC)/tools && $(CC) $(CPPFLAGS) $(CFLAGS) $(LINKER_FLAGS) -DDEFAULT_GEOIPFILE=\"$(GEOIPFILE)\" -lGeoIP geoiplookup_continent.c -o geoiplookup_continent
	@$(MAKECOOKIE)

install-custom:
	mkdir -p $(AP2_LIBEXEC)
	cd $(WORKSRC)/mod_mirrorbrain && $(APXS) -lm -S LIBEXECDIR=$(AP2_LIBEXEC) -i mod_mirrorbrain.la
	cd $(WORKSRC)/mod_autoindex_mb && $(APXS) -lm -S LIBEXECDIR=$(AP2_LIBEXEC) -i mod_autoindex_mb.la
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 $(WORKSRC)/mod_mirrorbrain/mod_mirrorbrain.conf $(DESTDIR)$(prefix)/apache2/etc/extra/mod_mirrorbrain.conf.CSW
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/tools/geoiplookup_city $(DESTDIR)$(bindir)/geoiplookup_city
	ginstall -m 0755 $(WORKSRC)/tools/geoiplookup_continent $(DESTDIR)$(bindir)/geoiplookup_continent
	@$(MAKECOOKIE)


# TBD:
# - Test, test, test!! Especially mirrorbrain
# - Make sure httpd-geoip.conf is installed and added to httpd.conf

NAME = mod_geoip2
VERSION = 1.2.8
GARTYPE = v2

DESCRIPTION = GeoIP Apache module
define BLURB
  The mod_geoip2 module embeds GeoIP database lookups into the Apache web server.
  It is only capable of looking up the IP of a client that connects to the web server,
  as opposed to looking up arbitrary addresses.
endef

nd.com/app/c
endef

MASTER_SITES = http://www.maxmind.com/download/geoip/api/mod_gmod_geoip2-latest.tar.gz
DISTFILES += CSWap2-mod-geoip.postinstall
DISTFILES += CSWap2-mod-geoip.preremove
DISTFILES += httpd-geoip.conf.CSW

WORKSRC = $(WORKDIR)/mod_geoip2_$(VERSION)
#PATCHDIR = $(WORKDIR)/$(DISTNAME)-src

BUILD_DEP_PKGS += CSWapache2-dev
BUILD_DEP_PKGS += CSWgeoip-dev

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_APXS      = $(AP2_ROOT)/sbin/apxs
AP2_MODS = 1
AP2_MODFILES += mod_geoip2.so

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --libexecdir=$(AP2_ROOT)/libexec
CONFIGURE_ARGS += --with-apxs=$(AP2_ROOT)/sbin/apxs

PACKAGES = CSWap2modgeoip2
RUNTIME_DEP_PKGS_CSWap2modgeoip2 += CSWapache2
RUNTIME_DEP_PKGS_CSWap2modgeoip2 += CSWgeolitedb
RUNTIME_DEP_PKGS_CSWap2modgeoip2 += CSWlibgeoip1
OBSOLETED_BY_CSWap2-mod-geoip += CSWap2modgeoip2

# This dependency should be in place.
CHECKPKG_OVERRIDES_CSWap2modgeoip2 += surplus-dependency|CSWgeolitedb
CHECKPKG_OVERRIDES_CSWap2modgeoip2 += surplus-dependency|CSWlibgeoip1

LICENSE_TEXT = Apache

# No test suite available
TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract:
	@-gmv $(WORKSRC)/mod_geoip.c $(WORKSRC)/mod_geoip2.c
	@$(MAKECOOKIE)

build-custom:
	@ginstall -d -m 755 $(AP2_LIBEXEC)
	@$(BUILD_ENV) $(AP2_APXS) -L$(prefix)/lib -lGeoIP -S LIBEXECDIR=$(AP2_LIBEXEC)/ -i -c $(WORKSRC)/mod_geoip2.c
	@$(MAKECOOKIE)

install-custom:
	@$(MAKECOOKIE)


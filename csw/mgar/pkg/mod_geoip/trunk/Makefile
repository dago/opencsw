NAME = mod_geoip2
VERSION = 1.2.8
GARTYPE = v2

DESCRIPTION = GeoIP Apache module
define BLURB
  The mod_geoip2 module embeds GeoIP database lookups into the Apache web server.
  It is only capable of looking up the IP of a client that connects to the web server,
  as opposed to looking up arbitrary addresses.
endef

PACKAGES = CSWap2modgeoip2mind.com/app/c
endef

MASTER_SITES = http://www.maxmind.com/download/geoip/api/mod_gmod_geoip2-latest.tar.gz
WORKSRC = $(WORKDIR)/mod_geoip2_$(VERSION)
#PATCHDIR = $(WORKDIR)/$(DISTNAME)-src

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_APXS      = $(AP2_ROOT)/sbin/apxs
AP2_MODS = 1
AP2_MODFILES += mod_geoip2.so

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --libexecdir=$(AP2_ROOT)/libexec
CONFIGURE_ARGS += --with-apxs=$(AP2_ROOT)/sbin/apxs

BUILD_DEP_PKGS_CSWap2modgeoip2 += CSWapache2-dev
BUILD_DEP_PKGS_CSWap2modgeoip2 += CSWgeoip-dev
#RUNTIME_DEP_PKGS_CSWap2modgeoip2 += CSWapache2
#RUNTIME_DEP_PKGS_CSWap2modgeoip2 += CSWgeolitedb
#RUNTIME_DEP_PKGS_CSWap2modgeoip2 += CSWlibgeoip1
PKGFILES_CSWap2modgeoip2 += $(AP2_LIBEXEC)/mod_geoip2.so

# This dependency should be in place.
#CHECKPKG_OVERRIDES_CSWap2modgeoip2 += surplus-dependency|CSWgeolitedb
#CHECKPKG_OVERRIDES_CSWap2modgeoip2 += surplus-dependency|CSWlibgeoip1

LICENSE_TEXT = Apache

# No test suite available
TEST_SCRIPTS =
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	@ginstall -d -m 755 $(AP2_LIBEXEC)
	@$(AP2_APXS) -L$(prefix)/lib -lGeoIP -S LIBEXECDIR=$(AP2_LIBEXEC)/ -i -c $(WORKSRC)/mod_geoip.c
	@$(MAKECOOKIE)

install-custom:
	@$(MAKECOOKIE)


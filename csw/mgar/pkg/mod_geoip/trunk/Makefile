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
#WORKSRC = $(WORKDIR)/$(DISTNAME)-src/native
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
RUNTIME_DEP_PKGS_CSWap2modgeoip2 += CSWapache2

LICENSE_TEXT = Apache

# No test suite available
TEST_SCRIPTS =

include gar/category.mk


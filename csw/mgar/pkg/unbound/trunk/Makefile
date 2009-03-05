GARNAME = unbound
GARVERSION = 1.2.1
CATEGORIES = server

DESCRIPTION = A validating, recursive, and caching DNS resolver
define BLUR
  Unbound is designed as a set of modular components, so that also
  DNSSEC (secure DNS) validation and stub-resolvers (that do not run as
  a server, but are linked into an application) are easily possible.
endef

MASTER_SITES = http://unbound.net/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWunbound, preinstall)

GARCOMPILER = GCC4

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --without-pthreads
CONFIGUTE_ARGS += --with-solaris-threads
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-pidfile=/var/run/unbound.pid

include gar/category.mk

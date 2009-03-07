GARNAME = nsd
GARVERSION = 3.2.1
CATEGORIES = server

DESCRIPTION = An authoritative only non-recursive name server
define BLURB
  NSD (Name Server Daemon) is a complete implementation of an
  authoritative DNS nameserver.
endef

MASTER_SITES = http://www.nlnetlabs.nl/downloads/nsd/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnsd,)

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw

include gar/category.mk

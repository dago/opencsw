GARNAME = drill
GARVERSION = 1.5.1
CATEGORIES = utils

DESCRIPTION = A dig style dnssec aware dns debugging tool
define BLURB
  Drill is a tool a la dig from BIND. It was designed with DNSSEC in
  mind and should be a useful debugging/query tool for DNSSEC.
endef

MASTER_SITES = http://www.nlnetlabs.nl/projects/ldns/
DISTFILES  = ldns-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://www.nlnetlabs.nl/downloads/ldns/

DISTNAME = ldns-$(GARVERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)/drill

REQUIRED_PKGS = CSWldns
REQUIRED_PKGS += CSWosslrt

GARCOMPILER = GCC4
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-ldns=/opt/csw

include gar/category.mk

NAME = ldns_drill
VERSION = 1.6.12
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A dig style dnssec aware dns debugging tool (ldns)
define BLURB
  Drill is a tool a la dig from BIND. It was designed with DNSSEC in
  mind and should be a useful debugging/query tool for DNSSEC.
endef

MASTER_SITES = http://www.nlnetlabs.nl/projects/ldns/
DISTFILES  = ldns-$(VERSION).tar.gz

PACKAGES = CSWldnsdrill

PACKAGING_PLATFORMS =  solaris9-sparc solaris9-i386

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://www.nlnetlabs.nl/downloads/ldns/

DISTNAME = ldns-$(VERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)/drill

LICENSE = LICENSE

RUNTIME_DEP_PKGS = CSWlibldns1
RUNTIME_DEP_PKGS += CSWosslrt

INCOMPATIBLE_PKGS_CSWldnsdrill = CSWdrill

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-ldns=/opt/csw

TEST_TARGET =

include gar/category.mk

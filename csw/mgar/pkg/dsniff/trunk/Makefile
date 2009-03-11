GARNAME = dsniff
GARVERSION = 2.4b1
CATEGORIES = net

DESCRIPTION = a collection of tools for network auditing and penetration testing
define BLURB
  dsniff is a collection of tools for network auditing and penetration testing.
	dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf, and webspy passively monitor
	a network for interesting data (passwords, e-mail, files, etc.). arpspoof,
	dnsspoof, and macof facilitate the interception of network traffic normally
	unavailable to an attacker (e.g, due to layer-2 switching). sshmitm and
	webmitm implement active monkey-in-the-middle attacks against redirected SSH
	and HTTPS sessions by exploiting weak bindings in ad-hoc PKI. 
endef

MASTER_SITES = http://www.monkey.org/~dugsong/dsniff/beta/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

DISTNAME = $(GARNAME)-2.4

REQUIRED_PKGS += > CSWbdb3 CSWlibnet CSWlibnids CSWlibpcap CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES = buildpatch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

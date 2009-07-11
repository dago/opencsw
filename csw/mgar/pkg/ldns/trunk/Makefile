GARNAME = ldns
GARVERSION = 1.6.0
CATEGORIES = lib

DESCRIPTION = A library for programs conforming to DNS RFCs and drafts
define BLURB
  Ldns is a library to simplify implementation of recent DNS RFCs. The goal
  is to allow depelopers to easily create software conforming to current RFCs
  and experimental software for current Internet drafts.
  Because ldns is written in C it should be a lot faster than Perl or other
  scripting languages.
endef

MASTER_SITES = http://www.nlnetlabs.nl/projects/ldns/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWldns.doxyparse.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://www.nlnetlabs.nl/downloads/ldns\

BUILD64 = 1
EXTRA_BUILD_ISAS_i386 = pentium_pro
EXTRA_BUILD_ISAS_sparc = sparcv8plus

REQUIRED_PKGS += CSWosslrt

PATCHFILES = CSWldns.doxyparse.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --enable-sha2

TEST_TARGET =

include gar/category.mk

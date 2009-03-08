GARNAME = pwgen
GARVERSION = 2.06
CATEGORIES = apps

DESCRIPTION = pwgen generates passwords which can be easily memorized by a human
define BLURB
	Pwgen is a small, GPL'ed password generator which creates passwords which can
	be easily memorized by a human. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://pwgen.sourceforge.net

LICENSE = LICENSE

#REQUIRED_PKGS = CSWggettextrt CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=28391
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES = mainpatch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

post-extract:
	( cp $(FILEDIR)/LICENSE $(WORKSRC) )
	@$(MAKECOOKIE)

#post-extract-$(MODULATION):
#	( cp $(FILEDIR)/LICENSE $(WORKSRC_FIRSTMOD) )
#	@$(MAKECOOKIE)

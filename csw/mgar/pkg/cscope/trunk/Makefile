GARNAME = cscope
GARVERSION = 15.7a
CATEGORIES = utils

DESCRIPTION = A text screen-based source browser
define BLURB
  cscope is a developer's tool for browsing source code. It has an impeccable
  Unix pedigree, having been originally developed at Bell Labs back in the days
  of the PDP-11. Cscope was part of the official AT&T Unix distribution for many
  years, and has been used to manage projects involving 20 million lines of code! 
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = cscope

DISTFILES = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Test suite won't run as root!
TEST_SCRIPTS =

include gar/category.mk

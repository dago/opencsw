GARNAME = ncal
GARVERSION = 1.0
CATEGORIES = utils

DESCRIPTION = Displays a calendar and the date of easter
define BLURB
  The cal utility displays a simple calendar in traditional format and 
  ncal offers an alternative layout, more options and the date of easter.
endef

MASTER_SITES = http://www.opencsw.org/~benny/
DISTFILES  = $(GARNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# since there is no configure script, this is intentionally left empty
CONFIGURE_SCRIPTS =

# no build tests
SKIPTEST = 1

# fix distname
DISTNAME = $(GARNAME)

include gar/category.mk

pre-build-modulated:
	gsed -i'' 's,^\(CFLAGS =\),\1 $(CFLAGS),' $(WORKSRC)/Makefile

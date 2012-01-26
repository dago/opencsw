NAME = ncal
VERSION = 1.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Displays a calendar and the date of easter
define BLURB
  The cal utility displays a simple calendar in traditional format and 
  ncal offers an alternative layout, more options and the date of easter.
endef

MASTER_SITES = http://www.opencsw.org/~benny/
DISTFILES  = $(NAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# since there is no configure script, this is intentionally left empty
CONFIGURE_SCRIPTS =

# no build tests
SKIPTEST = 1

# fix distname
DISTNAME = $(NAME)

include gar/category.mk

pre-build-modulated:
	gsed -i'' 's,^\(CFLAGS =\),\1 $(CFLAGS),' $(WORKSRC)/Makefile

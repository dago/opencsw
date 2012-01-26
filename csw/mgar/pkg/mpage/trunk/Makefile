# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = mpage
VERSION = 2.5.6
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Print several pages on a single sheet of paper.
define BLURB
  Print several pages on a single sheet of paper.
endef

MASTER_SITES = http://www.mesa.nl/pub/mpage/
DISTFILES  = $(NAME)-$(VERSION).tgz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

# doesn't come with a configure script
CONFIGURE_SCRIPTS =

PATCHFILES = Makefile.patch

TEST_SCRIPTS =

include gar/category.mk

#
GARCOMPILER = GCC4




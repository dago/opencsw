# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tuxpaint
VERSION = 0.9.21
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Simple drwaing program
define BLURB
  Tux Paint is a free, award-winning drawing program for children ages 3 to 12 (for example, preschool and K-6). Tux Paint is used in schools around the world as a computer literacy drawing activity. It combines an easy-to-use interface, fun sound effects, and an encouraging cartoon mascot who guides children as they use the program.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GCC4

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =

BUILD_ARGS += PREFIX=$(prefix)

include gar/category.mk


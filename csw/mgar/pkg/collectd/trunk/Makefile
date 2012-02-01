# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = collectd
VERSION = 5.0.2
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://collectd.org/files/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


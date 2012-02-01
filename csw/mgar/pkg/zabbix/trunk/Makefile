# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = zabbix
VERSION = 1.8.10
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

#BUILD64 = 1
#BUILD_ISA_i386 = amd64
BUILD64_ONLY = 1


# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS) --with-mysql --with-libcurl --enable-server --enable-agent --enable-ipv6

include gar/category.mk


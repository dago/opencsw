# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME 		= lsdvd
VERSION 	= 0.16
GARTYPE 	= v2
CATEGORIES 	= apps

DESCRIPTION = Print information about the contents and structure of a DVD
define BLURB
  Print information about the contents and structure of a DVD
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES  		=	$(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD_DEP_PKGS		=	CSWlibdvdreaddevel
RUNTIME_DEP_PKGS	=	\
						CSWlibdvdread \
						CSWlibgcc-s1
CONFIGURE_ARGS		=	$(DIRPATHS)
GARCOMPILER			=	GNU

include gar/category.mk


# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

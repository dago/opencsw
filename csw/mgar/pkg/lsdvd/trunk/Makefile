# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME 		= lsdvd
VERSION 	= 0.16
GARTYPE 	= v2

DESCRIPTION = Print information about the contents and structure of a DVD
define BLURB
  Print information about the contents and structure of a DVD
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES  		=	$(DISTNAME).tar.gz

BUILD_DEP_PKGS		=	CSWlibdvdread-dev
RUNTIME_DEP_PKGS	=	CSWlibdvdread
CONFIGURE_ARGS		=	$(DIRPATHS)
GARCOMPILER			=	GNU

include gar/category.mk


# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

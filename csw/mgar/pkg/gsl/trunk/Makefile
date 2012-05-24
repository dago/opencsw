# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gsl
VERSION = 1.15
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = GNU Scientific Library
define BLURB
  GNU Scientific Library
endef

DISTFILES		=	$(DISTNAME).tar.gz
MASTER_SITES	=	$(GNU_MIRROR)

CONFIGURE_ARGS = $(DIRPATHS)

GARCOMPILER			=	GNU

include gar/category.mk

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

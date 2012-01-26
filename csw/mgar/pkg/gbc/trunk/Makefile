# $Id$
NAME = bc
VERSION = 1.06
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = An interactive algebraic language with arbitrary precision which follows the POSIX 1003.2
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES = 0001-Do-not-use-Wall.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWgbc
CATALOGNAME = gbc

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

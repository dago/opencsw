NAME = glpk
VERSION = 4.43
CATEGORIES = lib

DESCRIPTION = GNU Linear Programming Kit
define BLURB
  The GLPK (GNU Linear Programming Kit) package is intended for solving large-scale
  linear programming (LP), mixed integer programming (MIP), and other related problems.
  It is a set of routines written in ANSI C and organized in the form of a callable library.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibglpk

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# This is normal for amd64 on i386
CHECKPKG_OVERRIDES_CSWlibglpk += soname-not-found|libm.so.2

include gar/category.mk

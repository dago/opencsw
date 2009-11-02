GARNAME = glpk
GARVERSION = 4.39
CATEGORIES = lib

DESCRIPTION = GNU Linear Programming Kit
define BLURB
  The GLPK (GNU Linear Programming Kit) package is intended for solving large-scale
  linear programming (LP), mixed integer programming (MIP), and other related problems.
  It is a set of routines written in ANSI C and organized in the form of a callable library.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibglpk

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

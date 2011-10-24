NAME = glpk
VERSION = 4.47
CATEGORIES = lib

DESCRIPTION = GNU Linear Programming Kit
define BLURB
  The GLPK (GNU Linear Programming Kit) package is intended for solving large-scale
  linear programming (LP), mixed integer programming (MIP), and other related problems.
  It is a set of routines written in ANSI C and organized in the form of a callable library.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWlibglpk0
SPKG_DESC_CSWlibglpk0 = GNU linear programming kit library, libglpk.so.0
PKGFILES_CSWlibglpk0 += $(call pkgfiles_lib,libglpk.so.0)
OBSOLETED_BY_CSWlibglpk0 = CSWlibglpk

PACKAGES += CSWlibglpk-dev
SPKG_DESC_CSWlibglpk-dev = Development files for libglpk.so.0
PKGFILES_CSWlibglpk-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibglpk-dev += CSWlibglpk0

PACKAGES += CSWglpk
SPKG_DESC_CSWglpk = GNU linear programming kit
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWglpk += CSWlibglpk0

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

# $Id$
NAME = bzflag
VERSION = 2.4.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A free multiplayer multiplatform 3D tank battle game
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES += 0001-Keep-norunpath.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

libdir_install = $(prefix)/lib/bzflag

RUNTIME_DEP_PKGS_CSWbzflag += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibz1
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibglew1-7
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibcares2
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibidn11
# Old-style deps
RUNTIME_DEP_PKGS_CSWbzflag += CSWmesa

EXTRA_LINKER_FLAGS += -norunpath

include gar/category.mk

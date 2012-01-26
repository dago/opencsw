# $Id$
NAME = bzflag
VERSION = 2.0.16
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A free multiplayer multiplatform 3D tank battle game
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES += 0001-Fix-ambiguity-between-double-and-long-double.patch
PATCHFILES += 0002-Make-function-location-explicit.patch
PATCHFILES += 0003-Force-inclusion-of-glew.h-before-gl.h.patch
PATCHFILES += 0004-Do-not-use-const-as-non-const-is-required-at-some-pl.patch
PATCHFILES += 0005-Make-arguments-constant-as-required.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWbzflag += CSWglew
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibsdl
RUNTIME_DEP_PKGS_CSWbzflag += CSWcurlrt
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibidn
RUNTIME_DEP_PKGS_CSWbzflag += CSWzlib
RUNTIME_DEP_PKGS_CSWbzflag += CSWmesa
RUNTIME_DEP_PKGS_CSWbzflag += CSWlibcares
RUNTIME_DEP_PKGS_CSWbzflag += CSWnas
RUNTIME_DEP_PKGS_CSWbzflag += CSWosslrt
RUNTIME_DEP_PKGS_CSWbzflag += CSWoldaprt

include gar/category.mk

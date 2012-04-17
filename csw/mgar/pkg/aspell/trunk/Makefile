# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = aspell
VERSION = 0.60.6.1
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Spell checker
define BLURB
  Long description
endef

MASTER_SITES = ftp://ftp.gnu.org/gnu/aspell/
DISTFILES  = $(DISTNAME).tar.gz

EXTRA_LDFLAGS = -lm

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWaspell += CSWlibintl8
RUNTIME_DEP_PKGS_CSWaspell += CSWlibncursesw5

CHECKPKG_OVERRIDES_CSWaspell += file-with-bad-content
CHECKPKG_OVERRIDES_CSWaspell += bad-rpath-entry

include gar/category.mk

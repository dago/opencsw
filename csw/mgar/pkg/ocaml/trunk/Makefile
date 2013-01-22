NAME = ocaml
VERSION = 3.11.2
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://caml.inria.fr/pub/distrib/ocaml-3.11/
DISTFILES  = $(NAME)-GARCOMPILER = GCC4

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# UPSTREAM_MASTER_SITES = 

PATCHFILES += 0-patch
PATCHFILES += 10-patch
PATCHFILES += 12-patch
PATCHFILES += 13-patch
PATCHFILES += 14-patch
PATCHFILES += 15-patch
PATCHFILES += 16-patch
PATCHFILES += 17-patch
PATCHFILES += 18-patch
PATCHFILES += 19-patch
PATCHFILES += 2-patch
PATCHFILES += 20-patch
PATCHFILES += 21-patch
PATCHFILES += 3-patch
PATCHFILES += 4-patch
PATCHFILES += 5-patch
PATCHFILES += 6-patch
PATCHFILES += 7-patch
PATCHFILES += 8-patch
PATCHFILES += 9-patch

RUNTIME_DEP_PKGS_CSWocaml += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWocaml += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWocaml += CSWlibtk8-5
Wocaml = CSWlibx11
LICENSE = LICENSE

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $# BUILD_ARGS = world.opt
BUILD_ARGS = world opt
#CONFIGURE_ARGS = $(DIRPATHS)
# CONFIGURE_ARGS += -bindir $(bindir)
# -bindir $(bindir)
CONFIGURE_ARGS += -libdir $(libdir)
CONFIGURE_ARGS += -mandir $(mandir)
CONFIGURE_ARGS += -prefix $(prefix)
Cverbose
# CONFIGURE_ARGS += -cc "$(CC) $(CFLAGS)"
# CONFIGURE_ARGS += -x11include $(prefix)/X11/include
# CONFIGURE_ARGS += -x11lib $(prefix)/X11/lib
INSTALL_ARGS += PWD=${PWD}/$(WORKSRC)

TEST_TARGET =

include gar/category.mk

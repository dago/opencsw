NAME = ocaml
VERSION = 3.11.2
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://caml.inria.fr/pub/distrib/ocaml-3.11/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# UPSTREAM_MASTER_SITES = 

RUNTIME_DEP_PKGS_CSWocaml = CSWlibx11
LICENSE = LICENSE

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD_ARGS = world.opt
#CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += -bindir $(bindir)
CONFIGURE_ARGS += -libdir $(libdir)
CONFIGURE_ARGS += -mandir $(mandir)
CONFIGURE_ARGS += -prefix $(prefix)
CONFIGURE_ARGS += -cc "$(CC) $(CFLAGS)"
CONFIGURE_ARGS += -x11include $(prefix)/X11/include
CONFIGURE_ARGS += -x11lib $(prefix)/X11/lib

TEST_TARGET =

include gar/category.mk

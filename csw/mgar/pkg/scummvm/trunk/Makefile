GARNAME = scummvm
GARVERSION = 1.0.0
CATEGORIES = apps

DESCRIPTION = Virtual machine for several classic graphical point-and-click adventure games
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GCC4

# Custom configure
CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --datadir=$(datadir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --enable-all-engines


include gar/category.mk

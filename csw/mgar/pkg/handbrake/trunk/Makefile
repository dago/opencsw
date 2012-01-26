NAME = HandBrake
VERSION = 0.9.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://download.handbrake.fr/handbrake/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GNU

CONFIGURE_ARGS = --prefix=$(prefix)

BUILD_SCRIPTS = $(WORKSRC)/build/Makefile

BUILD_ARGS = M4.exe=/opt/csw/bin/gm4


include gar/category.mk

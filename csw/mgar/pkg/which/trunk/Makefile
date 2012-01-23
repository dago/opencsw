NAME = which
VERSION = 2.20
CATEGORIES = utils

DESCRIPTION = locate a command and display its pathname or alias
define BLURB
  GNU which - is a utility that is used to find which executable (or alias or shell function) is executed when entered on the shell prompt
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWwhich,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
CONFIGURE_ARGS += --disable-dependency-tracking

BUILD64_LIBS_ONLY = 1

include gar/category.mk

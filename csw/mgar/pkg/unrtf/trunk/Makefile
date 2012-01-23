NAME = unrtf
VERSION = 0.21.1
CATEGORIES = utils

DESCRIPTION = A tool which converts documents from Rich Text Format
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWiconv

EXTRA_LINKER_FLAGS = -liconv

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

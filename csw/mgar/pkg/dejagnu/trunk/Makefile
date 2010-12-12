NAME = dejagnu
VERSION = 1.4.4
CATEGORIES = apps

DESCRIPTION = GNU auto-configuration tool
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

#PATCHFILES = 0001-Prefer-CSW-tools.patch

#BUILD_DEP_PKGS = CSWhelp2man
#RUNTIME_DEP_PKGS = CSWgawk CSWgm4 CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Tests take a loooooonnng time.
#TEST_SCRIPTS =

#EXTRA_MERGE_EXCLUDE_FILES = $(infodir)/standards.info

include gar/category.mk

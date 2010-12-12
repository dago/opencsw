NAME = help2man
VERSION = 1.38.2
CATEGORIES = devel

DESCRIPTION = A tool for automatically generating simple manual pages from program output
define BLURB
  help2man is a tool for automatically generating simple manual pages from program output.
  It is intended to provide an easy way for software authors to include a manual page
  in their distribution without having to maintain that document.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWpmlocalegettext
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

CONFIGURE_ARGS = $(DIRPATHS)
# We need to disable NLS as we don't have preloadable_libintl.so
# (only installed on glibc systems)
CONFIGURE_ARGS += --disable-nls

TEST_SCRIPTS =

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWhelp2man += surplus-dependency|CSWpmlocalegettext

include gar/category.mk

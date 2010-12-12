NAME = diffutils
VERSION = 3.0
CATEGORIES = utils

DESCRIPTION = Diff utilities
define BLURB
 The diff package provides the diff, diff3, sdiff, and cmp programs.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv CSWlibsigsegv
BUILD_DEP_PKGS = CSWggettext CSWiconv CSWlibsigsegv

VENDOR_URL = http://www.gnu.org/software/diffutils/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/lib/charset.alias

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

# We need GNU tail for the testsuite
PATH := /opt/csw/gnu:$(PATH)


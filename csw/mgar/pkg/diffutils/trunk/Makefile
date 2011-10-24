NAME = diffutils
VERSION = 3.2
CATEGORIES = utils

DESCRIPTION = Diff utilities
define BLURB
 The diff package provides the diff, diff3, sdiff, and cmp programs.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.xz

BUILD_DEP_PKGS += CSWlibsigsegv-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibiconv-dev

RUNTIME_DEP_PKGS_CSWdiffutils += CSWlibsigsegv2
RUNTIME_DEP_PKGS_CSWdiffutils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWdiffutils += CSWlibiconv2

VENDOR_URL = http://www.gnu.org/software/diffutils/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/lib/charset.alias

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

# We need GNU tail for the testsuite
PATH := /opt/csw/gnu:$(PATH)


NAME = patch
VERSION = 2.6.1
CATEGORIES = utils

DESCRIPTION = GNU patch utility
define BLURB
  The GNU patch utility.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz 

# Add some missing files from gnulib until this is fixed:
#   https://savannah.gnu.org/bugs/?30378
PATCHFILES  = 0001-Add-missing-strnlen.c-from-GNUlib.patch
PATCHFILES += 0002-Add-missing-m4-files.patch

PACKAGES = CSWgpatch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWlibgnugetopt

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

EXTRA_LINKER_FLAGS = -lgnugetopt
BUILD_ARGS = SHELL=bash

include gar/category.mk

post-extract-modulated:
	@# GARs usage of .git for patching in the package confuses the upstream building as
	@# if it was bootstrapped.
	-echo "exit 0" > $(WORKSRC)/update-version.sh

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)


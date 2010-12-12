NAME = make
VERSION = 3.82
CATEGORIES = devel

DESCRIPTION = Controls generation of executables and other compile-related tasks
define BLURB
  GNU Make examines the timestamps on a set of interdependent files, and, if
  necessary, issues commands to bring them up-to-date. The user creates a
  makefile describing the files, their relationships, and the commands to run.
  Most often make is used to rebuild libraries and programs when their sources
  are changed, but it can be used for any situation where one set of files needs
  to be generated from another set.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWgmake
CATALOGNAME = gmake

VENDOR_URL = http://www.gnu.org/software/make/

DEP_PKGS = CSWggettextrt

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

TEST_TARGET = check

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)


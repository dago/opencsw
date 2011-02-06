NAME = dialog
VERSION = 1.1r20110118
VERSION2 = 1.1
RELEASE = 20110118
DISTNAME = $(NAME)-$(VERSION2)-$(RELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = utils

DESCRIPTION = A script-interpreter which provides a set of curses widgets
define BLURB
  A script-interpreter which provides a set of curses widgets
endef

MASTER_SITES = http://invisible-island.net/datafiles/release/
DISTFILES = $(NAME).tar.gz

EXTRA_MODULATORS = CURSES
MODULATIONS_CURSES = ncurses minimal
MERGE_SCRIPTS_isa-default-curses-ncurses = copy-all
MERGE_SCRIPTS_isa-default-curses-minimal = copy-all

PACKAGES = CSWdialog CSWdialog-minimal
SPKG_DESC_CSWdialog = A script-interpreter which provides a set of curses widgets
SPKG_DESC_CSWdialog-minimal = A script-interpreter which provides a set of curses widgets (traditional curses version)

RUNTIME_DEP_PKGS_CSWdialog += CSWncurses

CHECKPKG_OVERRIDES_CSWdialog += file-with-bad-content
CHECKPKG_OVERRIDES_CSWdialog += missing-dependency|CSWpython

SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)
ifeq ($(CURSES),ncurses)
CONFIGURE_ARGS += --with-ncurses
endif

include gar/category.mk

post-install-modulated:
	@echo " ==> Post-install for $(NAME) (custom)"

	@mv $(DESTDIR)$(bindir)/dialog $(DESTDIR)$(bindir)/dialog.$(CURSES)
	@mv $(DESTDIR)$(mandir)/man1/dialog.1 $(DESTDIR)$(mandir)/man1/dialog.1.$(CURSES)
	@$(MAKECOOKIE)

post-merge:
	@echo " ==> Post-merge for $(NAME) (custom)"
	@ginstall -d $(PKGROOT)$(docdir)/$(NAME)/samples
	@cp -r $(WORKSRC_FIRSTMOD)/samples $(PKGROOT)$(docdir)/$(NAME)/

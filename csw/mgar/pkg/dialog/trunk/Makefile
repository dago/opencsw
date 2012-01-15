# Reminder: to build dialog_minimal, use
#   gmake package-CSWdialog-minimal

NAME = dialog
VERSION = 1.1r20111020
VERSION2 = 1.1
RELEASE = 20111020
DISTNAME = $(NAME)-$(VERSION2)-$(RELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = utils

DESCRIPTION = A script-interpreter which provides a set of curses widgets
define BLURB
  A script-interpreter which provides a set of curses widgets
endef

MASTER_SITES = http://invisible-island.net/datafiles/release/
DISTFILES = $(NAME).tar.gz
VENDOR_URL = http://invisible-island.net/dialog

EXTRA_MODULATORS = CURSES
MODULATIONS_CURSES = ncurses minimal
MERGE_SCRIPTS_isa-default-curses-ncurses = copy-all
MERGE_SCRIPTS_isa-default-curses-minimal = copy-all

PACKAGES = CSWdialog CSWdialog-minimal
SPKG_DESC_CSWdialog = A script-interpreter which provides a set of curses widgets
SPKG_DESC_CSWdialog-minimal = A script-interpreter which provides a set of curses widgets (traditional curses version)
CATALOGNAME_CSWdialog = dialog
CATALOGNAME_CSWdialog-minimal = dialog_minimal

RUNTIME_DEP_PKGS_CSWdialog += CSWlibncurses5

CHECKPKG_OVERRIDES_CSWdialog += file-with-bad-content
CHECKPKG_OVERRIDES_CSWdialog += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWdialog += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWdialog-minimal += surplus-dependency|CSWalternatives

PKGFILES_CSWdialog-minimal = $(bindir).*minimal $(mandir).*minimal

ALTERNATIVES_CSWdialog = ncurses
ALTERNATIVES_CSWdialog-minimal = minimal
ALTERNATIVE_ncurses = $(bindir)/dialog dialog $(bindir)/dialog.ncurses 50 $(mandir)/man1/dialog.1 dialog.man $(mandir)/man1/dialog.1.ncurses
ALTERNATIVE_minimal = $(bindir)/dialog dialog $(bindir)/dialog.minimal 25 $(mandir)/man1/dialog.1 dialog.man $(mandir)/man1/dialog.1.minimal

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

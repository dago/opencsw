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

CHECKPKG_OVERRIDES_CSWdialog += file-with-bad-content
CHECKPKG_OVERRIDES_CSWdialog += missing-dependency|CSWpython

SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated:
	@echo " ==> Post-install for $(NAME) (custom)"
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)/samples
	@cp -r $(WORKSRC)/samples $(DESTDIR)$(docdir)/$(NAME)/
	@$(MAKECOOKIE)

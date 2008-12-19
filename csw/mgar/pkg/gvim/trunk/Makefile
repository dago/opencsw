GARNAME = vim
DISTVERSION = 7.2
CATEGORIES = utils
SPKG_SOURCEURL = http://www.vim.org/download.php
DESCRIPTION = Vi IMproved with GTK+ support
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

#DEPENDS = utils/mktemp lib/ncurses

include ../vim/files/config.mk
DISTFILES += $(call admfiles,CSWgvim,prototype depend)
DISTFILES += gvim.desktop

CONFIGURE_ARGS += --with-vim-name="vim-x11"
CONFIGURE_ARGS += --enable-gui=gnome2

include ../vim/files/patches.mk

INSTALL_SCRIPTS = minimal

# Test requires controlling terminal
TEST_SCRIPTS =

include gar/category.mk

# Don't install the runtime
install-minimal:
	@$(INSTALL_ENV) $(MAKE) -C $(WORKSRC)/src \
		installvimbin installlinks installtools installgtutorbin
	mkdir -p $(DESTDIR)/opt/csw/share/pixmaps
	cp $(WORKSRC)/runtime/vim48x48.png $(DESTDIR)/opt/csw/share/pixmaps/gvim.png
	mkdir -p $(DESTDIR)/opt/csw/share/applications
	cp $(DOWNLOADDIR)/gvim.desktop $(DESTDIR)/opt/csw/share/applications/gvim.desktop
	mv $(DESTDIR)/opt/csw/bin/gvim-x11tutor $(DESTDIR)/opt/csw/bin/gvimtutor
	@$(MAKECOOKIE)
	$(DONADA)

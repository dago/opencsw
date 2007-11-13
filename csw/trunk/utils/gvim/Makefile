GARNAME = vim
DISTVERSION = 7.1
CATEGORIES = utils

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

CONFIGURE_ARGS += --with-vim-name="vim-x11"
CONFIGURE_ARGS += --enable-gui=gnome2

include ../vim/files/patches.mk

INSTALL_SCRIPTS = minimal

# Test requires controlling terminal
TEST_SCRIPTS =

include ../category.mk

# Don't install the runtime
install-minimal:
	@$(INSTALL_ENV) $(MAKE) -C $(WORKSRC)/src \
		installvimbin installlinks installtools
	@$(MAKECOOKIE)
	$(DONADA)


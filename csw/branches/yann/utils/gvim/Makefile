GARNAME = vim
GARVERSION = 7.0
CATEGORIES = utils

DESCRIPTION = Vi IMproved with GTK+ support
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

MASTER_SITES = ftp://ftp.vim.org/pub/vim/unix/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgvim,prototype depend)

WORKSRC = $(WORKDIR)/$(GARNAME)70

include files/vim_patches.mk

#DEPENDS = utils/mktemp lib/ncurses

INSTALL_SCRIPTS = minimal

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --with-vim-name="vim-x11"
CONFIGURE_ARGS += --with-features=huge 
CONFIGURE_ARGS += --enable-cscope
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-gui=gnome2
CONFIGURE_ARGS += --enable-perlinterp
CONFIGURE_ARGS += --enable-pythoninterp
CONFIGURE_ARGS += --with-python-config-dir=$(libdir)/python2.3/config/

# Test requires controlling terminal
ENABLE_TEST = 0

include ../category.mk

# Avlid direct depends for perl/python
LD_OPTIONS += -zlazyload

# Don't install the runtime
install-minimal:
	@$(INSTALL_ENV) $(MAKE) -C $(WORKSRC)/src \
		installvimbin installlinks installtools
	@$(MAKECOOKIE)
	$(DONADA)


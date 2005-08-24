GARNAME = vim
GARVERSION = 6.3
CATEGORIES = utils

DESCRIPTION = Vi IMproved
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

MASTER_SITES = ftp://ftp.vim.org/pub/vim/unix/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWvim.gspec CSWvim.depend CSWvim.prototype
DISTFILES += CSWvimrt.gspec CSWvimrt.prototype

WORKSRC = $(WORKDIR)/$(GARNAME)63

# When the DIGRAPH feature is turned on, EXTERN 'e_number'
# conflicts with perl CORE (found in 5.8.3).
#PATCHFILES += perl583core.diff

#DEPENDS = utils/mktemp lib/ncurses

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --with-features=huge 
CONFIGURE_ARGS += --enable-gui=gnome2
CONFIGURE_ARGS += --enable-perlinterp
CONFIGURE_ARGS += --enable-pythoninterp
CONFIGURE_ARGS += --with-python-config-dir=$(libdir)/python2.3/config/

# Test requires controlling terminal
ENABLE_TEST = 0

include ../category.mk

LD_OPTIONS += -zlazyload


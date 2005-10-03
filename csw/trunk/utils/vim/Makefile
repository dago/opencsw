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
WORKSRC = $(WORKDIR)/$(GARNAME)63

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWvim.gspec CSWvim.prototype CSWvim.depend
DISTFILES += CSWvimrt.gspec CSWvimrt.prototype

#DEPENDS = utils/mktemp lib/ncurses

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(GARNAME)
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --disable-xim
CONFIGURE_ARGS += --without-x
CONFIGURE_ARGS += --enable-cscope
CONFIGURE_ARGS += --enable-gui=no
CONFIGURE_ARGS += --disable-gpm
CONFIGURE_ARGS += --enable-static --disable-shared
#CONFIGURE_ARGS += --enable-perlinterp
CONFIGURE_ARGS += --enable-pythoninterp
CONFIGURE_ARGS += --with-python-config-dir=$(libdir)/python2.3/config/

# Test requires controlling terminal
ENABLE_TEST = 0

include ../category.mk

# Avoid direct depends for perl/python
LD_OPTIONS += -zlazyload


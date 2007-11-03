GARNAME = vim
DISTVERSION = 7.1
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
WORKSRC = $(WORKDIR)/$(GARNAME)$(subst .,,$(DISTVERSION))

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.bz2
DISTFILES += $(GARNAME)-$(DISTVERSION)-lang.tar.gz
DISTFILES += $(GARNAME)-$(DISTVERSION)-extra.tar.gz
DISTFILES += $(call admfiles,CSWvim,depend prototype)
DISTFILES += $(call admfiles,CSWvimrt,prototype)

include files/patches.mk

#DEPENDS = utils/mktemp lib/ncurses

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(GARNAME)
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --disable-xim
CONFIGURE_ARGS += --without-x
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-cscope
CONFIGURE_ARGS += --enable-gui=no
CONFIGURE_ARGS += --disable-gpm
CONFIGURE_ARGS += --enable-static
CONFIGURE_ARGS += --disable-shared
#CONFIGURE_ARGS += --enable-perlinterp
CONFIGURE_ARGS += --enable-pythoninterp
CONFIGURE_ARGS += --with-python-config-dir=$(libdir)/python/config/

# Test requires controlling terminal
TEST_SCRIPTS =

include ../category.mk

# Avoid direct depends for perl/python
LD_OPTIONS += -zlazyload
export LD_OPTIONS


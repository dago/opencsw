GARNAME = vim
DISTVERSION = 7.2
CATEGORIES = utils
SPKG_SOURCEURL = http://www.vim.org/download.php
DESCRIPTION = Vi IMproved
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

#DEPENDS = utils/mktemp lib/ncurses

include files/config.mk
DISTFILES += $(call admfiles,CSWvim,depend prototype)
DISTFILES += $(call admfiles,CSWvimrt,prototype)

CONFIGURE_ARGS += --disable-xim
CONFIGURE_ARGS += --without-x
CONFIGURE_ARGS += --enable-gui=no
CONFIGURE_ARGS += --disable-gpm

include files/patches.mk

# Test requires controlling terminal
TEST_SCRIPTS =

include gar/category.mk
include files/rules.mk

GARNAME = zsh
GARVERSION = 4.3.9
CATEGORIES = devel

DESCRIPTION = Powerful UNIX shell
define BLURB
  Zsh is a shell designed for interactive use, although it is also a
  powerful scripting language. Many of the useful features of bash,
  ksh, and tcsh were incorporated into zsh; many original features were added.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWzsh,depend postinstall postremove)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://sourceforge.net/project/showfiles.php?group_id=4068
#UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-maildir-support
CONFIGURE_ARGS += --enable-fndir=$(sharedstatedir)/$(GARNAME)/functions
CONFIGURE_ARGS += --enable-pcre

include gar/category.mk

# Use term.h from ncurses or we get compile errors
#   http://www.zsh.org/mla/workers/2007/msg01236.html
CFLAGS := -I$(includedir)/ncurses $(CFLAGS)

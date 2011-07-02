NAME = readline
VERSION = 4.3
CATEGORIES = lib

DESCRIPTION = GNU readline
define BLURB
  The Readline library provides a set of functions for use by applications
  that allow users to edit command lines as they are typed in.  Both
  Emacs and vi editing modes are available.  The Readline library includes
  additional functions to maintain a list of previously-entered command
  lines, to recall and perhaps reedit those lines, and perform csh-like
  history expansion on previous commands.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://tiswww.case.edu/php/chet/readline/rltop.html

PACKAGES += CSWlibhistory4
CATALOGNAME_CSWlibhistory4 = libhistory4
SPKG_DESC_CSWlibhistory4 = GNU readline library, libhistory.so.4
PKGFILES_CSWlibhistory4 = $(call pkgfiles_lib,libhistory.so.4)

PACKAGES += CSWlibreadline4
CATALOGNAME_CSWlibreadline4 = libreadline4
SPKG_DESC_CSWlibreadline4 = GNU readline library, libreadline.so.4
PKGFILES_CSWlibreadline4 = $(call pkgfiles_lib,libreadline.so.4)

BUILD64 = 1
NORUNPATH = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-curses

include gar/category.mk

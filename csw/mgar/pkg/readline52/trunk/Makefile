NAME = readline
VERSION = 5.2
CATEGORIES = lib
GARTYPE = v2

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

PACKAGES += CSWlibhistory5
CATALOGNAME_CSWlibhistory5 = libhistory5
SPKG_DESC_CSWlibhistory5 = GNU readline library, libhistory.so.5
PKGFILES_CSWlibhistory5 = $(call pkgfiles_lib,libhistory.so.5)
# This dependency is not really necessary, just because we unconditionally add
# "-lncurses" to LDFLAGS as this does not happen automatically.
RUNTIME_DEP_PKGS_CSWlibhistory5 += CSWlibncurses5

PACKAGES += CSWlibreadline5
CATALOGNAME_CSWlibreadline5 = libreadline5
SPKG_DESC_CSWlibreadline5 = GNU readline library, libreadline.so.5
PKGFILES_CSWlibreadline5 = $(call pkgfiles_lib,libreadline.so.5)
RUNTIME_DEP_PKGS_CSWlibreadline5 += CSWlibncurses5

BUILD64_LIBS_ONLY = 1
NORUNPATH = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-curses

include gar/category.mk

LDFLAGS := $(filter-out -xarch=%,$(filter-out -m%,$(LDFLAGS))) -R$(libdir) -lncurses

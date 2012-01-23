NAME = readline
VERSION = 6.2
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
PATCHFILES += patch-history.3.diff

VENDOR_URL = http://tiswww.case.edu/php/chet/readline/rltop.html

# From pkg/readline43
FOREIGN_PACKAGES += CSWlibhistory4
OBSOLETED_BY_CSWlibhistory4 = CSWreadline
FOREIGN_PACKAGES += CSWlibreadline4
OBSOLETED_BY_CSWlibreadline4 = CSWreadline

# From pkg/readline52
FOREIGN_PACKAGES += CSWlibhistory5
OBSOLETED_BY_CSWlibhistory5 = CSWreadline
FOREIGN_PACKAGES += CSWlibreadline5
OBSOLETED_BY_CSWlibreadline5 = CSWreadline

PACKAGES += CSWlibhistory6
CATALOGNAME_CSWlibhistory6 = libhistory6
SPKG_DESC_CSWlibhistory6 = GNU readline library, libhistory.so.6
PKGFILES_CSWlibhistory6 = $(call pkgfiles_lib,libhistory.so.6)
# This dependency is not really necessary, just because we unconditionally add
# "-lncurses" to LDFLAGS as this does not happen automatically.
RUNTIME_DEP_PKGS_CSWlibhistory6 += CSWlibncurses5
OBSOLETED_BY_CSWlibhistory6 = CSWreadline

PACKAGES += CSWlibreadline6
CATALOGNAME_CSWlibreadline6 = libreadline6
SPKG_DESC_CSWlibreadline6 = GNU readline library, libreadline.so.6
PKGFILES_CSWlibreadline6 = $(call pkgfiles_lib,libreadline.so.6)
RUNTIME_DEP_PKGS_CSWlibreadline6 += CSWlibncurses5
OBSOLETED_BY_CSWlibreadline6 = CSWreadline

PACKAGES += CSWlibreadline-dev
CATALOGNAME_CSWlibreadline-dev = libreadline_dev
SPKG_DESC_CSWlibreadline-dev = GNU readline development files for libreadline.so.6 and libhistory.so.6
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibreadline-dev += CSWlibhistory6
RUNTIME_DEP_PKGS_CSWlibreadline-dev += CSWlibreadline6

BUILD64_LIBS_ONLY = 1
NORUNPATH = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-curses

include gar/category.mk

post-install-modulated:
	perl -pi -e 's,/usr/local/lib,$(libdir),' \
		$(DESTDIR)/opt/csw/share/readline/rl-fgets.c
	@$(MAKECOOKIE)

LDFLAGS := $(filter-out -xarch=%,$(filter-out -m%,$(LDFLAGS))) -R$(libdir) -lncurses

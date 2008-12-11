GARNAME = readline
GARVERSION = 5.2
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWreadline,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-curses

TEST_TARGET = check

include gar/category.mk

post-install:
	@chmod 555 $(DESTDIR)$(libdir)/libhistory.*
	@chmod 555 $(DESTDIR)$(libdir)/libreadline.*

LDFLAGS := $(filter-out -xarch=%,$(filter-out -m%,$(LDFLAGS)))

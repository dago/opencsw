GARNAME = readline
GARVERSION = 6.0
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 4.3 5.2 6.0

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
DISTFILES  = $(foreach V,$(MODULATIONS_GARVERSION),$(GARNAME)-$(V).tar.gz)

REQUIRED_PKGS = CSWncurses

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

NORUNPATH = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-curses

TEST_TARGET = check

MERGE_SCRIPTS_isa-i386-garversion-4.3 = copy-only
MERGE_DIRS_isa-i386-garversion-4.3 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-4.3 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-4.3 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-5.2 = copy-only
MERGE_DIRS_isa-i386-garversion-5.2 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-5.2 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-5.2 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-6.0 = copy-all
MERGE_SCRIPTS_isa-amd64-garversion-6.0 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-6.0 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-4.3 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-4.3 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-4.3 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-4.3 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-5.2 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-5.2 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-5.2 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-5.2 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-6.0 = copy-all
MERGE_SCRIPTS_isa-sparcv9-garversion-6.0 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-6.0 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

include gar/category.mk

post-install:
	@chmod 555 $(DESTDIR)$(libdir)/libhistory.*
	@chmod 555 $(DESTDIR)$(libdir)/libreadline.*

LDFLAGS := $(filter-out -xarch=%,$(filter-out -m%,$(LDFLAGS))) -R$(libdir) -lncurses

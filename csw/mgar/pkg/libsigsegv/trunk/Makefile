GARNAME = libsigsegv
GARVERSION = 2.8
CATEGORIES = lib
EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 2.6 2.8

DESCRIPTION = A library for catching and handling segmentation faults
define BLURB
  This is a library for handling page faults in user mode. A page fault occurs
  when a program tries to access to a region of memory that is currently not available.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SOURCEFILES = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(GARNAME)-$(VERSION).tar.gz)
DISTFILES = $(SOURCEFILES)
NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz, $(SOURCEFILES))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/libsigsegv/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static

TEST_TARGET = check

MERGE_SCRIPTS_isa-default-garversion-2.6 = copy-only
MERGE_DIRS_isa-default-garversion-2.6 = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-2.6 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-2.6 = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-2.8 = copy-all
MERGE_SCRIPTS_isa-default64-garversion-2.8 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-2.8 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

include gar/category.mk

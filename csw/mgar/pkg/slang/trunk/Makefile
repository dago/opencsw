GARNAME = slang
GARVERSION = 2.2.2
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.4.9 2.2.2

DESCRIPTION = Library primarily to provide an alternative to libcurses
define BLURB
endef

MASTER_SITES = $(foreach V,$(MODULATIONS_GARVERSION),ftp://space.mit.edu/pub/davis/slang/v$(shell echo $V | perl -ne 'print /(\d+\.\d+)/')/)
SOURCEFILES = $(foreach VERSION,$(MODULATIONS_GARVERSION), $(GARNAME)-$(VERSION).tar.gz)
DISTFILES = $(SOURCEFILES)
NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz,$(SOURCEFILES))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWiconv CSWpcrert CSWpng CSWzlib 

SPKG_SOURCEURL = http://www.s-lang.org/

# Setting -L$(libdir) before the newly built lib confuses function
# definitions if the installed lib is older than the newly built one.
LINKER_FLAGS =

sysconfdir = /etc/opt/csw

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET_GARVERSION-1.4.9 =
TEST_TARGET_GARVERSION-2.2.2 = check
TEST_TARGET = $(TEST_TARGET_GARVERSION-$(GARVERSION))

INSTALL_ARGS_GARVERSION-1.4.9 = install-elf install-links
INSTALL_ARGS = $(INSTALL_ARGS_GARVERSION-$(GARVERSION))

MERGE_SCRIPTS_isa-default-garversion-1.4.9 = copy-only
MERGE_DIRS_isa-default-garversion-1.4.9 = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-1.4.9 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-1.4.9 = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-2.2.2 = copy-all
MERGE_SCRIPTS_isa-default64-garversion-2.2.2 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-2.2.2 = $(libdir)

include gar/category.mk


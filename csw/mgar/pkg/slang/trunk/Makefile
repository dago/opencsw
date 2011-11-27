# $Id$

NAME = slang
VERSION = 2.2.4
CATEGORIES = lib

EXTRA_MODULATORS = VERSION
MODULATIONS_VERSION = 1.4.9 2.2.2

# The old package didn't contain 64 bit, so don't bother building it for compat
SKIP_MODULATIONS  = isa-sparcv9-garversion-1.4.9
SKIP_MODULATIONS += isa-amd64-garversion-1.4.9

DESCRIPTION = Library primarily to provide an alternative to libcurses
define BLURB
endef

MASTER_SITES = $(foreach V,$(MODULATIONS_VERSION),ftp://space.mit.edu/pub/davis/slang/v$(shell echo $V | perl -ne 'print /(\d+\.\d+)/')/)
SOURCEFILES = $(foreach VERSION,$(MODULATIONS_VERSION), $(NAME)-$(VERSION).tar.gz)
DISTFILES = $(SOURCEFILES)
NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz,$(SOURCEFILES))

# RUNTIME_DEP_PKGS = CSWiconv CSWpcrert CSWpng CSWzlib CSWoniguruma

SPKG_SOURCEURL = http://www.s-lang.org/

# Setting -L$(libdir) before the newly built lib confuses function
# definitions if the installed lib is older than the newly built one.
LINKER_FLAGS =

UILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET_VERSION-1.4.9 =
TEST_TARGET_VERSION-2.2.2 = check
TEST_TARGET = $(TEST_TARGET_VERSION-$(VERSION))

INSTALL_ARGS_VERSION-1.4.9 = install-elf install-links
INSTALL_ARGS = $(INSTALL_ARGS_VERSION-$(VERSION))

BUILD_ARGS_VERSION-1.4.9 = elf
BUILD_ARGS = $(BUILD_ARGS_VERSION-$(VERSION))

BUILD_OVERRIDE_VARS_VERSION-1.4.9 = ELF_CFLAGS
BUILD_OVERRIDE_VARS = $(BUILD_OVERRIDE_VARS_VERSION-$(VERSION))
BUILD_OVERRIDE_VAR_ELF_CFLAGS = -K pic $(CFLAGS)

MERGE_SCRIPTS_isa-default-garversion-1.4.9 = copy-only
MERGE_DIRS_isa-default-garversion-1.4.9 = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-1.4.9 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-1.4.9 = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-2.2.2 = copy-all
MERGE_SCRIPTS_isa-default64-garversion-2.2.2 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-2.2.2 = $(libdir)

include gar/category.mk

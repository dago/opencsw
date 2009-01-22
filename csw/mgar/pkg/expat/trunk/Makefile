GARNAME = expat
GARVERSION = 2.0.1
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.95.8 2.0.1

DESCRIPTION = XML Parser Toolkit
define BLURB
	This is James Clark's Expat XML parser library in C. It is a stream oriented
	parser that requires setting handlers to deal with the structure that the
	parser discovers in the document.
endef

MASTER_SITES = $(SF_MIRRORS)
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION), $(GARNAME)-$(VERSION).tar.gz)
DISTFILES    = $(SOURCEFILES)
DISTFILES += $(call admfiles,CSWexpat,)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10127
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

# The expat 'check' target tries to compile tests that use GCC
# constructs -- won't compile under Forte without hackery.
TEST_TARGET = check
TEST_SCRIPTS =

ifeq ($(GARVERSION),1.95.8)
INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir libdir includedir man1dir
endif

MERGE_SCRIPTS_isa-i386-garversion-1.95.8 = copy-only
MERGE_DIRS_isa-i386-garversion-1.95.8 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-1.95.8 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-1.95.8 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-2.0.1 = copy-all
MERGE_SCRIPTS_isa-amd64-garversion-2.0.1 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-2.0.1 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-1.95.8 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-1.95.8 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-1.95.8 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-1.95.8 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-2.0.1 = copy-all
MERGE_SCRIPTS_isa-sparcv9-garversion-2.0.1 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-2.0.1 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

include gar/category.mk

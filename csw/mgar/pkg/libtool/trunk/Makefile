GARNAME = libtool
GARVERSION = 2.2.4
CATEGORIES = devel

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.5.26 2.2.4

DESCRIPTION = A generic library support tool
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION), $(GARNAME)-$(VERSION).tar.gz)
DISTFILES    = $(SOURCEFILES)

PACKAGES = CSWlibtool CSWlibtoolrt
CATALOGNAME_CSWlibtoolrt = libtool_rt

SPKG_DESC_CSWlibtool   = A generic library support tool
SPKG_DESC_CSWlibtoolrt = A Generic library support tool runtime libraries

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1
NO_ISAEXEC = 1

SKIPTEST = 1
TEST_TARGET = check

MERGE_SCRIPTS_isa-i386-garversion-1.5.26 = copy-only
MERGE_DIRS_isa-i386-garversion-1.5.26 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-1.5.26 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-1.5.26 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-2.2.4 = copy-all
MERGE_SCRIPTS_isa-amd64-garversion-2.2.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-2.2.4 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-1.5.26 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-1.5.26 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-1.5.26 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-1.5.26 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-2.2.4 = copy-all
MERGE_SCRIPTS_isa-sparcv9-garversion-2.2.4 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-2.2.4 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

PKGFILES_CSWlibtoolrt = $(PKGFILES_RT)

include gar/category.mk


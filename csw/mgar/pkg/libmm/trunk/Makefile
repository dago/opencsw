GARNAME = libmm
GARVERSION = 1.4.2
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.3.1 1.4.2

# No 64 bit for old version as it wasn't provided in the legacy version also
SKIP_MODULATIONS = isa-amd64-garversion-1.3.1
SKIP_MODULATIONS += isa-sparcv9-garversion-1.3.1

DESCRIPTION = Shared Memory Allocation abstraction library
define BLURB
  OSSP mm is a 2-layer abstraction library which simplifies the usage
  of shared memory between forked (and this way strongly related) processes
  under Unix platforms. On the first layer it hides all platform dependent
  implementation details (allocation and locking) when dealing with shared
  memory segments and on the second layer it provides a high-level
  malloc(3)-style API for a convenient and well known way to work with data
  structures inside those shared memory segments.
endef

MASTER_SITES = ftp://ftp.ossp.org/pkg/lib/mm/
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION),mm-$(VERSION).tar.gz)
DISTFILES  = $(SOURCEFILES)

NOEXTRACT = $(filter-out mm-$(GARVERSION).tar.gz,$(SOURCEFILES))

PATCHFILES = 0001-libtool-cflags.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

SPKG_SOURCEURL = http://www.ossp.org/pkg/lib/mm/

DISTNAME = mm-$(GARVERSION)

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_SCRIPTS_isa-i386-garversion-1.3.1 = copy-only
MERGE_DIRS_isa-i386-garversion-1.3.1 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-1.3.1 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-1.3.1 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-1.4.2 = copy-all
MERGE_SCRIPTS_isa-amd64-garversion-1.4.2 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-1.4.2 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-1.3.1 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-1.3.1 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-1.3.1 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-1.3.1 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-1.4.2 = copy-all
MERGE_SCRIPTS_isa-sparcv9-garversion-1.4.2 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-1.4.2 = $(bindir) $(sbindir) $(libexecdir) $(libdir)


include gar/category.mk

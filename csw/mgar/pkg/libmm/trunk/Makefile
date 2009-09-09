GARNAME = libmm
GARVERSION = 1.4.2
CATEGORIES = lib

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
DISTFILES  = mm-$(GARVERSION).tar.gz
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

include gar/category.mk

# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = llvm
VERSION = 2.9
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://llvm.org/releases/$(VERSION)/
DISTFILES  = $(DISTNAME).tgz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-optimized

PATCHFILES += 0001-limits.h-used-for-MAX_PATH.patch

ENABLE_OPTIMIZED = 1
OPTIMIZE_OPTION = -O0
EXTRA_CONFIGURE_EXPORTS  = ENABLE_OPTIMIZED
EXTRA_CONFIGURE_EXPORTS += OPTIMIZE_OPTION
EXTRA_BUILD_EXPORTS  = ENABLE_OPTIMIZED
EXTRA_BUILD_EXPORTS += OPTIMIZE_OPTION
VERBOSE = 1
EXTRA_CONFIGURE_EXPORTS  = VERBOSE
EXTRA_BUILD_EXPORTS  = VERBOSE

include gar/category.mk

# ARCHFLAGS_GCC4_sparcv8 = -m32

# Undefined symbol __sync_fetch_and_add_4
# http://www.mail-archive.com/maintainers@lists.opencsw.org/msg06095.html
# http://opencsw.wikidot.com/porting-faq#toc6
# ifeq ($(ISA),sparcv8)
OPT_FLAGS_GCC = -O0
# endif
# ifeq ($(ISA),i386)
# OPT_FLAGS_GCC =
# endif


# $Id$

NAME = boost
VERSION = 1.55.0
GARTYPE = v2

define BLURB
  Boost was begun by members of the C++ standards committee Library Working
  Group to provide free peer-reviewed portable libraries to the C++ community.
  An additional objective is to establish "existing practice" and provide
  reference implementations so that the Boost libraries are suitable for
  eventual standardization. Indeed, the explicit intent is to propose many of
  these libraries for inclusion in the C++ Standard Library. The Boost Graph
  Library, formerly known as the Generic Graph Component Library (GGCL), is a
  collection of graph algorithms and data structures created in the generic
  programming style of the Standard Template Library (STL).
endef

DESCRIPTION = Free peer-reviewed portable C++ source libraries

MASTER_SITES = $(SF_MIRROR)
DISTVERSION = $(subst .,_,$(VERSION))
DISTNAME = $(NAME)_$(DISTVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# PATCHFILES += 0003-Bug-4757-fix-backported.patch

# It takes an awful lot of time.
NOGITPATCH = 1

# PATCHFILES += 0001-Don-t-try-to-use-fchmodat.patch

# Known problems:
# https://svn.boost.org/trac/boost/ticket/4757
# Proposed fix:
# https://svn.boost.org/trac/boost/changeset/66651

# We define upstream file regex so we can be notifed of new upstream software release
# UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=7586
# UPSTREAM_USE_SF = 1
UPSTREAM_MASTER_SITES = http://www.boost.org/users/history/
UFILES_REGEX = Version (\d+(?:\.\d+)*)


TOOLSET = sun
COMPILER_SUFFIX_PKG =
COMPILER_SUFFIX_CAT =

PACKAGES += CSWboost$(COMPILER_SUFFIX_PKG)-dev
SPKG_DESC_CSWboost$(COMPILER_SUFFIX_PKG)-dev = $(DESCRIPTION), development files
PKGFILES_CSWboost$(COMPILER_SUFFIX_PKG)-dev = $(PKGFILES_DEVEL)

# Empty transitional package
PACKAGES += CSWboostrt
CATALOGNAME_CSWboostrt = boost_rt
SPKG_DESC_CSWboostrt = Empty transitional package
PKGFILES_CSWboostrt = no-files-here
ARCHALL_CSWboostrt = 1

LICENSE = LICENSE_1_0.txt

BUILD_DEP_PKGS += CSWstar

CONFIGURE_SCRIPTS = boost
BUILD_SCRIPTS = boost
INSTALL_SCRIPTS = bjam

BUILD64 = 1

BUILD_ARGS += toolset=$(TOOLSET)
BUILD_ARGS += --prefix=$(DESTDIR)$(prefix)
BUILD_ARGS += --libdir=$(DESTDIR)$(libdir)
BUILD_ARGS += link=shared
BUILD_ARGS += cflags='$(CFLAGS)'
BUILD_ARGS += cxxflags='$(CXXFLAGS)'
BUILD_ARGS += linkflags='$(LDFLAGS) $(LD_OPTIONS)'
# Stop on the first error
BUILD_ARGS += -q
# Display commands as you run them, I want to know what you are doing there
BUILD_ARGS += -d+2
BUILD_ARGS += include='/opt/csw/include'
BUILD_ARGS += --debug-building
BUILD_ARGS += address-model=$(MEMORYMODEL)
# We don't have 64-bit Python
BUILD_ARGS += --without-python

BUILD_ARGS_sparcv8plus = instruction-set=v9
BUILD_ARGS_sparcv9 = instruction-set=v9
BUILD_ARGS += $(BUILD_ARGS_$(ISA))

TEST_SCRIPTS =

JAMDIR_sparc = solarissparc
JAMDIR_i386 = solarisx86
JAMDIR = $(JAMDIR_$(GARCH))

# BUILD64 = 1

# These can't be just passed from Make's PARALLELMFLAGS because of the -l flag.
# BJAM_PARALLELMFLAGS_current9s = -j 32
# BJAM_PARALLELMFLAGS_current9x = -j 5
# BJAM_PARALLELMFLAGS = $(BJAM_PARALLELMFLAGS_$(call modulation2host))

include gar/category.mk

PYTHON_ROOT = $(prefix)
PYTHON_VERSION = 2.6
export PYTHON_ROOT PYTHON_VERSION

# Boost is not extractable with SUNW tar nor GNU tar :-(
tar-bz-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	/opt/csw/bin/star -bz -x -C $(EXTRACTDIR) -f $(DOWNLOADDIR)/$*
	@$(MAKECOOKIE)

configure-boost:
	( cd $(WORKSRC) && \
	  ./bootstrap.sh $(TOOLSET))
	@$(MAKECOOKIE)

build-boost:
	cd $(WORKSRC) && \
		./b2 \
		  -d+2 \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS)
	@$(MAKECOOKIE)

install-bjam:
	cd $(WORKSRC) && \
		./b2 \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS) \
			install
	@$(MAKECOOKIE)

# $Id$

NAME = boost
VERSION = 1.45.0
CATEGORIES = lib

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

MASTER_SITES = $(SF_MIRROR)/$(NAME)/
DISTVERSION = $(subst .,_,$(VERSION))
DISTNAME = $(NAME)_$(DISTVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# Known problems:
# https://svn.boost.org/trac/boost/ticket/4757
# Proposed fix:
# https://svn.boost.org/trac/boost/changeset/66651

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=7586
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# GARCOMPILER = GNU
TOOLSET = sun
COMPILER_SUFFIX_PKG =
COMPILER_SUFFIX_CAT =

PACKAGES += CSWboost$(COMPILER_SUFFIX_PKG)
CATALOGNAME_CSWboost$(COMPILER_SUFFIX_PKG) += boost$(COMPILER_SUFFIX_CAT)
SPKG_DESC_CSWboost$(COMPILER_SUFFIX_PKG) = Boost libraries
# The boost build system is hard to harness.
CHECKPKG_OVERRIDES_CSWboost$(COMPILER_SUFFIX_PKG) += bad-rpath-entry

PACKAGES += CSWboost$(COMPILER_SUFFIX_PKG)devel
CATALOGNAME_CSWboost$(COMPILER_SUFFIX_PKG)devel = boost$(COMPILER_SUFFIX_CAT)_devel
SPKG_DESC_CSWboost$(COMPILER_SUFFIX_PKG)devel = Boost libraries, development files
PKGFILES_CSWboost$(COMPILER_SUFFIX_PKG)devel = $(PKGFILES_DEVEL)

# Empty transitional package
PACKAGES += CSWboostrt
CATALOGNAME_CSWboostrt = boost_rt
SPKG_DESC_CSWboostrt = Empty transitional package
PKGFILES_CSWboostrt = no-files-here
ARCHALL_CSWboostrt = 1

LICENSE = LICENSE_1_0.txt

BUILD_DEP_PKGS += CSWstar
BUILD_DEP_PKGS += CSWboost-jam

CONFIGURE_SCRIPTS = boost
BUILD_SCRIPTS = boost
INSTALL_SCRIPTS = bjam

BUILD_ARGS += toolset=$(TOOLSET)
BUILD_ARGS += --prefix=$(DESTDIR)$(prefix)
BUILD_ARGS += link=shared
BUILD_ARGS += cflags="$(CFLAGS)"
BUILD_ARGS += cxxflags="$(CXXFLAGS)"
BUILD_ARGS += linkflags="$(LDFLAGS) $(LD_OPTIONS)"
# Stop on the first error
BUILD_ARGS += -q
# Display commands as you run them, I want to know what you are doing there
BUILD_ARGS += -d+2

TEST_SCRIPTS =

JAMDIR_sparc = solarissparc
JAMDIR_i386 = solarisx86
JAMDIR = $(JAMDIR_$(GARCH))

# BUILD64_LIBS_ONLY = 1

# These can't be just passed from Make's PARALLELMFLAGS because of the -l flag.
BJAM_PARALLELMFLAGS_current9s = -j 32
BJAM_PARALLELMFLAGS_current9x = -j 5
BJAM_PARALLELMFLAGS = $(BJAM_PARALLELMFLAGS_$(call modulation2host))

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
	cd $(WORKSRC) && ./bootstrap.sh
	@$(MAKECOOKIE)

build-boost:
	cd $(WORKSRC) && \
		./bjam \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS)
	@$(MAKECOOKIE)

install-bjam:
	cd $(WORKSRC) && \
		./bjam \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS) \
			install
	@$(MAKECOOKIE)

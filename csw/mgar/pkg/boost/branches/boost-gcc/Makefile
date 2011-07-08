# $Id$

NAME = boost
VERSION = 1.45.0
GARTYPE = v1
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

prefix = /opt/csw/boost-gcc

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=7586
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

GARCOMPILER = GNU
TOOLSET = gcc
COMPILER_SUFFIX_PKG = -gcc
COMPILER_SUFFIX_CAT = _gcc

PACKAGES += CSWboost$(COMPILER_SUFFIX_PKG)
CATALOGNAME_CSWboost$(COMPILER_SUFFIX_PKG) += boost
SPKG_DESC_CSWboost$(COMPILER_SUFFIX_PKG) = Boost libraries
# The boost build system is hard to harness.
CHECKPKG_OVERRIDES_CSWboost$(COMPILER_SUFFIX_PKG) += bad-rpath-entry

PACKAGES += CSWboost$(COMPILER_SUFFIX_PKG)devel
CATALOGNAME_CSWboost$(COMPILER_SUFFIX_PKG)devel = boost_devel
SPKG_DESC_CSWboost$(COMPILER_SUFFIX_PKG)devel = Boost libraries, development files
PKGFILES_CSWboost$(COMPILER_SUFFIX_PKG)devel = $(PKGFILES_DEVEL)


LICENSE = LICENSE_1_0.txt

BUILD_DEP_PKGS += CSWstar

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = bjam
INSTALL_SCRIPTS = bjam

BUILD_ARGS += toolset=$(TOOLSET)
BUILD_ARGS += --prefix=$(DESTDIR)$(prefix)
BUILD_ARGS += link=shared
BUILD_ARGS += cflags="$(CFLAGS)"
BUILD_ARGS += cxxflags="$(CXXFLAGS)"
BUILD_ARGS += linkflags="$(LDFLAGS) $(LD_OPTIONS)"
# Stop on the first error
BUILD_ARGS += -q
BUILD_ARGS += include="/opt/csw/boost-gcc/include"

TEST_SCRIPTS =

JAMDIR_sparc = solarissparc
JAMDIR_i386 = solarisx86
JAMDIR = $(JAMDIR_$(GARCH))

# BUILD64 = 1

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

pre-configure-modulated:
	( cd $(WORKSRC)/tools/jam/src && \
	  ./build.sh $(TOOLSET) && \
	  mkdir -p $(DESTDIR)$(bindir) && \
	  cp bin.$(JAMDIR)/bjam $(DESTDIR)$(bindir) )
	@$(MAKECOOKIE)

build-bjam:
	cd $(WORKSRC) && \
		$(DESTDIR)$(bindir)/bjam \
		  -d+2 \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS)
	@$(MAKECOOKIE)

install-bjam:
	cd $(WORKSRC) && \
		$(DESTDIR)$(bindir)/bjam \
		  -d+2 \
			$(BJAM_PARALLELMFLAGS) \
			$(BUILD_ARGS) \
			install
	@$(MAKECOOKIE)

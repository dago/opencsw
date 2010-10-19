GARNAME = boost
GARVERSION = 1.44.0
CATEGORIES = lib

DESCRIPTION = A collection of C++ libraries
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

MASTER_SITES = $(SF_MIRROR)/$(GARNAME)/
DISTVERSION = $(subst .,_,$(GARVERSION))
DISTNAME = $(GARNAME)_$(DISTVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=7586
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PACKAGES = CSWboost
CATALOGNAME_CSWboost = boost

LICENSE = LICENSE_1_0.txt

BUILD_DEP_PKGS += CSWstar

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = bjam

BUILD_ARGS  = --prefix=$(DESTDIR)$(prefix)
BUILD_ARGS += toolset=sun
#BUILD_ARGS += --with-python-root=$(prefix)

TEST_SCRIPTS =

JAMDIR_sparc = solarissparc
JAMDIR_i386 = solarisx86
JAMDIR = $(JAMDIR_$(GARCH))

include gar/category.mk

PYTHON_ROOT = $(prefix)
PYTHON_VERSION = 2.3
export PYTHON_ROOT PYTHON_VERSION

# Boost is not extractable with SUNW tar nor GNU tar :-(
tar-bz-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	/opt/csw/bin/star -bz -x -C $(EXTRACTDIR) -f $(DOWNLOADDIR)/$*
	@$(MAKECOOKIE)

pre-configure-modulated:
	( cd $(WORKSRC)/tools/jam/src ; \
	  ./build.sh sunpro ; \
	  mkdir -p $(DESTDIR)$(bindir) ; \
	  mv bin.$(JAMDIR)/bjam $(DESTDIR)$(bindir) )
	@$(MAKECOOKIE)

install-bjam:
	( cd $(WORKSRC) ; which bjam; bjam $(BUILD_ARGS) install ) || exit 1
	@$(MAKECOOKIE)

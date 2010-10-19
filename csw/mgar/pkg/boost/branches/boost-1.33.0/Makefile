GARNAME = boost
GARVERSION = 1.33.0
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
DISTFILES  = $(GARNAME)_$(DISTVERSION).tar.bz2
DISTFILES += CSWboost.gspec

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=7586
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

WORKSRC = $(WORKDIR)/$(GARNAME)_$(DISTVERSION)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = bjam

BUILD_ARGS  = --prefix=$(DESTDIR)$(prefix)
BUILD_ARGS += -sTOOLS=sunpro
BUILD_ARGS += --with-python-root=$(prefix)

TEST_SCRIPTS =

include gar/category.mk

PYTHON_ROOT = $(prefix)
PYTHON_VERSION = 2.3
export PYTHON_ROOT PYTHON_VERSION

pre-configure:
	( cd $(WORKSRC)/tools/build/jam_src ; \
	  ./build.sh sunpro ; \
	  mkdir -p $(DESTDIR)$(bindir) ; \
	  mv bin.solaris/bjam $(DESTDIR)$(bindir) )
	@$(MAKECOOKIE)

install-bjam:
	( cd $(WORKSRC) ; bjam $(BUILD_ARGS) install ) || exit 1
	@$(MAKECOOKIE)

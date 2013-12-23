# NOTE: Autotools build depreciated switching to cmake.
# NOTE: cmake finds boost library but "mgar build" step can't find boost 
#	headers and setting EXTRA_INC or EXTRA_CPPFLAGS doesn't help.
NAME = wesnoth
VERSION = 1.10.7
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A free turn-based strategy game with a fanasy theme
define BLURB
  Build up a great army, gradually turning raw recruits into hardened veterans. In later games, recall your toughest warriors and form a deadly host against whom none can stand! Choose units from a large pool of specialists, and hand-pick a force with the right strengths to fight well on different terrains against all manner of opposition.  
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89495
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

NOGITPATCH = 1

EXTRA_INC = /opt/csw/gxx/include

GARCOMPILER = GNU

TEST_SCRIPTS =

CONFIGUREBUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk

# Autotools build depreciated now using cmake
configure-custom:
	mkdir $(WORKSRC)/build
	cd $(WORKSRC)/build && \
	CMAKE_INCLUDE_PATH=/opt/csw/gxx/include:/opt/csw/include \
	CMAKE_LIBRARY_PATH=/opt/csw/gxx/lib:/opt/csw/lib \
	CC=gcc CXX=g++ \
	/opt/csw/bin/cmake \
	-DCMAKE_INSTALL_PREFIX=/opt/csw \
	-DCMAKE_VERBOSE_MAKEFILE=TRUE \
	-DCMAKE_CPP_FLAGS=-I/opt/csw/gxx/include \
	-DBoost_INCLUDE_DIR=/opt/csw/gxx/include ..
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

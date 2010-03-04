GARNAME = wesnoth
GARVERSION = 1.4.7
CATEGORIES = apps

DESCRIPTION = a free turn-based strategy game with a fanasy theme
define BLURB
  Build up a great army, gradually turning raw recruits into hardened veterans. In later games, recall your toughest warriors and form a deadly host against whom none can stand! Choose units from a large pool of specialists, and hand-pick a force with the right strengths to fight well on different terrains against all manner of opposition.  
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += Makefile.fixed

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89495
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

PATCHFILES = language.cpp.diff
PATCHFILES += configure.patch
PATCHFILES += simple_wml.cpp.patch
PATCHFILES += global.hpp.patch

RUNTIME_DEP_PKGS_CSWwesnoth = CSWboostrt
RUNTIME_DEP_PKGS_CSWwesnoth += CSWftype2
RUNTIME_DEP_PKGS_CSWwesnoth += CSWggettextrt
RUNTIME_DEP_PKGS_CSWwesnoth += CSWlibsdl
RUNTIME_DEP_PKGS_CSWwesnoth += CSWpng
RUNTIME_DEP_PKGS_CSWwesnoth += CSWpython
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlimage
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlmixer
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlnet
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsdlttf
RUNTIME_DEP_PKGS_CSWwesnoth += CSWstlport
RUNTIME_DEP_PKGS_CSWwesnoth += CSWsunmath
RUNTIME_DEP_PKGS_CSWwesnoth += CSWzlib

CHECKPKG_OVERRIDES_CSWwesnoth += symbol-not-found|campaignd
CHECKPKG_OVERRIDES_CSWwesnoth += symbol-not-found|exploder
CHECKPKG_OVERRIDES_CSWwesnoth += symbol-not-found|cutter
CHECKPKG_OVERRIDES_CSWwesnoth += symbol-not-found|wesnoth_editor
CHECKPKG_OVERRIDES_CSWwesnoth += symbol-not-found|wesnoth
CHECKPKG_OVERRIDES_CSWwesnoth += symbol-not-found|wesnothd

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += CXXFLAGS='-features=extensions -library=stlport4'
CONFIGURE_ARGS += LDFLAGS='-L. -L/opt/csw/lib -lstlport -lintl -lsocket -lboost_iostreams -lsunmath -lSDL_ttf'
CONFIGURE_ARGS += --with-fifodir=/var/opt/csw/run
CONFIGURE_ARGS += --enable-server
CONFIGURE_ARGS += --enable-campaign-server
CONFIGURE_ARGS += --enable-tools
CONFIGURE_ARGS += --enable-editor
CONFIGURE_ARGS += --with-boost=/opt/csw

TEST_SCRIPTS =

include gar/category.mk

post-configure-modulated:
	-cp $(FILEDIR)/Makefile.fixed $(WORKSRC)/src/Makefile
	$(MAKECOOKIE)

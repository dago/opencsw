GARNAME = wesnoth
GARVERSION = 1.4.7
CATEGORIES = apps

DESCRIPTION = a free turn-based strategy game with a fanasy theme
define BLURB
  Build up a great army, gradually turning raw recruits into hardened veterans. In later games, recall your toughest warriors and form a deadly host against whom none can stand! Choose units from a large pool of specialists, and hand-pick a force with the right strengths to fight well on different terrains against all manner of opposition.  
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWwesnoth, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89495
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

GARCOMPILER ?= SUN

PATCHFILES = language.cpp.diff

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += CXXFLAGS='-features=extensions -library=stlport4'
CONFIGURE_ARGS += LDFLAGS='-L. -L/opt/csw/lib -lstlport -lintl -lsocket -lboost_iostreams -lsunmath -lSDL_ttf'
CONFIGURE_ARGS += --with-fifodir=/var/opt/csw/run/wesnothd
#CONFIGURE_ARGS += --enable-server
#CONFIGURE_ARGS += --enable-campaign-server
#CONFIGURE_ARGS += --enable-tools
#CONFIGURE_ARGS += --enable-editor
CONFIGURE_ARGS += --with-boost=/opt/csw

TEST_SCRIPTS =

include gar/category.mk

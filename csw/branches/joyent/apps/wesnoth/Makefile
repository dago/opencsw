GARNAME = wesnoth
GARVERSION = 1.0.2
CATEGORIES = apps

DESCRIPTION = a free turn-based strategy game with a fanasy theme
define BLURB
  Build up a great army, gradually turning raw recruits into hardened veterans. In later games, recall your toughest warriors and form a deadly host against whom none can stand! Choose units from a large pool of specialists, and hand-pick a force with the right strengths to fight well on different terrains against all manner of opposition.  
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWwesnoth,)

GARCOMPILER ?= GNU

PATCHFILES = language.cpp.diff

CONFIGURE_ARGS = --prefix=$(prefix) LDFLAGS='-lsunmath -lintl'
CONFIGURE_ARGS += LD_OPTIONS=-L/opt/csw/lib
#CONFIGURE_ARGS += --with-server-uid=60001
#CONFIGURE_ARGS += --with-server-gid=60001
CONFIGURE_ARGS += --disable-nls
#CONFIGURE_ARGS += --enable-server
#CONFIGURE_ARGS += --enable-campaign-server
CONFIGURE_ARGS += --enable-tools
CONFIGURE_ARGS += --enable-editor
CONFIGURE_ARGS += --with-kde
CONFIGURE_ARGS += --with-gnome

ENABLE_TEST = 0

include ../category.mk

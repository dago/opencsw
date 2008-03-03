GARNAME = wesnoth
GARVERSION = 1.2.5
CATEGORIES = apps

DESCRIPTION = a free turn-based strategy game with a fanasy theme
define BLURB
  Build up a great army, gradually turning raw recruits into hardened veterans. In later games, recall your toughest warriors and form a deadly host against whom none can stand! Choose units from a large pool of specialists, and hand-pick a force with the right strengths to fight well on different terrains against all manner of opposition.  
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWwesnoth, depend )

GARCOMPILER ?= GNU

PATCHFILES = language.cpp.diff

CONFIGURE_ARGS = --prefix=$(prefix) --mandir=/opt/csw/share/man LDFLAGS='-lsunmath -lintl'
CONFIGURE_ARGS += LD_OPTIONS=-L/opt/csw/lib
CONFIGURE_ARGS += --with-server-uid=60001
CONFIGURE_ARGS += --with-server-gid=60001
CONFIGURE_ARGS += --disable-nls
CONFIGURE_ARGS += --enable-server
CONFIGURE_ARGS += --enable-campaign-server
CONFIGURE_ARGS += --enable-tools
CONFIGURE_ARGS += --enable-editor
CONFIGURE_ARGS += --with-kde
CONFIGURE_ARGS += --with-gnome

TEST_SCRIPTS =

include gar/category.mk

#pre-configure:
#	( cd $(WORKSRC) ; aclocal ; autoconf ; automake -a )
#	@$(MAKECOOKIE)

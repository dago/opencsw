NAME = xpilot
VERSION = 4.5.5
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = multi-player 2D space game
define BLURB
  XPilot is a multi-player 2D space game for both local and Internet gaming. Some features are borrowed from classics like the Atari coin-ups Asteroids and Gravitar, and the home-computer games Thrust and Gravity Force, but XPilot has many new aspects too.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PATCHFILES = query.c.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*ECT).tar.gz

SF_PROJ = project/xpilotgame/xpilot-4/xpilot-4.5.5
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=14558
UPSTREAM_USE_SF = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract-modulated:
	-cp $(FILEDIR)/Makefile.std $(WORKSRC)/src/Makefile
	$(MAKECOOKIE)

build-custom:
	-cd $(WORKSRC)/src && make solaris
	$(MAKECOOKIE)

install-custom:
	-cd $(WORKSRC)/src && make install-solari
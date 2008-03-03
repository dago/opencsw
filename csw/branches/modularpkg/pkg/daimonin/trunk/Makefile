GARNAME = daimonin
GARVERSION = 
CATEGORIES = apps

DESCRIPTION = FREE online role playing game (MMORPG)
define BLURB
daimonin is a free open source Massively Multiplayer On-line Role-playing Game (MMORPG) under the GPL license.
endef

MASTER_SITES = http://heanet.dl.sourceforge.net/sourceforge/daimonin/
DISTFILES  = $(GARNAME)_client-BETA3-0967.tar.gz
DISTFILES += $(call admfiles,CSWdaimonin,)

GARCOMPILER = GNU

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	( chmod +x $(WORKDIR)/daimonin/client/make/linux/configure )
	( cd $(WORKDIR)/daimonin/client/make/linux ; ./configure )
	@$(MAKECOOKIE)

build-custom:
	( cd $(WORKDIR)/daimonin/client/make/linux ; LD_OPTIONS='-lsocket -lnsl' make )
	@$(MAKECOOKIE)

install-custom:
	( cd $(WORKDIR)/daimonin/client/make/linux ; make install )
	@$(MAKECOOKIE)

GARNAME = eggdbus
GARVERSION = 0.6
CATEGORIES = lib

DESCRIPTION = EggDbus
define BLURB
endef

MASTER_SITES = http://cgit.freedesktop.org/~david/eggdbus/snapshot/
#DISTNAME  = PolicyKit-$(GARVERSION)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWeggdbus CSWeggdbusdevel
CATALOGNAME_CSWeggdbus = eggdbus
CATALOGNAME_CSWeggdbusdevel = eggdbus_devel
SPKG_DESC_CSWeggdbus = eggdbus is an implementation of XMP
SPKG_DESC_CSWeggdbusdevel = eggdbus is an implementation of XMP - developer package

#REQUIRED_PKGS_CSWeggdbus += CSWexpat CSWstlport CSWzlib CSWiconv
#REQUIRED_PKGS_CSWeggdbusdevel += CSWeggdbus

#PREREQUISITE_PKGS += $(REQUIRED_PKGS_CSWeggdbus)

PKGFILES_CSWeggdbusdevel = $(PKGFILES_DEVEL)

SPKG_SOURCEURL = http://cgit.freedesktop.org/~david/eggdbus

#CONFIGURE_SCRIPTS += $(WORKSRC)/autogen.sh
#CONFIGURE_SCRIPTS += $(WORKSRC)/configure

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@( cd $(WORKSRC) ; ./autogen.sh )
	@$(MAKECOOKIE)

#pre-configure-modulated:
#	@echo " ==> Regenerating build tools..."
#	@(cd $(WORKSRC) ; \
#		aclocal                       && \
#		autoconf                      && \
#		libtoolize --automake --force && \
#		aclocal                       && \
#		automake -a )
#	@$(MAKECOOKIE)

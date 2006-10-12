GARNAME = ogle
GARVERSION = 0.9.2
CATEGORIES = apps

DESCRIPTION = opensource DVD player with DVD menu support
define BLURB
  opensource DVD player with DVD menu support
endef

MASTER_SITES = http://www.dtek.chalmers.se/groups/dvd/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWogle, depend )

#PATCHFILES = configure.in.diff

CONFIGURE_ARGS = $(DIRPATHS) --disable-mmx
CONFIGURE_ARGS += --with-libmlib=/export/home/jgoerzen/MediaLib

TEST_SCRIPTS =

include ../category.mk

# Cannot do this yet (libtool problems)
#pre-configure:
#	( cd $(WORKSRC) ; ./autogen.sh )
#	@$(MAKECOOKIE)

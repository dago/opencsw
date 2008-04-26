GARNAME = povray
GARVERSION = 3.6
CATEGORIES = apps

DESCRIPTION = povray
define BLURB
endef

MASTER_SITES = http://www.povray.org/redirect/www.povray.org/ftp/pub/povray/Official/Unix/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWpovray,depend)

#PREREQUISITE_PKGS = CSWncurses CSWggettext

WORKSRC = $(WORKDIR)/$(GARNAME)-3.6.1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include ../category.mk

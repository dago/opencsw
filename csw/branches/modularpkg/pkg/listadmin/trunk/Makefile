GARNAME = listadmin
GARVERSION = 2.37
CATEGORIES = apps

DESCRIPTION = Command line utility for processing the moderator queue on Mailman lists

MASTER_SITES = http://heim.ifi.uio.no/kjetilho/hacks
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlistadmin,)

PATCHFILES = gar-base.diff

# This package doesn't use ./configure
CONFIGURE_SCRIPTS =

TEST_TARGET =

include gar/category.mk

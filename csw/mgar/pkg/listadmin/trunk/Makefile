NAME = listadmin
VERSION = 2.37
GARTYPE = v1
CATEGORIES = apps

DESCRIPTION = Command line utility for processing the moderator queue on Mailman lists

MASTER_SITES = http://heim.ifi.uio.no/kjetilho/hacks
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWlistadmin,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = gar-base.diff

# This package doesn't use ./configure
CONFIGURE_SCRIPTS =

TEST_TARGET =

include gar/category.mk

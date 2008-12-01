GARNAME = ksh
GARVERSION = 93
CATEGORIES = devel

DESCRIPTION = The KornShell Command and Programming Language
define BLURB
  The KornShell language was designed and developed by David G. Korn at AT&T
  Bell Laboratories. It is an interactive command language that provides
  access to the UNIX system and to many other systems, on the many different
  computers and workstations on which it is implemented.
endef

# Main archive location
MASTER_SITES =
#DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWksh,)

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


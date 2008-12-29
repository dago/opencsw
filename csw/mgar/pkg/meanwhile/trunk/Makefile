GARNAME = meanwhile
GARVERSION = 1.0.2
CATEGORIES = lib

#Need to use either gcc or studio 12 with -features=extensions
GARCOMPILER = GNU

DESCRIPTION = Open implementation of the lotus sametime community client
define BLURB
  The Meanwhile project is an open implementation of the Lotus Sametime client protocol. The project provides a library written in C, a python module, and a Gaim plugin utilizing the library.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmeanwhile,depend prototype)
PATCHFILES += ft_fix.patch
PATCHFILES += presence_fix_v2.patch
PATCHFILES += status_timestamp_workaround.patch
PATCHFILES += doc_dir.patch

#No tests
TEST_SCRIPTS =

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

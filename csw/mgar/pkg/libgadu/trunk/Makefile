GARNAME = libgadu
GARVERSION = 1.8.2
CATEGORIES = lib
SPKG_SOURCEURL = http://toxygen.net/libgadu

#Need to use either gcc or studio 12 with -features=extensions
GARCOMPILER = GNU

DESCRIPTION = Gadu-Gadu protocol implementation library

MASTER_SITES = http://toxygen.net/libgadu/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibgadu,depend prototype)

#No tests
TEST_SCRIPTS =

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

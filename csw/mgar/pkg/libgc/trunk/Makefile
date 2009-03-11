GARNAME = libgc
GARVERSION = 7.0
CATEGORIES = lib

DESCRIPTION = A garbage collector for C and C++
define BLURB
	The Boehm-Demers-Weiser conservative garbage collector can be used as a
	garbage collecting replacement for C malloc or C++ new. It allows you to
	allocate memory basically as you normally would, without explicitly
	deallocating memory that is no longer useful. The collector automatically
	recycles memory when it determines that it can no longer be otherwise
	accessed.
endef

MASTER_SITES = http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/
DISTFILES  = gc-$(GARVERSION).tar.gz

DISTNAME = gc-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

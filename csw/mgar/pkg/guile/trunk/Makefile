# 2009-11-15: The package builds successfully with GCC (not with sun cc).
#             The version in the catalog (1.6.7,REV=2005.07.03) includes the .a 
#             and .la files only, this package include the .so files only. I'm 
#             not quite sure what's the correct approach here.
#             The existing Makefile included the libraries under files/
#                                                                  - Trygve

GARNAME = guile
GARVERSION = 1.8.7
CATEGORIES = lib

DESCRIPTION = GNU extensibility library
define BLURB
	Guile is a library designed to help programmers create flexible applications. Using Guile in an application allows programmers to write plug-ins, or modules (there are many names, but the concept is essentially the same) and users to use them to have an application fit their needs. 
endef

SPKG_DESC_CSWguilelib12 = GNU extensibility library (shared libraries)

# There has to be something wrong when a package depends on *both* gcc3 and gcc4 - trygve
REQUIRED_PKGS  = CSWgcc3core
REQUIRED_PKGS += CSWgcc3corert
REQUIRED_PKGS += CSWgcc4corert
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWlibgmp
REQUIRED_PKGS += CSWlibtoolrt
REQUIRED_PKGS += CSWncurses
REQUIRED_PKGS += CSWreadline

MASTER_SITES = ftp://ftp.gnu.org/pub/gnu/guile/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-error-on-warning=no

TEST_SCRIPTS =
BUILD_64BIT = yes

include gar/category.mk

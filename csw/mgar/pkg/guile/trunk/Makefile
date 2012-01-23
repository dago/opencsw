# 2009-11-15: The package builds successfully with GCC (not with sun cc).
#             The version in the catalog (1.6.7,REV=2005.07.03) includes the .a 
#             and .la files only, this package include the .so files only. I'm 
#             not quite sure what's the correct approach here.
#             The existing Makefile included the libraries under files/
#                                                                  - Trygve

NAME = guile
VERSION = 1.8.7
CATEGORIES = lib

DESCRIPTION = GNU extensibility library
define BLURB
	Guile is a library designed to help programmers create flexible applications. Using Guile in an application allows programmers to write plug-ins, or modules (there are many names, but the concept is essentially the same) and users to use them to have an application fit their needs. 
endef

SPKG_DESC_CSWguilelib12 = GNU extensibility library (shared libraries)

RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWlibgmp
RUNTIME_DEP_PKGS += CSWlibtoolrt
RUNTIME_DEP_PKGS += CSWncurses
RUNTIME_DEP_PKGS += CSWreadline

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS  = $(DIRPATHS) 
CONFIGURE_ARGS += --enable-error-on-warning=no

TEST_SCRIPTS =

include gar/category.mk

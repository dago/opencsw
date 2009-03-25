GARNAME      = gcc
GARVERSION   = 4.3.3
CATEGORIES   = lang

DESCRIPTION  = The GNU Compiler Collection
define BLURB
	The GNU Compiler Collection includes front ends for C, C++, 
	Objective-C, Fortran, Java, and Ada, as well as libraries 
	for these languages (libstdc++, libgcj,...).
endef

DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2
MASTER_SITES = $(GNU_MIRROR)/$(GARNAME)-$(GARVERSION)/

# We define upstream file regex so we can be notifed 
# of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

## For cleanliness I split the Configuration into separate files
include files/gar_override.mk
include files/configure_def.mk  
include files/pkg_scripts.mk
include files/package_def.mk
include files/amd_merge.mk
## include mGar definitions
include gar/category.mk

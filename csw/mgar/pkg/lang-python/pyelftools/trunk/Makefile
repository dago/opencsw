# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pyelftools
VERSION = 0.21
GARTYPE = v2

DESCRIPTION = Library for analyzing ELF files and DWARF debugging information
define BLURB
endef

CATEGORIES = python
DISTFILES  = $(DISTNAME).tar.gz

# Since elftools are used for checkpkg, they need to be built for all
# platforms on which we're building.
PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PATCHFILES += 0001-syminfo+symbol_versioning_support.patch
PATCHFILES += 0002-Correctly-handle-the-multiple-string-tables-case-for.patch

TEST_SCRIPTS =

ARCHALL_CSWpy-pyelftools = 1

include gar/category.mk


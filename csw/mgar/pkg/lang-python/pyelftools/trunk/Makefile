# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pyelftools
# In 0.23 minimal Python support is raised to 2.7, stick at 0.22 until checkpkg is updated to use 2.7
VERSION = 0.22
GARTYPE = v2

DESCRIPTION = Library for analyzing ELF files and DWARF debugging information

CATEGORIES = python
DISTFILES  = $(DISTNAME).tar.gz

# Since elftools are used for checkpkg, they need to be built for all
# platforms on which we're building.
PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

TEST_SCRIPTS =

ARCHALL_CSWpy-pyelftools = 1

include gar/category.mk


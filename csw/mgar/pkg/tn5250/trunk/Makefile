# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tn5250
VERSION = 0.17.4
GARTYPE = v2
CATEGORIES = net

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

DESCRIPTION = A tn5250 emulator
define BLURB
tn5250 is a telnet client for the IBM iSeries and AS/400 that emulates 5250 terminals and printers. This function is the same as that provided by the 5250 emulator in IBM iSeries Access.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Ensure-we-have-FIONBIO-defined.patch

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


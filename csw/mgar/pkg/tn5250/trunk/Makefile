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

PACKAGES += CSWtn5250
SPKG_DESC_CSWtn5250 = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWtn5250 += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWtn5250 += CSWlib5250-0
RUNTIME_DEP_PKGS_CSWtn5250 += CSWlibssl1-0-0

PACKAGES += CSWlib5250-0
SPKG_DESC_CSWlib5250-0 += $(DESCRIPTION), lib5250.so.0
PKGFILES_CSWlib5250-0 += $(call baseisadirs,$(libdir),lib5250\.so\.0\.0\.0)
PKGFILES_CSWlib5250-0 += $(call baseisadirs,$(libdir),lib5250\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlib5250-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlib5250-0 += CSWlibssl1-0-0

PACKAGES += CSWtn5250-dev
SPKG_DESC_CSWtn5250-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWtn5250-dev += CSWlib5250-0
PKGFILES_CSWtn5250-dev += $(PKGFILES_DEVEL)

EXTRA_INC += $(includedir)/ncurses

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


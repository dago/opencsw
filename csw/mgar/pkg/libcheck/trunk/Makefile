# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME    = check
VERSION = 0.9.14
GARTYPE = v2

DESCRIPTION = A unit test framework for C

define BLURB
  Check is a unit testing framework for C. It features a simple interface for
  defining unit tests, putting little in the way of the developer. Tests are
  run in a separate address space, so both assertion failures and code errors
  that cause segmentation faults or other signals can be caught. Test results
  are reportable in the following: Subunit, TAP, XML, and a generic logging
  format. 
endef

VENDOR_URL = http://check.sourceforge.net/

MASTER_SITES = $(SF_MIRROR)
DISTFILES    = $(DISTNAME).tar.gz

LICENSE      = COPYING.LESSER

GARCOMPILER  = GNU

PACKAGES += CSWlibcheck0
SPKG_DESC_CSWlibcheck0 = A unit test framework for C, libcheck.so.0
PKGFILES_CSWlibcheck0 += $(call pkgfiles_lib,libcheck.so.0)
RUNTIME_DEP_PKGS_CSWlibcheck0 += CSWlibgcc-s1

PACKAGES += CSWlibcheck-dev
SPKG_DESC_CSWlibcheck-dev = Development files for libckeck.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibcheck-dev += CSWlibcheck0

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)

OUR_PATH = /usr/xpg6/bin:/usr/xpg4/bin:/usr/ccs/bin:/usr/bin:/sbin:/usr/sbin:/opt/csw/bin:$(PATH)

CONFIGURE_ENV_PATH = $(OUR_PATH)
BUILD_ENV_PATH     = $(OUR_PATH)
TEST_ENV_PATH      = $(OUR_PATH)
INSTALL_ENV_PATH   = $(OUR_PATH)

include gar/category.mk

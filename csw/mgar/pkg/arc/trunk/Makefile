# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = arc
VERSION = 5.21p
GARTYPE = v2

DESCRIPTION = Based on the MSDOS ARC program

VENDOR_URL = http://sourceforge.net/projects/arc/

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_TARGET =

PATCHFILES = 0001-Adjust-Makefile-to-accept-common-env-variables.patch

GARCOMPILER = GNU

EXTRA_CFLAGS = -DSYSV=1 -DNEED_ALPHASORT
EXTRA_INC = /usr/ucbinclude
EXTRA_LIB = /usr/ucblib
EXTRA_LINKER_FLAGS = -lucb

include gar/category.mk

build-custom:
	(cd $(WORKSRC); gmake $(BUILD_ENV) $(PARALLELMFLAGS))
	@$(MAKECOOKIE)

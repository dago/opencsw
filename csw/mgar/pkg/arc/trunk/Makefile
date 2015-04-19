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
PATCHFILES += 0002-Use-ginstall.patch

GARCOMPILER = GNU

EXTRA_CFLAGS_5.9 = -DNEED_ALPHASORT
EXTRA_CFLAGS = -DSYSV=1 $(EXTRA_CFLAGS_$(GAROSREL))
EXTRA_INC = /usr/ucbinclude
EXTRA_LIB = /usr/ucblib
EXTRA_LINKER_FLAGS = -lucb

# It can be investigated; there's something wrong with escaping:
# /usr/ucblib/SALIST
# It would only be a problem if we were building a 64-bit binary, but we
# aren't.
CHECKPKG_OVERRIDES_CSWarc += bad-rpath-entry

include gar/category.mk

build-custom:
	(cd $(WORKSRC); gmake $(BUILD_ENV) $(PARALLELMFLAGS))
	@$(MAKECOOKIE)

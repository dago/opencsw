# $Id: Makefile 24861 2015-04-19 14:26:11Z wahwah $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = isaexec
VERSION = 0.3
GARTYPE = v2

DESCRIPTION = Find and execute an architecture-optimized binary

VENDOR_URL = http://www.opencsw.org

MASTER_SITES =
DISTFILES  = csw-isaexec.c Makefile

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_TARGET =

GARCOMPILER = GNU

MKPACKAGE_ARGS = --nocompress

include gar/category.mk

pre-configure:
	cp $(WORKDIR)/Makefile $(WORKSRC)
	cp $(WORKDIR)/csw-isaexec.c $(WORKSRC)
	@$(MAKECOOKIE)

build-custom:
	(cd $(WORKSRC); gmake $(BUILD_ENV) $(PARALLELMFLAGS))
	@$(MAKECOOKIE)

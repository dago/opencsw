# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME       = Mojo-IOLoop-ForkCall
VERSION    = 0.12
GARTYPE    = v2
CATEGORIES = cpan
AUTHOR     = JBERGER

DESCRIPTION = Run blocking functions asynchronously by forking
define BLURB
  Asynchronous programming can be benefitial for performance, however not all functions are written for nonblocking interaction and external processes almost never are. Still, all is not lost.
endef


PACKAGES    = CSWpm-mojo-ioloop-forkcall
CATALOGNAME = pm_mojo-ioloop-forkcall
SPKG_DESC_CSWpm-mojo-ioloop-forkcall = $(DESCRIPTION)

ARCHALL = 1

BUILD_DEP_PKGS += CSWpm-module-build
BUILD_DEP_PKGS += CSWpm-module-metadata
BUILD_DEP_PKGS += CSWpm-io-pipely

RUNTIME_DEP_PKGS_CSWpm-mojo-ioloop-forkcall += CSWpm-module-build
CHECKPKG_OVERRIDES_CSWpm-mojo-ioloop-forkcall += surplus-dependency|CSWpm-module-build
RUNTIME_DEP_PKGS_CSWpm-mojo-ioloop-forkcall += CSWpm-module-metadata
CHECKPKG_OVERRIDES_CSWpm-mojo-ioloop-forkcall += surplus-dependency|CSWpm-module-metadata
RUNTIME_DEP_PKGS_CSWpm-mojo-ioloop-forkcall += CSWpm-io-pipely
CHECKPKG_OVERRIDES_CSWpm-mojo-ioloop-forkcall += surplus-dependency|CSWpm-io-pipely

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk


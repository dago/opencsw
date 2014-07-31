# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME       = IO-Pipely
VERSION    = 0.005
GARTYPE    = v2
CATEGORIES = cpan
AUTHOR     = RCAPUTO

DESCRIPTION = Portably create pipe() or pipe-like handles, one way or another.
define BLURB
endef

PACKAGES = CSWpm-io-pipely
CATALOGNAME = pm_io_pipely
SPKG_DESC_CSWpm-io-pipely = $(DESCRIPTION)

BUILD_DEP_PKGS += CSWpm-test-simple

RUNTIME_DEP_PKGS_CSWpm-io-pipely += CSWpm-test-simple

ARCHALL = 1

include gar/category.mk


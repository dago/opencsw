# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = PPIx-Utilities
VERSION = 1.001000
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = ELLIOTJS

DESCRIPTION = Extensions to PPI
define BLURB
  Extensions to PPI
endef

PACKAGES = CSWpm-ppix-utilities
CATALOGNAME = pm_ppix_utilities
ARCHALL = 1

LICENSE = LICENSE

RUNTIME_DEP_PKGS += CSWpmreadonly
RUNTIME_DEP_PKGS += CSWpm-test-deep
RUNTIME_DEP_PKGS += CSWpm-module-build
RUNTIME_DEP_PKGS += CSWpm-exception-class

# Unreleased packages, remove next time
CHECKPKG_OVERRIDES_CSWpm-ppix-utilities += unidentified-dependency|CSWpm-exception-class
CHECKPKG_OVERRIDES_CSWpm-ppix-utilities += unidentified-dependency|CSWpm-module-build

include gar/category.mk


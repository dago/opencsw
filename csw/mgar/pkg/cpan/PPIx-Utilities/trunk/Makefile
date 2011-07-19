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

RUNTIME_DEP_PKGS += CSWpm-ppi
RUNTIME_DEP_PKGS += CSWpmexceptcls
RUNTIME_DEP_PKGS += CSWpmreadonly
RUNTIME_DEP_PKGS += CSWpmtaskweaken

# Unreleased packages, remove next time
CHECKPKG_OVERRIDES_CSWpm-ppix-utilities += unidentified-dependency|CSWpm-ppi

include gar/category.mk


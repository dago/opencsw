NAME = CHI
VERSION = 0.55
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = JSWARTZ

DESCRIPTION = Unified cache handling interface
define BLURB
  Unified cache handling interface
endef

LICENSE = LICENSE

PACKAGES = CSWpm-chi
CATALOGNAME = pm_chi
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-list-moreutils
RUNTIME_DEP_PKGS += CSWpm-moose
RUNTIME_DEP_PKGS += CSWpm-time-duration
RUNTIME_DEP_PKGS += CSWpm-time-duration-parse
RUNTIME_DEP_PKGS += CSWpm-try-tiny
RUNTIME_DEP_PKGS += CSWpmlogany

# Remove on next build
CHECKPKG_OVERRIDES_CSWpm-chi += unidentified-dependency|CSWpm-moose
CHECKPKG_OVERRIDES_CSWpm-chi += unidentified-dependency|CSWpm-time-duration
CHECKPKG_OVERRIDES_CSWpm-chi += unidentified-dependency|CSWpm-time-duration-parse

CONFIGURE_ARGS = 

include gar/category.mk

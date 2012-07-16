NAME = Time-Duration-Parse
VERSION = 0.06
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = MIYAGAWA

DESCRIPTION = Parse string that represents time duration
define BLURB
  Parse string that represents time duration
endef

DISTFILES += COPYING

PACKAGES = CSWpm-time-duration-parse
CATALOGNAME = pm_time_duration_parse
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-exporter-lite

# Remove on next build
CHECKPKG_OVERRIDES_CSWpm-time-duration-parse += unidentified-dependency|CSWpm-exporter-lite

CONFIGURE_ARGS = 

include gar/category.mk

NAME = DateTime-Set
VERSION = 0.31
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = FGLOCK

DESCRIPTION = Datetime sets and set math
define BLURB
  Datetime sets and set math
endef

LICENSE = LICENSE

PACKAGES = CSWpm-datetime-set
CATALOGNAME = pm_datetime_set
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-set-infinite

CONFIGURE_ARGS = 

# Remove this on next build
CHECKPKG_OVERRIDES_CSWpm-datetime-set += unidentified-dependency|CSWpm-set-infinite

include gar/category.mk

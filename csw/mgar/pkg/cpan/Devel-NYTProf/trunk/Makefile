NAME = Devel-NYTProf
VERSION = 4.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TIMB

DESCRIPTION = Powerful fast feature-rich perl source code profiler
define BLURB
  Powerful fast feature-rich perl source code profiler
endef

DISTFILES += COPYING

PACKAGES = CSWpm-devel-nytprof
CATALOGNAME = pm_devel_nytprof

RUNTIME_DEP_PKGS += CSWpm-json-any

# Temporary override since CSWpm-json-any is not released yet, remove this next time
CHECKPKG_OVERRIDES_CSWpm-devel-nytprof += unidentified-dependency|CSWpm-json-any

include gar/category.mk

NAME = Module-Load-Conditional
VERSION = 0.44
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BINGOS

DESCRIPTION = Query module information and load at runtime
define BLURB
  Module::Load::Conditional provides simple ways to query and possibly load
  any of the modules you have installed on your system during runtime.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-module-load-conditional
CATALOGNAME = pm_module_load_conditional
SPKG_DESC_CSWpm-module-load-conditional = $(DESCRIPTION)
ARCHALL = 1
OBSOLETED_BY_CSWpm-module-load-conditional = CSWpmmodloadcond
CATALOGNAME_CSWpmmodloadcond = pm_modloadcond

RUNTIME_DEP_PKGS = CSWpmprmscheck CSWpmmodload CSWpmlclemktxtsimple

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk

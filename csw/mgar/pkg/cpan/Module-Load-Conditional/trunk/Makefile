NAME = Module-Load-Conditional
VERSION = 0.38
CATEGORIES = cpan
AUTHOR = BINGOS

DESCRIPTION = Query module information and load at runtime
define BLURB
  Module::Load::Conditional provides simple ways to query and possibly load
  any of the modules you have installed on your system during runtime.
endef

DISTFILES += COPYING

PACKAGES = CSWpmmodloadcond
CATALOGNAME = pm_modloadcond
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmprmscheck CSWpmmodload CSWpmlclemktxtsimple

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk

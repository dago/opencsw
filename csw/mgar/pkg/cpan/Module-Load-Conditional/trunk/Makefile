GARNAME = Module-Load-Conditional
GARVERSION = 0.36
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

CHECKPKG_OVERRIDES_CSWpmmodloadcond += surplus-dependency|CSWpmprmscheck
CHECKPKG_OVERRIDES_CSWpmmodloadcond += surplus-dependency|CSWpmmodload
CHECKPKG_OVERRIDES_CSWpmmodloadcond += surplus-dependency|CSWpmlclemktxtsimple

DEPENDS += cpan/Params-Check
DEPENDS += cpan/Module-Load
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/version

include gar/category.mk

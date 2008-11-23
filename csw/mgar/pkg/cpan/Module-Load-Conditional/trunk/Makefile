GARNAME = Module-Load-Conditional
GARVERSION = 0.16
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Query module information and load at runtime
define BLURB
  Module::Load::Conditional provides simple ways to query and possibly load
  any of the modules you have installed on your system during runtime.
endef

DISTFILES += $(call admfiles,CSWpmmodloadcond,depend prototype)

DEPENDS += cpan/Params-Check
DEPENDS += cpan/Module-Load
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/version

include gar/category.mk

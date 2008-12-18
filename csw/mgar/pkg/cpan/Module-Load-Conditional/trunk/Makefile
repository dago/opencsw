GARNAME = Module-Load-Conditional
GARVERSION = 0.28
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Query module information and load at runtime
define BLURB
  Module::Load::Conditional provides simple ways to query and possibly load
  any of the modules you have installed on your system during runtime.
endef

DISTFILES += $(call admfiles,CSWpmmodloadcond,)

REQUIRED_PKGS = CSWpmprmscheck CSWpmmodload CSWpmlclemktxtsimple

#SKIPTEST = 1

DEPENDS += cpan/Params-Check
DEPENDS += cpan/Module-Load
DEPENDS += cpan/Locale-Maketext-Simple
DEPENDS += cpan/version

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

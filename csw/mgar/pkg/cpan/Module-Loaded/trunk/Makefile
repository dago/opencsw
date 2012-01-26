NAME = Module-Loaded
VERSION = 0.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BINGOS

DESCRIPTION = Mark modules as loaded or unloaded
define BLURB
  When testing applications, often you find yourself needing to provide
  functionality in your test environment that would usually be provided by
  external modules. Rather than munging the INC by hand to mark these external
  modules as loaded, so they are not attempted to be loaded by perl, this
  module offers you a very simple way to mark modules as loaded and/or
  unloaded.
endef

DISTFILES += COPYING

PACKAGES = CSWpmmodloaded
CATALOGNAME = pm_modloaded
ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk

GARNAME = Module-Loaded
GARVERSION = 0.01
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Mark modules as loaded or unloaded
define BLURB
  When testing applications, often you find yourself needing to provide
  functionality in your test environment that would usually be provided by
  external modules. Rather than munging the INC by hand to mark these external
  modules as loaded, so they are not attempted to be loaded by perl, this
  module offers you a very simple way to mark modules as loaded and/or
  unloaded.
endef

DISTFILES += $(call admfiles,CSWpmmodloaded,prototype)

include ../category.mk

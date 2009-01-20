GARNAME = Module-Load
GARVERSION = 0.14
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Runtime require of both modules and files
define BLURB
  Eliminates the need to know whether you are trying to require either a file
  or a module.
endef

DISTFILES += $(call admfiles,CSWpmmodload,)

#SKIPTEST = 1

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk

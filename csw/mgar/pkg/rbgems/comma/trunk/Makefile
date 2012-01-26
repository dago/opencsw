NAME = comma
VERSION = 0.4.1
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = Ruby Comma Seperated Values generation library

define BLURB
  Ruby Coma Seperated Values generation library
endef

RUNTIME_DEP_PKGS += CSWgem-rspec
RUNTIME_DEP_PKGS += CSWgem-activesupport

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*/\.gitignore

# These will go away when the packages have been released.
CHECKPKG_OVERRIDES_CSWgem-comma += unidentified-dependency|CSWgem-rspec
CHECKPKG_OVERRIDES_CSWgem-comma += unidentified-dependency|CSWgem-activesupport

include gar/category.mk

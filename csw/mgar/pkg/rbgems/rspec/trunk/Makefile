NAME = rspec
VERSION = 2.4.0
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = Meta-gem that depends on the other rspec gems

define BLURB
  Meta-gem that depends on the other rspec gems
endef

RUNTIME_DEP_PKGS += CSWgem-rspec-core
RUNTIME_DEP_PKGS += CSWgem-rspec-expectations
RUNTIME_DEP_PKGS += CSWgem-rspec-mocks

LICENSE = License.txt

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*/\.gitignore

# These will go away after official release
CHECKPKG_OVERRIDES_CSWgem-rspec += unidentified-dependency|CSWgem-rspec-core
CHECKPKG_OVERRIDES_CSWgem-rspec += unidentified-dependency|CSWgem-rspec-expectations
CHECKPKG_OVERRIDES_CSWgem-rspec += unidentified-dependency|CSWgem-rspec-mocks

include gar/category.mk

NAME = rspec-expectations
VERSION = 2.4.0
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = Rspec expectations (should[_not] and matchers)

define BLURB
  rspec expectations (should[_not] and matchers)
endef

RUNTIME_DEP_PKGS += CSWgem-diff-lcs

LICENSE = License.txt

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*/\.gitignore

# This will go away after official release
CHECKPKG_OVERRIDES_CSWgem-rspec-expectations += unidentified-dependency|CSWgem-diff-lcs

include gar/category.mk

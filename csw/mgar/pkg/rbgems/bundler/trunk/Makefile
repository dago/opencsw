NAME = bundler
VERSION = 1.0.13
CATEGORIES = rbgems

DESCRIPTION = Manages an application's dependencies through its entire life,
define BLURB
  Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
endef

PACKAGES = CSWgem-bundler
CATALOGNAME = gem_bundler

# This is docs only
CHECKPKG_OVERRIDES_CSWgem-bundler += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/bundler-1.0.13/lib/bundler/man/bundle-config
CHECKPKG_OVERRIDES_CSWgem-bundler += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/bundler-1.0.13/lib/bundler/man/bundle-config.txt
CHECKPKG_OVERRIDES_CSWgem-bundler += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/bundler-1.0.13/man/bundle-config.ronn

LICENSE = LICENSE

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES += .*/\.gitignore

include gar/category.mk

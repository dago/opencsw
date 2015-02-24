NAME = cache-money
VERSION = 0.2.5
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = Write-through and Read-through Cacheing for ActiveRecord

define BLURB
  Cache utilities.
endef

# I really don't have a clue
LICENSE =
CHECKPKG_OVERRIDES_CSWgem-cache-money += license-missing|/opt/csw/share/doc/gem_cache_money/license

RUNTIME_DEP_PKGS += CSWgem-activerecord
RUNTIME_DEP_PKGS += CSWgem-activesupport
RUNTIME_DEP_PKGS += CSWgem-memcache-client

ARCHALL = 1

# These will go away after gem release
CHECKPKG_OVERRIDES_CSWgem-cache-money += unidentified-dependency|CSWgem-activerecord
CHECKPKG_OVERRIDES_CSWgem-cache-money += unidentified-dependency|CSWgem-memcache-client
CHECKPKG_OVERRIDES_CSWgem-cache-money += unidentified-dependency|CSWgem-activesupport

include gar/category.mk

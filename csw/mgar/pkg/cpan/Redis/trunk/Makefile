NAME = Redis
VERSION = 1.951
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MELO

DESCRIPTION = Perl binding for Redis database
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-test-exception
BUILD_DEP_PKGS += CSWpm-io-string
BUILD_DEP_PKGS += CSWpm-test-deep

PACKAGES += CSWpm-redis
CATALOGNAME_CSWpm-redis = pm_redis
SPKG_DESC_CSWpm-redis = Perl binding for Redis database
ARCHALL_CSWpm-redis = 1
RUNTIME_DEP_PKGS_CSWpm-redis += CSWpm-try-tiny

include gar/category.mk

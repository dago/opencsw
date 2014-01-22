NAME = Test-Version
VERSION = 1.002004
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = XENO

DESCRIPTION = Check to see that version's in modules are sane
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-exception
BUILD_DEP_PKGS += CSWpm-test-tester

PACKAGES += CSWpm-test-version
CATALOGNAME_CSWpm-test-version = pm_test_version
SPKG_DESC_CSWpm-test-version = Check to see that version's in modules are sane
ARCHALL_CSWpm-test-version = 1
RUNTIME_DEP_PKGS_CSWpm-test-version += CSWpm-file-find-rule-perl
RUNTIME_DEP_PKGS_CSWpm-test-version += CSWpm-module-metadata

include gar/category.mk

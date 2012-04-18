NAME = Class-Load
VERSION = 0.19
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DOY

DESCRIPTION = A working (require "Class::Name") and more
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-class-load
CATALOGNAME_CSWpm-class-load = pm_class_load
SPKG_DESC_CSWpm-class-load = A working (require "Class::Name") and more
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-class-load = 1
RUNTIME_DEP_PKGS_CSWpm-class-load += CSWpm-module-implementation
RUNTIME_DEP_PKGS_CSWpm-class-load += CSWpm-try-tiny
RUNTIME_DEP_PKGS_CSWpm-class-load += CSWpm-data-optlist
RUNTIME_DEP_PKGS_CSWpm-class-load += CSWpm-package-stash
RUNTIME_DEP_PKGS_CSWpm-class-load += CSWpm-module-runtime

include gar/category.mk

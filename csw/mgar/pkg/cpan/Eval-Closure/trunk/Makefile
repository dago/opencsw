NAME = Eval-Closure
VERSION = 0.08
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DOY

DESCRIPTION = Safely and cleanly create closures via string eval
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-eval-closure
CATALOGNAME_CSWpm-eval-closure = pm_eval_closure
SPKG_DESC_CSWpm-eval-closure = Safely and cleanly create closures via string eval
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-eval-closure = 1
RUNTIME_DEP_PKGS_CSWpm-eval-closure += CSWpm-sub-exporter
RUNTIME_DEP_PKGS_CSWpm-eval-closure += CSWpm-try-tiny

include gar/category.mk

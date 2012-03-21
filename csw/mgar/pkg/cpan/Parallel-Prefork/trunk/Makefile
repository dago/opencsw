NAME = Parallel-Prefork
VERSION = 0.13
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KAZUHO

DESCRIPTION = A simple prefork server framework
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-test-sharedfork
BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-parallel-prefork
CATALOGNAME_CSWpm-parallel-prefork = pm_parallel_prefork
SPKG_DESC_CSWpm-parallel-prefork = A simple prefork server framework
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-parallel-prefork = 1
RUNTIME_DEP_PKGS_CSWpm-parallel-prefork += CSWpm-class-accessor-lite
RUNTIME_DEP_PKGS_CSWpm-parallel-prefork += CSWpm-scope-guard
RUNTIME_DEP_PKGS_CSWpm-parallel-prefork += CSWpm-list-moreutils
RUNTIME_DEP_PKGS_CSWpm-parallel-prefork += CSWpm-proc-wait3

include gar/category.mk

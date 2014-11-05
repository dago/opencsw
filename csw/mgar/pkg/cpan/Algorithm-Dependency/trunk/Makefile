NAME = Algorithm-Dependency
VERSION = 1.110
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Base class for implementing various dependency trees
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-classapi

PACKAGES += CSWpm-algorithm-dependency
CATALOGNAME_CSWpm-algorithm-dependency = pm_algorithm_dependency
SPKG_DESC_CSWpm-algorithm-dependency = Base class for implementing various dependency trees
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-algorithm-dependency = 1
RUNTIME_DEP_PKGS_CSWpm-algorithm-dependency += CSWpm-params-util
OBSOLETED_BY_CSWpm-algorithm-dependency += CSWpmalgorithmdep
CATALOGNAME_CSWpmalgorithmdep = pm_algorithmdep_stub

include gar/category.mk

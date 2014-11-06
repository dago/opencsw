NAME = File-Flat
VERSION = 1.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Implements a flat filesystem
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-classapi

PACKAGES += CSWpm-file-flat
CATALOGNAME_CSWpm-file-flat = pm_file_flat
SPKG_DESC_CSWpm-file-flat = Implements a flat filesystem
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-file-flat = 1
RUNTIME_DEP_PKGS_CSWpm-file-flat += CSWpm-file-copy-recursive
RUNTIME_DEP_PKGS_CSWpm-file-flat += CSWpm-prefork
RUNTIME_DEP_PKGS_CSWpm-file-flat += CSWpm-file-remove
OBSOLETED_BY_CSWpm-file-flat += CSWpmfileflat
CATALOGNAME_CSWpmfileflat = pm_fileflat_stub

include gar/category.mk

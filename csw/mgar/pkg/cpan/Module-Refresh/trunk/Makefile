NAME = Module-Refresh
VERSION = 0.17
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ALEXMV

DESCRIPTION = Refresh %INC files when updated on disk
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-path-class

PACKAGES += CSWpm-module-refresh
CATALOGNAME_CSWpm-module-refresh = pm_module_refresh
SPKG_DESC_CSWpm-module-refresh = Refresh %INC files when updated on disk
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-module-refresh = 1
OBSOLETED_BY_CSWpm-module-refresh += CSWpmmodrefresh
CATALOGNAME_CSWpmmodrefresh = pm_modrefresh_stub

include gar/category.mk

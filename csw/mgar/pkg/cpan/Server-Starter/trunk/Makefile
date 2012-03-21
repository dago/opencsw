NAME = Server-Starter
VERSION = 0.11
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KAZUHO

DESCRIPTION = A superdaemon for hot-deploying server programs
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

PACKAGES += CSWpm-server-starter
CATALOGNAME_CSWpm-server-starter = pm_server_starter
SPKG_DESC_CSWpm-server-starter = A superdaemon for hot-deploying server programs
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-server-starter = 1
RUNTIME_DEP_PKGS_CSWpm-server-starter += CSWpm-scope-guard
RUNTIME_DEP_PKGS_CSWpm-server-starter += CSWpm-list-moreutils
RUNTIME_DEP_PKGS_CSWpm-server-starter += CSWpm-proc-wait3

include gar/category.mk

NAME = Starlet
VERSION = 0.14
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KAZUHO

DESCRIPTION = A simple, high-performance PSGI/Plack HTTP server
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-test-tcp

PACKAGES += CSWpm-starlet
CATALOGNAME_CSWpm-starlet = pm_starlet
SPKG_DESC_CSWpm-starlet = A simple, high-performance PSGI/Plack HTTP server
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-starlet = 1
RUNTIME_DEP_PKGS_CSWpm-starlet += CSWpm-parallel-prefork
RUNTIME_DEP_PKGS_CSWpm-starlet += CSWpm-server-starter
RUNTIME_DEP_PKGS_CSWpm-starlet += CSWpm-plack

include gar/category.mk

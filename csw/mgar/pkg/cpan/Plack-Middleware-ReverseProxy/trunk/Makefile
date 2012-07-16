NAME = Plack-Middleware-ReverseProxy
VERSION = 0.14
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIYAGAWA

DESCRIPTION = Supports app to run as a reverse proxy backend
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-test-base

PACKAGES += CSWpm-plack-middleware-reversep
SPKG_DESC_CSWpm-plack-middleware-reversep = Supports app to run as a reverse proxy backend
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-plack-middleware-reversep = 1
RUNTIME_DEP_PKGS_CSWpm-plack-middleware-reversep += CSWpm-yaml
RUNTIME_DEP_PKGS_CSWpm-plack-middleware-reversep += CSWpm-plack

# The tests contain now a port as result, I guess this is ok.
SKIPTEST ?= 1

include gar/category.mk

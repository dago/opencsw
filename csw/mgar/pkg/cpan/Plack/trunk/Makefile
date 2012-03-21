NAME = Plack
VERSION = 0.9986
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIYAGAWA

DESCRIPTION = Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-plack
CATALOGNAME_CSWpm-plack = pm_plack
SPKG_DESC_CSWpm-plack = Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-plack = 1
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-filesys-notify-simple
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-http-body
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-uri
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-devel-stacktrace-ashtml
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-libwww-perl
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-try-tiny
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-devel-stacktrace
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-test-tcp
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-file-sharedir
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-hash-multivalue

include gar/category.mk

NAME = Plack
VERSION = 0.9970
CATEGORIES = cpan
AUTHOR = MIYAGAWA

DESCRIPTION = Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
define BLURB
endef

BUILD_DEP_PKGS += CSWpm-test-requires

LICENSE = README

PACKAGES += CSWpm-plack
CATALOGNAME_CSWpm-plack = pm_plack
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-plack = 1
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-try-tiny
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-hash-multivalue
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpmuri
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpmdevstacktrace
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-http-body
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-test-tcp
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-file-sharedir
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-filesys-notify-simple
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpm-devel-stacktrace-ashtml
RUNTIME_DEP_PKGS_CSWpm-plack += CSWpmlibwww

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWpm-plack)

include gar/category.mk

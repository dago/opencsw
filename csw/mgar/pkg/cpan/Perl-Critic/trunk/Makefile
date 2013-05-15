NAME = Perl-Critic
VERSION = 1.118
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = THALJEF

DESCRIPTION = Critique Perl source code for best-practices
define BLURB
endef

PACKAGES = CSWpm-perl-critic
CATALOGNAME = pm_perl_critic
ARCHALL = 1

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build
BUILD_DEP_PKGS += CSWpm-test-deep

# Required
RUNTIME_DEP_PKGS += CSWpmbkeywords
RUNTIME_DEP_PKGS += CSWpm-config-tiny
RUNTIME_DEP_PKGS += CSWpm-email-address
RUNTIME_DEP_PKGS += CSWpm-exception-class
RUNTIME_DEP_PKGS += CSWpm-io-string
RUNTIME_DEP_PKGS += CSWpm-list-moreutils
RUNTIME_DEP_PKGS += CSWpm-ppi
RUNTIME_DEP_PKGS += CSWpm-ppix-regexp
RUNTIME_DEP_PKGS += CSWpm-ppix-utilities
RUNTIME_DEP_PKGS += CSWperltidy
RUNTIME_DEP_PKGS += CSWpm-pod-spell
RUNTIME_DEP_PKGS += CSWpmreadonly
RUNTIME_DEP_PKGS += CSWpm-string-format
RUNTIME_DEP_PKGS += CSWpm-task-weaken

# Recommended
RUNTIME_DEP_PKGS += CSWpmfilehomedir
RUNTIME_DEP_PKGS += CSWpm-file-which
RUNTIME_DEP_PKGS += CSWpm-readonly-xs

include gar/category.mk


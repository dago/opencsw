# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Perl-Critic
VERSION = 1.116
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = ELLIOTJS

DESCRIPTION = Critique Perl source code for best-practices
define BLURB
  Critique Perl source code for best-practices
endef

PACKAGES = CSWpm-perl-critic
CATALOGNAME = pm_perl_critic
ARCHALL = 1

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpmreadline

RUNTIME_DEP_PKGS += CSWperltidy
RUNTIME_DEP_PKGS += CSWpm-email-address
RUNTIME_DEP_PKGS += CSWpm-pod-spell
RUNTIME_DEP_PKGS += CSWpm-ppi
RUNTIME_DEP_PKGS += CSWpm-ppix-regexp
RUNTIME_DEP_PKGS += CSWpm-ppix-utilities
RUNTIME_DEP_PKGS += CSWpm-string-format
RUNTIME_DEP_PKGS += CSWpmbkeywords
RUNTIME_DEP_PKGS += CSWpmconfigtiny
RUNTIME_DEP_PKGS += CSWpmtestdeep

# Unreleased deps, remove next time
CHECKPKG_OVERRIDES_CSWpm-perl-critic += unidentified-dependency|CSWpm-email-address
CHECKPKG_OVERRIDES_CSWpm-perl-critic += unidentified-dependency|CSWpm-pod-spell
CHECKPKG_OVERRIDES_CSWpm-perl-critic += unidentified-dependency|CSWpm-ppi
CHECKPKG_OVERRIDES_CSWpm-perl-critic += unidentified-dependency|CSWpm-ppix-regexp
CHECKPKG_OVERRIDES_CSWpm-perl-critic += unidentified-dependency|CSWpm-ppix-utilities
CHECKPKG_OVERRIDES_CSWpm-perl-critic += unidentified-dependency|CSWpm-string-format

# Harmless documentation examples
CHECKPKG_OVERRIDES_CSWpm-perl-critic += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/Perl/Critic/Policy/CodeLayout/RequireTidyCode.pm
CHECKPKG_OVERRIDES_CSWpm-perl-critic += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/Perl::Critic::Policy::CodeLayout::RequireTidyCode.3perl

include gar/category.mk


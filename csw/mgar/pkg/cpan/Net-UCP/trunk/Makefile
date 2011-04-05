NAME = Net-UCP
VERSION = 0.41
CATEGORIES = cpan
AUTHOR = NEMUX

DESCRIPTION = Perl extension for EMI UCP Protocol
define BLURB
  Perl extension for EMI - UCP Protocol
endef

MODDIST = $(NAME)-$(VERSION).tgz

PACKAGES = CSWpmnetucp
CATALOGNAME = pm_netucp

CHECKPKG_OVERRIDES_CSWpmnetucp += catalogname-does-not-match-pkgname|pkgname=CSWpmnetucp|catalogname=pm_netucp|expected-catalogname=pmnetucp

DISTFILES += LICENSE
ARCHALL = 1

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWpmnetucp = CSWpmnetucpcommon
RUNTIME_DEP_PKGS_CSWpmnetucp = CSWpmnetucpinttimeout
RUNTIME_DEP_PKGS_CSWpmnetucp = CSWpmnetucptransactionmanager

include gar/category.mk

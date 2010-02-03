GARNAME = Module-Build
GARVERSION = 0.33
CATEGORIES = cpan
AUTHOR = EWILHELM

DESCRIPTION = build and install Perl modules
define BLURB
  Module::Build is a system for building, testing, and installing Perl
  modules.  It is meant to be a replacement for ExtUtils::MakeMaker.
  Developers may alter the behavior of the module through subclassing in a
  much more straightforward way than with MakeMaker.
endef

LICENSE = LICENSE

PACKAGES = CSWpmmodulebuild
CATALOGNAME = pm_modulebuild

RUNTIME_DEP_PKGS = CSWpmarchivetar CSWpmextutparsexs CSWpmextutcbuilder CSWpmmodulesign
BUILD_DEP_PKGS = CSWperl

ARCHALL = 1

include gar/category.mk

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

#DISTFILES += $(call admfiles,CSWpmmodulebuild,depend prototype)

PACKAGES = CSWpmmodulebuild
CATALOGNAME = pm_modulebuild
REQUIRED_PKGS = CSWpmarchivetar CSWpmextutparsexs CSWpmyaml

LICENSE = LICENSE

DEPENDS += cpan/YAML
DEPENDS += cpan/ExtUtils-ParseXS
DEPENDS += cpan/Archive-Tar

CONFIGURE_ARGS = destdir=$(DESTDIR)

ARCHALL = 1

include gar/category.mk

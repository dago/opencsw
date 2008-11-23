GARNAME = Module-Build
GARVERSION = 0.2806
CATEGORIES = cpan
AUTHOR = KWILLIAMS

DESCRIPTION = build and install Perl modules
define BLURB
  Module::Build is a system for building, testing, and installing Perl
  modules.  It is meant to be a replacement for ExtUtils::MakeMaker.
  Developers may alter the behavior of the module through subclassing in a
  much more straightforward way than with MakeMaker.
endef

DISTFILES += $(call admfiles,CSWpmmodulebuild,depend prototype)

DEPENDS += cpan/YAML
DEPENDS += cpan/ExtUtils-ParseXS
DEPENDS += cpan/Archive-Tar

CONFIGURE_ARGS = destdir=$(DESTDIR)

include gar/category.mk

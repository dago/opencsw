GARNAME = Module-Build
GARVERSION = 0.2612
CATEGORIES = cpan
AUTHOR = KWILLIAMS

DESCRIPTION = build and install Perl modules
define BLURB
  Module::Build is a system for building, testing, and installing Perl
  modules.  It is meant to be a replacement for ExtUtils::MakeMaker.
  Developers may alter the behavior of the module through subclassing in a
  much more straightforward way than with MakeMaker.
endef

DISTFILES += $(call admfiles,CSWpmmodulebuild,)

DEPENDS += cpan/YAML cpan/ExtUtils-ParseXS cpan/Archive-Tar

CONFIGURE_ARGS = destdir=$(DESTDIR)

include ../category.mk

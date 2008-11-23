GARNAME = ExtUtils-AutoInstall
GARVERSION = 0.63
CATEGORIES = cpan
AUTHOR = AUTRIJUS

DESCRIPTION = Automatic install of dependencies via CPAN
define BLURB
  ExtUtils::AutoInstall lets module writers to specify a more sophisticated
  form of dependency information than the PREREQ_PM option offered by
  ExtUtils::MakeMaker.
endef

DISTFILES += $(call admfiles,CSWpmextutautoinst,depend)

DEPENDS += cpan/ExtUtils-Manifest
DEPENDS += cpan/CPANPLUS
DEPENDS += cpan/Sort-Versions

include gar/category.mk


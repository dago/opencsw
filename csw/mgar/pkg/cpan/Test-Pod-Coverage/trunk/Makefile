GARNAME = Test-Pod-Coverage
GARVERSION = 1.08
CATEGORIES = cpan
AUTHOR = PETDANCE

DESCRIPTION = Check for pod coverage in your distribution
define BLURB
endef

DISTFILES += $(call admfiles,CSWpmtestpodcoverage,depend)

DEPENDS   += cpan/Pod-Simple cpan/IO-stringy
BUILDDEPS += cpan/Test-Builder-Tester

include gar/category.mk

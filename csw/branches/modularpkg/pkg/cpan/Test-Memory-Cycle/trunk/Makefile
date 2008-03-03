GARNAME = Test-Memory-Cycle
GARVERSION = 1.04
CATEGORIES = cpan
AUTHOR = PETDANCE

DESCRIPTION = check for memory leaks and circular memory references
define BLURB
  Perl's garbage collection has one big problem: Circular references can't get
  cleaned up. Test::Memory::Cycle is built on top of Devel::Cycle to give you
  an easy way to check for these circular references.
endef

DISTFILES += CSWpmtestmemcycle.gspec CSWpmtestmemcycle.depend

DEPENDS   += cpan/Devel-Cycle
BUILDDEPS += cpan/Test-Builder-Tester

include gar/category.mk

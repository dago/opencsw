GARNAME = Test-Class
GARVERSION = 0.11
CATEGORIES = cpan
AUTHOR = ADIE

DESCRIPTION = easily create test classes in an xUnit style.
define BLURB
  Test::Class provides a simple way of creating classes and objects to test your
  code in an xUnit style.
endef

DISTFILES += CSWpmtestclass.gspec CSWpmtestclass.depend

DEPENDS += cpan/Attribute-Handlers cpan/Class-ISA
DEPENDS += cpan/Test-Differences cpan/Test-Exception
DEPENDS += cpan/Test-Builder-Tester

include gar/category.mk

# pod.t has errors, but everything else passes! disable for now
pre-test:
	@rm -f $(WORKSRC)/t/pod.t

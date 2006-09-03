GARNAME = Test-Pod
GARVERSION = 1.26
CATEGORIES = cpan
AUTHOR = PETDANCE

DESCRIPTION = check for POD errors in files
define BLURB
  Check POD files for errors or warnings in a test file, using Pod::Simple to
  do the heavy lifting.
endef

DISTFILES += CSWpmtestpod.gspec CSWpmtestpod.depend

DEPENDS   += cpan/Pod-Simple cpan/IO-stringy
BUILDDEPS += cpan/Test-Builder-Tester

include ../category.mk

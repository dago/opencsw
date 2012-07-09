NAME = Test-MockObject
VERSION = 1.20120301
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHROMATIC

DESCRIPTION = Extension for emulating troublesome interfaces
define BLURB
  It's a simple program that doesn't use any other modules, and those are easy
  to test. More often, testing a program completely means faking up input to
  another module, trying to coax the right output from something you're not
  supposed to be testing anyway.
endef

LICENSE = $(FILEDIR)/LICENSE

PACKAGES = CSWpm-test-mockobject
CATALOGNAME = pm_test_mockobject
SPKG_DESC_CSWpm-test-mockobject = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-test-mockobject = CSWpmtstmockobject
CATALOGNAME_CSWpmtstmockobject = pm_tstmockobject_stub

RUNTIME_DEP_PKGS += CSWpm-test-exception
RUNTIME_DEP_PKGS += CSWpmuniversalisa
RUNTIME_DEP_PKGS += CSWpmuniversalcan

ARCHALL = 1

CONFIGURE_ARGS =

include gar/category.mk

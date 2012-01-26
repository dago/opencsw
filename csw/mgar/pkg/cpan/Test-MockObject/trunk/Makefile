NAME = Test-MockObject
VERSION = 1.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHROMATIC

DESCRIPTION = extension for emulating troublesome interfaces
define BLURB
  It's a simple program that doesn't use any other modules, and those are easy
  to test. More often, testing a program completely means faking up input to
  another module, trying to coax the right output from something you're not
  supposed to be testing anyway.
endef

PACKAGES = CSWpmtstmockobject
CATALOGNAME = pm_tstmockobject

DEP_PKGS = CSWpmtstexception CSWpmuniversalisa CSWpmuniversalcan

ARCHALL = 1

LICENSE = $(FILEDIR)/LICENSE

CHECKPKG_OVERRIDES_CSWpmtstmockobject += surplus-dependency|CSWpmtstexception
CHECKPKG_OVERRIDES_CSWpmtstmockobject += surplus-dependency|CSWpmuniversalisa
CHECKPKG_OVERRIDES_CSWpmtstmockobject += surplus-dependency|CSWpmuniversalcan

include gar/category.mk

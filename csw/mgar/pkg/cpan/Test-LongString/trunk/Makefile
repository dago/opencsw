NAME = Test-LongString
VERSION = 0.14
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RGARCIA

DESCRIPTION = Tests strings for equality
define BLURB
  This module provides some drop-in replacements for the string comparison
  functions of Test::More, but which are more suitable when you test against
  long strings. If you've ever had to search for text in a multi-line string
  like an HTML document, or find specific items in binary data, this is the
  module for you.
endef

DISTFILES = COPYING

PACKAGES = CSWpmtestlongstring CSWpmtestlongstr

CATALOGNAME_CSWpmtestlongstring = pm_testlongstring
CATALOGNAME_CSWpmtestlongstr = pm_testlongstr

SPKG_DESC_CSWpmtestlongstring = $(DESCRIPTION)
SPKG_DESC_CSWpmtestlongstr = Empty stub as contents has been moved to CSWpmtestlongstring

RUNTIME_DEP_PKGS_ONLY_CSWpmtestlongstr = CSWpmtestlongstring

ARCHALL = 1

PKGFILES_CSWpmtestlongstr = NOFILES

include gar/category.mk

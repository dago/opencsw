GARNAME = XML-DOM
GARVERSION = 1.44
CATEGORIES = cpan
AUTHOR = TJMATHER

DESCRIPTION = module for building DOM Level 1 compliant document structures
define BLURB
  This module extends the XML::Parser module by Clark Cooper. The XML::Parser
  module is built on top of XML::Parser::Expat, which is a lower level
  interface to James Clark's expat library.
endef

DISTFILES += $(call admfiles,CSWpmxmldom,depend)

#DEPENDS += cpan/XML-Parser
DEPENDS += cpan/XML-RegExp
#DEPENDS += cpan/libwww-perl
DEPENDS += cpan/libxml-perl

# I don't know enough about Unicode to debug this test, but I suspect
# it's just a matter of the test not being properly maintained.
#ENABLE_TEST = 0

include ../category.mk

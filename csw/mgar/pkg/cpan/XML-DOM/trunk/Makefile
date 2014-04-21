NAME = XML-DOM
VERSION = 1.44
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TJMATHER

DESCRIPTION = Building DOM Level 1 compliant document structures
define BLURB
  This module extends the XML::Parser module by Clark Cooper. The XML::Parser
  module is built on top of XML::Parser::Expat, which is a lower level
  interface to James Clark's expat library.
endef

# DISTFILES += $(call admfiles,CSWpmxmldom,depend)

PACKAGES = CSWpm-xmldom
SPKG_DESC_CSWpm-xmldom = $(DESCRIPTION)
ARCHALL_CSWpm-xmldom = 1

OBSOLETED_BY_CSWpm-xmldom = CSWpmxmldom

#DEPENDS += cpan/XML-Parser
DEPENDS += cpan/XML-RegExp
#DEPENDS += cpan/libwww-perl
DEPENDS += cpan/libxml-perl

include gar/category.mk

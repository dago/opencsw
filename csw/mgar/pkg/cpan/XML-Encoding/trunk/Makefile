NAME = XML-Encoding
VERSION = 2.08
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHAY

DESCRIPTION = module for parsing XML encoding maps.
define BLURB
  This module, which is built as a subclass of XML::Parser, provides a parser
  for encoding map files, which are XML files. The file maps/encmap.dtd in the
  distribution describes the structure of these files. Calling a parse method
  returns the name of the encoding map (obtained from the name attribute of
  the root element). The contents of the map are processed through the
  callback functions push_prefix, pop_prefix, and range_set.
endef

CATALOGNAME     = pm_xml_encoding
PACKAGES	= CSWpm-xml-encoding

ARCHALL_CSWpm-xml-encoding = 1

LICENSE = README

RUNTIM_DEP_PKGS = CSWpmxmlparser

include gar/category.mk

GARNAME = XML-LibXML-Common
GARVERSION = 0.13
CATEGORIES = cpan
AUTHOR = PHISH

DESCRIPTION = routines and constants common for XML::LibXML and XML::GDOME
define BLURB
  XML::LibXML and XML::GDOME share some of the same functionality. This
  package should bundle some shared constansts and functions, so both modules
  may coexist within the same scripts.
endef

DISTFILES += $(call admfiles,CSWpmxmllibxmlcom,depend prototype)

DEPENDS += lib/libxml2

include ../category.mk

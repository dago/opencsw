GARNAME = XML-LibXML
GARVERSION = 1.58
CATEGORIES = cpan
AUTHOR = PHISH

DESCRIPTION = binding for libxml2
define BLURB
  This module is an interface to the gnome libxml2 DOM and SAX parser and the
  DOM tree. It also provides an XML::XPath-like findnodes() interface,
  providing access to the XPath API in libxml2. The module is split into
  several packages which are not described in this section.
endef

DISTFILES += $(call admfiles,CSWpmxmllibxml,depend prototype)

DEPENDS += cpan/XML-LibXML-Common
DEPENDS += cpan/XML-NamespaceSupport
DEPENDS += cpan/XML-SAX

include ../category.mk

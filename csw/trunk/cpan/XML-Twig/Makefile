GARNAME = XML-Twig
GARVERSION = 3.29
CATEGORIES = cpan
AUTHOR = MIROD

DESCRIPTION = a module for processing huge XML documents in tree mode.
define BLURB
  This module provides a way to process XML documents. It is build on top of
  XML::Parser.  The module offers a tree interface to the document, while
  allowing you to output the parts of it that have been completely processed.
endef

DISTFILES = $(call admfiles,CSWpmxmltwig,depend prototype)

DEPENDS += cpan/XML-Parser

# Force installation without prompting
PATCHFILES = install.diff

include ../category.mk

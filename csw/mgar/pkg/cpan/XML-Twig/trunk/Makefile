NAME = XML-Twig
VERSION = 3.34
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIROD

DESCRIPTION = A module for processing huge XML documents in tree mode.
define BLURB
  This module provides a way to process XML documents. It is build on top of
  XML::Parser.  The module offers a tree interface to the document, while
  allowing you to output the parts of it that have been completely processed.
endef


PACKAGES = CSWpmxmltwig
CATLOGNAME_CSWpmxmltwig = pm_xmltwig

RUNTIME_DEP_PKGS += CSWpmxmlparser

ARCHALL_CSWpmxmltwig = 1

# Force installation without prompting
PATCHFILES = install.diff

include gar/category.mk

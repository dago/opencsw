GARNAME = XML-SemanticDiff
GARVERSION = 0.95
CATEGORIES = cpan
AUTHOR = KHAMPTON

DESCRIPTION = extension for comparing XML documents.
define BLURB
  XML::SematicDiff provides a way to compare the contents and structure of two
  XML documents. By default, it returns a list of hashrefs where each hashref
  describes a single difference between the two docs.
endef

DISTFILES += $(call admfiles,CSWpmxmlsemdiff,depend prototype)

DEPENDS += cpan/libxml-perl

include gar/category.mk

GARNAME = XML-Smart
GARVERSION = 1.6.9
CATEGORIES = cpan
AUTHOR = GMPASSOS

DESCRIPTION = a smart, easy and powerful way to access/create XML files/data.
define BLURB
  This module has an easy way to access/create XML data. It's based on the
  HASH tree that is made of the XML data, and enable a dynamic access to it
  with the Perl syntax for Hashe and Array, without needing to care if you
  have a Hashe or an Array in the tree. In other words, each point in the tree
  work as a Hash and an Array at the same time!
endef

DISTFILES = $(call admfiles,CSWpmxmlsmart,depend prototype)

DEPENDS += cpan/Object-MultiType

# Disable the URL test
PATCHFILES = url_test.diff

include ../category.mk

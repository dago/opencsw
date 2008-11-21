GARNAME = Tree-Simple
GARVERSION = 1.16
CATEGORIES = cpan
AUTHOR = STEVAN

DESCRIPTION = a simple tree object
define BLURB
  This module in an fully object-oriented implementation of a simple n-ary
  tree.  It is built upon the concept of parent-child relationships, so
  therefore every Tree::Simple object has both a parent and a set of children
  (who themselves may have children, and so on). Every Tree::Simple object
  also has siblings, as they are just the children of their immediate parent.
endef

DISTFILES += CSWpmtreesimple.gspec

BUILDDEPS += cpan/Test-Exception

include ../category.mk

GARNAME = Pod-POM
GARVERSION = 0.17
CATEGORIES = cpan
AUTHOR = ABW

DESCRIPTION = POD Object Model
define BLURB
  This module implements a parser to convert Pod documents into a simple
  object model form known hereafter as the Pod Object Model. The object model
  is generated as a hierarchical tree of nodes, each of which represents a
  different element of the original document. The tree can be walked manually
  and the nodes examined, printed or otherwise manipulated. In addition,
  Pod::POM supports and provides view objects which can automatically traverse
  the tree, or section thereof, and generate an output representation in one
  form or another.
endef

DISTFILES += CSWpmpodpom.gspec CSWpmpodpom.depend

#DEPENDS += cpan/Text-Diff

# The 'htmlview' function is currently broken (0.17)
# =for sections are being ignored!
PATCHFILES = htmlview.diff

include gar/category.mk

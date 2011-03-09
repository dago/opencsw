NAME = Pod-POM
VERSION = 0.27
CATEGORIES = cpan
AUTHOR = ANDREWF

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

DISTFILES += COPYING

PACKAGES = CSWpm-pod-pom
CATALOGNAME_CSWpm-pod-pom = pm_pod_pom
SPKG_DESC_CSWpm-pod-pom = $(DESCRIPTION)
OBSOLETES_CSWpm-pod-pom = CSWpmpodpom
CATALOGNAME_CSWpmpodpom = pm_podpom

ARCHALL = 1

include gar/category.mk

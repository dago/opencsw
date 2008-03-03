GARNAME = GraphViz
GARVERSION = 2.02
CATEGORIES = cpan
AUTHOR = LBROCARD

DESCRIPTION = interface to the GraphViz graphing tool
define BLURB
  This module provides an interface to layout and image generation of directed
  and undirected graphs in a variety of formats (PostScript, PNG, etc.) using
  the "dot", "neato" and "twopi" programs from the GraphViz project
  (http://www.graphviz.org/ or
  http://www.research.att.com/sw/tools/graphviz/).
endef

DISTFILES += CSWpmgraphviz.gspec CSWpmgraphviz.depend

DEPENDS += utils/graphviz
DEPENDS += cpan/Graph cpan/Math-Bezier cpan/Heap

include gar/category.mk

GARNAME = graphviz
GARVERSION = 1.18
CATEGORIES = utils

DESCRIPTION = Graph drawing utilities with web and graphical interfaces.
define BLURB
    graphviz is a set of graph drawing tools and libraries. It supports
    hierarchical and mass-spring drawings; although the tools are scalable, their
    emphasis is on making very good drawings of reasonably-sized graphs.
endef

MASTER_SITES = http://www.graphviz.org/pub/graphviz/ARCHIVE/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWgraphviz,depend)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk

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
DISTFILES += CSWgraphviz.gspec CSWgraphviz.depend CSWgraphviz.prototype

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk

# Prevent grammars and parsers from being regenerated
pre-build:
	@( cd $(WORKSRC) ; \
		touch \
			dotneato/common/htmlparse.[ch] \
			graph/parser.[ch]              \
			lefty/parse.[ch]               \
			lefty/dot2l/dotparse.[ch]      \
			tools/expr/exparse.[ch]        \
			tools/gpr/parse.[ch]           \
			agraph/grammar.[ch]            \
	)
	@$(MAKECOOKIE)

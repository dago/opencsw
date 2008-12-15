GARNAME = graphviz
GARVERSION = 1.18
CATEGORIES = utils

DESCRIPTION = Graph drawing utilities with web and graphical interfaces.
define BLURB
    graphviz is a set of graph drawing tools and libraries. It supports
    hierarchical and mass-spring drawings; although the tools are scalable, their
    emphasis is on making very good drawings of reasonably-sized graphs.
endef

MASTER_SITES = http://www.graphviz.org/pub/graphviz/stable/SOURCES/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWgraphviz)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS  = CSWexpat CSWfconfig CSWftype2 CSWgd CSWiconv CSWjpeg
REQUIRED_PKGS += CSWpng CSWxpm CSWzlib CSWsunmath
INCOMPATIBLE_PKGS = CSWgraphvis

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

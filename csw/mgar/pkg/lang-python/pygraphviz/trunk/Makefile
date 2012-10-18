# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pygraphviz
VERSION = 1.1
GARTYPE = v2
CATEGORIES = lang

DESCRIPTION =  Python interface to the Graphviz graph layout and visualization
define BLURB
  PyGraphviz is a Python interface to the Graphviz graph layout and visualization package. With PyGraphviz you can create, edit, read, write, and draw graphs using Python to access the Graphviz graph data structure and layout algorithms. PyGraphviz is independent from NetworkX but provides a similar programming interface.
endef

MASTER_SITES = http://pypi.python.org/packages/source/p/pygraphviz/
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = README.txt

GARCOMPILER = SOS12U3

BUILD_DEP_PKGS += CSWgraphvizdevel

PACKAGES = CSWpy-pygraphviz
RUNTIME_DEP_PKGS_CSWpy-pygraphviz += CSWpython
RUNTIME_DEP_PKGS_CSWpy-pygraphviz += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pygraphviz += CSWlibcgraph6

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py 
INSTALL_ARGS = --root=$(DESTDIR)


include gar/category.mk


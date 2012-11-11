# $Id$
#
NAME = gnuplot.py
VERSION = 1.8
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A Python interface to the gnuplot plotting program
define BLURB
  Gnuplot.py is a Python package that interfaces to gnuplot, the
  popular open-source plotting program. It allows you to use gnuplot
  from within Python to plot arrays of data from memory, data files, or
  mathematical functions. If you use Python to perform computations or
  as 'glue' for numerical programs, you can use this package to plot
  data on the fly as they are computed. And the combination with Python
  makes it is easy to automate things, including creating crude
  'animations' by plotting different datasets one after another.
endef

SF_PROJECT = $(subst .,-,$(NAME))
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(SF_PROJ)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES = CSWpy-gnuplot
CATALOGNAME_CSWpy-gnuplot = py_gnuplot

BUILD_DEP_PKGS += CSWpy-numpy CSWpython-dev
RUNTIME_DEP_PKGS += CSWgnuplot
TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWpy-gnuplot += surplus-dependency|CSWgnuplot

LICENSE = LICENSE.txt
ARCHALL = 1

include gar/category.mk

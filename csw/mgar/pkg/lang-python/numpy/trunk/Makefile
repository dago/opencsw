# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = numpy
VERSION = 1.5.1rc1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Standard numerical array library for python
define BLURB
  numpy is the standard numerical array library for python, the successor
  to Numeric and numarray. numpy provides fast operations for homogeneous
  data sets and common mathematical operations like correlations, standard
  deviation, fourier transforms, and convolutions.
endef

SPKG_SOURCEURL = http://numpy.scipy.org/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpy-numpy
CATALOGNAME = py_numpy

RUNTIME_DEP_PKGS_CSWpy-numpy += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-numpy += CSWss12f95rt
RUNTIME_DEP_PKGS_CSWpy-numpy += CSWsunmath

LICENSE = LICENSE.txt

export ATLAS = None
export BLAS = $(CC_HOME)/lib/libsunperf.so
export LAPACK = $(libdir)/libsunmath.so

TEST_SCRIPTS =
INSTALL_ARGS += --root=$(DESTDIR)

include gar/category.mk

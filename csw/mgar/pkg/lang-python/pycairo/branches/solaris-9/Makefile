# $Id$

NAME      = pycairo
VERSION   = 1.4.12
CATEGORIES   = python
GARTYPE = v2

DESCRIPTION  = Python binding for Cairo library
define BLURB
  This package contains the pycairo Python module which implements
  a binding the the cairo Library.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = pycairo-$(VERSION).tar.gz

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc

PACKAGES = CSWpycairo
SPKG_DESC_CSWpycairo = $(DESCRIPTION); main

CAIRO_LIBS = -L/opt/csw/lib -R/opt/csw/lib/\$$ISALIST -lcairo
CAIRO_CFLAGS = -I/opt/csw/include -I/opt/csw/include/cairo
EXTRA_BUILD_EXPORTS += CAIRO_LIBS CAIRO_CFLAGS

LICENSE = COPYING-LGPL-2.1

MODULATIONS_PYTHON_VERSION = 2_6

TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWpycairo += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpycairo += CSWlibcairo2

# Solaris 9 specifics.
CHECKPKG_OVERRIDES_CSWpycairo += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpycairo += catalogname-does-not-start-with-py_

include gar/category.mk

GARCOMPILER := SOS12

